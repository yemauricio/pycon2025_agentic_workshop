## Project Structure

- **agentic/**
  - **src/**
    - **agent/**
      - `base_agent.py`
      - `pdf_tool.py`
      - `code_tool.py`
    - **service/**
      - `handler.py`
      - `gemini_llm.py`
  - **api/**
    - `main.py` ← FastAPI backend
  - **frontend/**
    - `app.py` ← Streamlit frontend
  - `requirements.txt`
  - `README.md`
  - env.env: gemini_api_key refer to link https://ai.google.dev/gemini-api/docs/api-keylink 

## RUNNING INSTRUCTIONS
### **Start FastAPI backend**
cd api
uvicorn main:app --reload

### Start Streamlit frontend
cd frontend
streamlit run app.py
