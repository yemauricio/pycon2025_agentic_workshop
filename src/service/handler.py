from src.agent.pdf_tool import pdf_tool
from src.agent.code_tool import code_tool

def get_tools(tool_type: str):
    if tool_type == "pdf":
        return [pdf_tool]
    elif tool_type == "code":
        return [code_tool]
    else:
        raise ValueError("Invalid tool type.")
