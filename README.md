# YouTube Transcript API

A FastAPI-based project for fetching YouTube video transcripts and processing them with OpenAI's GPT models for summarization and analysis.

---

## Features

- Fetch YouTube video transcripts using the `youtube-transcript-api`.
- Summarize and analyze transcripts using OpenAI's GPT models.
- Expose APIs for transcript retrieval and optional processing.

---

## Requirements

- Python 3.12+
- pip (Python package manager)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/youtube-transcript-api.git
cd youtube-transcript-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Linux/Mac
.\venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

---

## Run the Application

### 0. Prepare the Infrastructure

Ensure you have Docker and Docker Compose installed on your machine. Then, run the following command to set up the necessary infrastructure:

```bash
docker-compose up -d
```

This will start the required services defined in your `docker-compose.yml` file.

#### Apply Database Migrations

Run the following command to apply database migrations using `yoyo-migrations`:

```bash
yoyo apply
```

Replace `username`, `password`, and `youtube_transcripts` with your actual database credentials.

### 1. Start the Server

Run the FastAPI application using Uvicorn:

```bash
uvicorn app.__init__:app --reload
```

### 2. Access the API

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Usage

### Endpoints

1. **Fetch Transcript**

   ```
   GET /transcript/{video_id}
   ```

   - **Parameters**:
     - `video_id` (str): The YouTube video ID.
   - **Response**:
     ```json
     {
       "video_id": "example_id",
       "transcript": "Transcript content..."
     }
     ```

2. **Fetch and Summarize Transcript**
   ```
   GET /transcript/{video_id}?summarize=true
   ```
   - **Query Parameter**:
     - `summarize` (bool): Set to `true` to include a summary.
   - **Response**:
     ```json
     {
       "video_id": "example_id",
       "transcript": "Transcript content...",
       "summary": "Summarized content..."
     }
     ```

you can find more endpoint in the docs using swagger as explained later in this readme.
---

## Development

### Project Structure

```
youtube-transcript-api/
│
├── app/
│   ├── __init__.py            # FastAPI app entry point
│   ├── api/                   # API routes
│   │   ├── endpoints/
│   │   │   ├── transcript.py  # Transcript-related endpoints
│   ├── core/                  # Core configurations
│   │   ├── config.py          # Config file for environment variables
│   ├── services/              # Business logic
│   │   ├── openai_service.py  # Integration with OpenAI API
│   │   ├── transcript_service.py  # Logic for transcript fetching
│   ├── utils/                 # Utility functions
│
├── tests/                     # Tests for your application
├── .env                       # Environment variables
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
```

### Run Tests

```bash
pytest
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

---

## Author

**Josep Servat**  
For any queries, contact at DM on x @servatj or linkedin https://www.linkedin.com/in/servatj/.
