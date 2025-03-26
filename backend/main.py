from fastapi import FastAPI
from processor import process_email
import json

app = FastAPI()

# Load mock emails
with open("data/sample_emails.json") as f:
    mock_emails = json.load(f)

@app.get("/process-emails")
def process_mock_emails():
    results = [process_email(email) for email in mock_emails]
    return {"processed_requests": results}