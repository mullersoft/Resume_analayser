CREATE TABLE IF NOT EXISTS resumes (
    id SERIAL PRIMARY KEY,
    filename TEXT,
    full_name TEXT,
    email TEXT,
    phone TEXT,
    skills TEXT[],
    experience_years FLOAT,
    last_job_title TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
