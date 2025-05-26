from langchain.tools import Tool

def review_code(code: str) -> str:
    # Placeholder logic, actual logic handled by agent
    return code

code_tool = Tool.from_function(
    name="CodeReviewTool",
    func=review_code,
    description="Receives code and passes it to LLM for review"
)
