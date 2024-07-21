from config import cfg
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain import hub
from langchain.agents import create_react_agent
from graph.tools import websearch, triplet_number



## define llm
llm = cfg.llm

## Create Chain
react_prompt: PromptTemplate = hub.pull("hwchase17/react")
# Define tools
tools = [websearch.tavily_tool, triplet_number.triple]


## Define chain
react_agent_runnable = create_react_agent(llm, tools, react_prompt)
