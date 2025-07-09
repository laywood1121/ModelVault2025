from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()
LOG_FILE = "logs"

class PromptRequest(BaseModel):
    prompt: str

class ResponseModel(BaseModel):
    response: str

def log_interaction(prompt: str, response: str):
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

@app.post("/generate", response_model=ResponseModel)
async def generate_response(request: PromptRequest):
    prompt = request.prompt
    response_text = f"You said: {prompt}"  # Stubbed response
    log_interaction(prompt, response_text)
    return {"response": response_text}
