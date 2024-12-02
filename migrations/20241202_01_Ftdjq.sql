-- 
-- depends: 
CREATE TABLE transcripts (
    id SERIAL PRIMARY KEY,          -- Unique ID for the transcript
    video_id VARCHAR(255) NOT NULL, -- YouTube video ID
    transcript TEXT NOT NULL,       -- Transcript text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of creation
)