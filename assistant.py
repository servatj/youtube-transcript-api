import openai

class OpenAIAssistant:
    def __init__(self, api_key: str):
        """
        Initialize the OpenAI Assistant with the given API key.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def summarize_transcript(self, transcript: str) -> str:
        """
        Summarize the given transcript using OpenAI GPT models.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are an assistant that summarizes transcripts."},
                    {"role": "user", "content": f"Summarize this transcript: {transcript}"}
                ],
                max_tokens=500,
                temperature=0.7,
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            raise RuntimeError(f"Failed to summarize transcript: {str(e)}")

    def analyze_transcript(self, transcript: str) -> dict:
        """
        Perform a custom analysis of the transcript, such as extracting key topics.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are an assistant that analyzes transcripts."},
                    {"role": "user", "content": f"Analyze this transcript and extract key topics: {transcript}"}
                ],
                max_tokens=500,
                temperature=0.7,
            )
            return {"analysis": response['choices'][0]['message']['content'].strip()}
        except Exception as e:
            raise RuntimeError(f"Failed to analyze transcript: {str(e)}")