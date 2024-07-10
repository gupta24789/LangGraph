from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from enum import Enum
from typing import Union, Annotated, List, Any
from langchain.pydantic_v1 import BaseModel, Field
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser

## Create Agent
def create_agent(llm , tools : list, prompt_template : ChatPromptTemplate) -> AgentExecutor:
    """
    create agent
    """
    agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt_template)
    agent_executor = AgentExecutor(agent = agent, tools=tools, handle_parsing_errors=True)
    return agent_executor

        
def agent_node(state, agent, name):
    """
    First Argument must be state otherwise you will get error
    """
    result = agent.invoke(state)
    return {
        "messages": [HumanMessage(content=result["output"], name=name)],
        "sender": name
        }