import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from src.agent.gemini_llm import get_agent
import tempfile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process/")
async def process(tool: str = Form(...), prompt: str = Form(...), file: UploadFile = None, code: str = Form(None)):
    agent = get_agent(tool)
    
    if tool == "pdf":
        if file is None:
            return {"error": "No file uploaded"}
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp.flush()
            result = agent.run(f"{prompt}:\nFilePath: {tmp.name}")
    elif tool == "code":
        if not code:
            return {"error": "No code provided"}
        result = agent.run(f"{prompt}:\n{code}")
    else:
        return {"error": "Invalid tool"}
    
    return {"result": result}
