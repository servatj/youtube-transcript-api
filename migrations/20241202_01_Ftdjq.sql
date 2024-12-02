-- 
-- depends: 
        CREATE TABLE analyses (
            id SERIAL PRIMARY KEY,
            video_id VARCHAR(255) NOT NULL,
            transcript TEXT NOT NULL,
            analysis JSONB NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
