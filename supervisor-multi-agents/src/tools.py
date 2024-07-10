from langchain.tools import tool
from typing import Annotated
from langchain_experimental.utilities import PythonREPL
from langchain_community.tools.tavily_search import TavilySearchResults

tavily_tool = TavilySearchResults(max_results=5)
python_repl = PythonREPL()

@tool
def python_repl_tool(code : Annotated[str, "Python code"]):
    """
    Use this tool to execute the python code.
    Use the print(...) to print the result.
    """

    result = python_repl.run(code)
    
    if "Error" in result:
        return f"Failed to execute. Error : {result}"
    
    result_str = f"Code Executed Successfully : \n\nCode : \n```python\n{code}\n``` \nStdout : {result}"
    completed_msg = f"\n\nIf you have completed all tasks, respond with FINAL ANSWER."
    return result_str +  completed_msg