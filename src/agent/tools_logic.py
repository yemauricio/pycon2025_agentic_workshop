from src.tools.pdf_tool import pdf_tool
from src.tools.code_tool import code_tool, generate_code

def get_tools(tool_type: str):
    if tool_type == "pdf":
        return [pdf_tool]
    elif tool_type == "code":
        return [code_tool, generate_code]
    else:
        raise ValueError("Invalid tool type.")
