import streamlit as st
import requests

st.title("📄 PDF & Code Review Agent")

tool = st.radio("Choose Tool", ["PDF", "Code"])

prompt = st.text_area("Enter your prompt", placeholder="e.g., Summarize the content or Review the code...")

file = None
code = None

if tool == "PDF":
    file = st.file_uploader("Upload a PDF file", type=["pdf"])
elif tool == "Code":
    code = st.text_area("Paste your code here")

if st.button("Run Agent"):
    if tool == "PDF" and file and prompt:
        with st.spinner("Processing PDF..."):
            response = requests.post(
                "http://localhost:8000/process/",
                files={"file": file},
                data={"tool": "pdf", "prompt": prompt}
            )
            st.success("Done!")
            st.text_area("Result", response.json()["result"], height=300)
    elif tool == "Code" and code and prompt:
        with st.spinner("Code analysis ..."):
            response = requests.post(
                "http://localhost:8000/process/",
                data={"tool": "code", "prompt": prompt, "code": code}
            )
            st.success("Done!")
            st.text_area("Result", response.json()["result"], height=300)
    else:
        st.warning("Please provide both the prompt and the necessary input.")
