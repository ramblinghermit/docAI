from fastapi import APIRouter
import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv


router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

# Additional routes can be added here as needed.



# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Pydantic Models (Data Validation) ---
class CommandRequest(BaseModel):
    prompt: str
    app_context: str  # e.g., "Sheet", "Doc", "Invoice"

class UniverCommand(BaseModel):
    app: str
    commandId: str
    params: dict

# --- Gemini Configuration ---
try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Error configuring Gemini: {e}")

# --- Univer Command Schemas ---
SCHEMA_SHEET = {
    "type": "OBJECT",
    "properties": {
        "app": {"type": "STRING", "description": "The app context, e.g., 'Sheet'"},
        "commandId": {"type": "STRING", "description": "The Univer mutation ID"},
        "params": {"type": "OBJECT", "description": "The parameters for the mutation"}
    },
    "required": ["app", "commandId"]
}

APP_SCHEMAS = {
    "Sheet": SCHEMA_SHEET,
}


# --- Helper Function: AI Translator ---
async def get_ai_command(request: CommandRequest) -> UniverCommand:
    schema = APP_SCHEMAS.get(request.app_context)
    if not schema:
        raise HTTPException(status_code=400, detail="Invalid app_context")

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": schema
        },
        system_instruction=f"You are an AI assistant for Univer. The user is in the '{request.app_context}' app. Translate the prompt into a single, valid JSON command matching the schema."
    )
    
    try:
        response = await model.generate_content_async(request.prompt)
        return UniverCommand.model_validate(response.candidates[0].content.parts[0].json)
    except Exception as e:
        print(f"Error during Gemini call: {e}")
        raise HTTPException(status_code=500, detail=f"AI processing error: {e}")

# --- API Endpoint ---
@router.post("/api/v1/process-command", response_model=UniverCommand)
async def process_command(request: CommandRequest):
    print(f"Received request for {request.app_context}: {request.prompt}")
    ai_command = await get_ai_command(request)
    print(f"Returning command: {ai_command.model_dump_json()}")
    return ai_command

@router.get("/")
def read_root():
    return {"status": "AI Spreadsheet Backend is running!"}