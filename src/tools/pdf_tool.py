from langchain.tools import Tool
from PyPDF2 import PdfReader

def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text[:3000]  # limit content if needed

pdf_tool = Tool.from_function(
    name="PDFReaderTool",
    func=read_pdf,
    description="Reads and returns content from a PDF file"
)
