from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import os
import shutil
import requests
import fitz  # PyMuPDF

router = APIRouter()
security = HTTPBearer()
UPLOAD_DIR = "backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, os.getenv("SECRET_KEY", "testsecret"), algorithms=["HS256"])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

def extract_text_from_pdf(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text

@router.post("/upload")
def upload_file(file: UploadFile = File(...), user=Depends(verify_token)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = extract_text_from_pdf(file_path)

    response = requests.post(WEBHOOK_URL, json={
        "filename": file.filename,
        "text": text
    })

    return {
        "message": "Uploaded and sent to n8n",
        "n8n_response": response.json()
    }
