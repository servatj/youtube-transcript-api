-- 
-- depends: 20241202_01_Ftdjq
CREATE TABLE analysis_results (
    id SERIAL PRIMARY KEY,           -- Unique ID for the analysis result
    transcript_id INT NOT NULL,      -- Foreign key referencing transcripts
    analysis JSONB NOT NULL,         -- Analysis result in JSON format
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    FOREIGN KEY (transcript_id) REFERENCES transcripts(id) ON DELETE CASCADE -- Link to transcripts
)
