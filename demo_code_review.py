import sys
import os
sys.path.append(os.path.abspath('.'))

from src.agent.gemini_llm import get_agent

def run_code_review_demo():
    """Run the code review demo with various code examples."""
    # Get the code review agent
    try:
        agent = get_agent("code")
        print("Code review agent initialized successfully!")
        print()
    except Exception as e:
        print(f"Error initializing agent: {e}")
        print("Make sure you have set up your GEMINI_API_KEY in .env file")
        return
    
    example1 = """
                def calculate_average(numbers):
                    sum = 0
                    for i in range(len(numbers)):
                        sum += numbers[i]
                    return sum / len(numbers)
                """

    # Example 3: Python class with good practices
    example2 = """
                from typing import List, Optional
                import logging

                class BankAccount:
                    def __init__(self, account_number: str, initial_balance: float = 0.0):
                        self._account_number = account_number
                        self._balance = max(0.0, initial_balance)
                        self._transaction_history: List[str] = []
                        self._logger = logging.getLogger(__name__)
                    
                    def deposit(self, amount: float) -> bool:
                        if amount <= 0:
                            self._logger.warning(f"Invalid deposit amount: {amount}")
                            return False
                        
                        self._balance += amount
                        self._transaction_history.append(f"Deposit: +${amount:.2f}")
                        self._logger.info(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
                        return True
                    
                    def withdraw(self, amount: float) -> bool:
                        if amount <= 0:
                            self._logger.warning(f"Invalid withdrawal amount: {amount}")
                            return False
                        
                        if amount > self._balance:
                            self._logger.warning("Insufficient funds")
                            return False
                        
                        self._balance -= amount
                        self._transaction_history.append(f"Withdrawal: -${amount:.2f}")
                        self._logger.info(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
                        return True
                    
                    @property
                    def balance(self) -> float:
                        return self._balance
                    
                    def get_transaction_history(self) -> List[str]:
                        return self._transaction_history.copy()
                """
    
    examples = [
        ("Simple Python Function (with issues)", example1),
        ("Python Class (good practices)", example2)
    ]
    
    for i, (title, code) in enumerate(examples, 1):

        try:
            print("🤖 Agent Analysis:")
            result = agent.run(f"Please review this code and provide detailed feedback:\n{code}")
            print(result)
            print()
            print("=" * 80)
            print()
        except Exception as e:
            print(f"❌ Error during review: {e}")
            print()
    
    print("🎉 Demo completed!")
    print()
    print("💡 To test the web interface:")
    print("1. Start the API server: uvicorn api.main:app --reload")
    print("2. Start the frontend: streamlit run frontend/app.py")
    print("3. Open your browser and go to the Streamlit URL")
    print("4. Select 'Code' tool and paste any code for review")


if __name__ == "__main__":
    print("Starting Code Review Agent Demo...")
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--examples":
        show_usage_examples()
    else:
        run_code_review_demo()
