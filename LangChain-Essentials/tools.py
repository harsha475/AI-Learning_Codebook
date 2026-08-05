from langchain_core.tools import tool
from datetime import datetime

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def today() -> str:
    """Returns today's date."""
    return str(datetime.now().date())

print(add.invoke({"a": 15, "b": 5}))
print(today.invoke({}))