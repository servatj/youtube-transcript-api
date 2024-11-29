from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import CouldNotRetrieveTranscript, TranscriptsDisabled
import os
from dotenv import load_dotenv
from assistant import OpenAIAssistant  # Import the assistant class


# Load environment variables from a .env file
load_dotenv()
# Initialize FastAPI app and OpenAI Assistant
app = FastAPI()
assistant = OpenAIAssistant(api_key=os.getenv("OPENAI_API_KEY"))  # Get the OpenAI API key from environment variables

@app.get("/health")
def health_check():
  """
  Health check endpoint to provide basic metrics.
  """
  metrics = {
    "status": "healthy",
    "uptime": os.popen('uptime').read().strip(),
    "disk_usage": os.popen('df -h /').read().strip(),
    "memory_usage": os.popen('free -h').read().strip()
  }
  return JSONResponse(content=metrics)

@app.get("/transcript/{video_id}")
async def get_transcript(video_id: str, summarize: bool = False, analyze: bool = False):
    """
    Fetch the transcript of a YouTube video and optionally summarize or analyze it.
    """
    file_name = f"{video_id}_transcript.txt"

    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Create a formatted transcript
        transcript_text = "\n".join(
            [f"{item['start']:.2f}s: {item['text']}" for item in transcript]
        )
        
        # Save transcript to a file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(transcript_text)

        # Optional: Summarize or analyze the transcript
        results = {}
        if summarize:
            results["summary"] = assistant.summarize_transcript(transcript_text)
        if analyze:
            results["analysis"] = assistant.analyze_transcript(transcript_text)

        # Return results along with the transcript file
        return JSONResponse(content={"transcript": transcript_text, "results": results})

    except CouldNotRetrieveTranscript:
        raise HTTPException(status_code=404, detail="Transcript not available for this video")
    except TranscriptsDisabled:
        raise HTTPException(status_code=403, detail="Transcripts are disabled for this video")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
    finally:
        # Clean up the file after serving
        if os.path.exists(file_name):
            os.remove(file_name)
 