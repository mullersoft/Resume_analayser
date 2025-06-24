# Resume Analyzer – FastAPI + n8n + PostgreSQL

This is a resume analysis system that extracts structured information (name, email, skills, etc.) from PDF resumes. It uses:

- 🐍 **FastAPI** (backend upload and text extraction)
- 🔗 **n8n** (workflow orchestration)
- 🧠 **OpenAI GPT-3.5 Turbo** (resume parsing)
- 🐘 **PostgreSQL** (data storage)
- 🐳 **Docker Compose** (to run all services)

---

## 🚀 Features

- Upload PDF resumes via FastAPI
- Extracts resume text using `PyMuPDF`
- Sends extracted text to `n8n` webhook
- Uses OpenAI to parse structured fields
- Stores results into `resumes` table in PostgreSQL

How to Run:
docker-compose up --build

To view in the DB:docker exec -it resume-analyzer-postgres-1 psql -U admin -d resumes
tables:SELECT \* FROM resumes;
