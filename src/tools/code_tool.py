from langchain.tools import Tool

def review_code(code: str) -> str:

    review_template = f"""
                CODE REVIEW ANALYSIS

                CODE TO REVIEW:
                {code}

                ANALYSIS FRAMEWORK:
                Please provide a comprehensive review covering:

                1. CODE QUALITY & STYLE:
                - Readability and maintainability
                - Naming conventions
                - Code organization and structure
                - Documentation and comments

                2. FUNCTIONALITY & LOGIC:
                - Correctness of implementation
                - Edge cases handling
                - Error handling and validation
                - Algorithm efficiency

                3. SECURITY CONSIDERATIONS:
                - Input validation
                - Potential vulnerabilities
                - Data handling security

                4. PERFORMANCE:
                - Time complexity
                - Space complexity
                - Optimization opportunities

                5. BEST PRACTICES:
                - Language-specific conventions
                - Design patterns usage
                - Code reusability

                6. RECOMMENDATIONS:
                - Specific improvements
                - Refactoring suggestions
                - Additional features or considerations

                Please provide specific, actionable feedback with examples where applicable.
                """
    
    return review_template

code_tool = Tool.from_function(
    name="CodeReviewTool",
    func=review_code,
    description="""
    Comprehensive code review tool that analyzes source code for quality, security, performance, and best practices.
    
    This tool accepts source code as input and provides detailed analysis including:
    - Code quality assessment and style recommendations
    - Bug detection and logic validation
    - Security vulnerability identification
    - Performance optimization suggestions
    - Best practices compliance
    - Specific improvement recommendations
    
    Use this tool when you need to review, analyze, or get feedback on any piece of source code.
    """
)

def generate_code(prompt: str) -> str:
    review_template = f"""
                create this code in a way that it is easy to read, maintain, and follow best practices.
                {prompt}
                Please provide specific, actionable feedback with examples where applicable.
                """
    
    return review_template

code_tool = Tool.from_function(
    name="CodeCreationTool",
    func=generate_code,
    description="""
    Comprehensive code creation tool that generates source code based on user prompts.
    This tool accepts a prompt as input and provides a well-structured code snippet as output.
    """
)
