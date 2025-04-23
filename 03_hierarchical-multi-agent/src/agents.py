from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

# def create_agent(name: str, llm , tools: list, prompt: ChatPromptTemplate):

#     agent = create_openai_functions_agent(llm, tools=tools, prompt=prompt)
#     agent_executor = AgentExecutor(agent=agent, tools=tools)

#     def create_node(state):
#         result = agent_executor.invoke(state)
#         return {
#             'messages': [HumanMessage(content=result["output"], name=name)]
#         }

#     return create_node

def create_agent(llm , tools: list, prompt: ChatPromptTemplate):

    agent = create_openai_functions_agent(llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    return agent_executor


def agent_node(state, agent, name):
    "state must be first argument"
    result = agent.invoke(state)
    return {
        'messages': [HumanMessage(content=result["output"], name=name)]
    }

def create_supervisor_chain(llm , prompt: ChatPromptTemplate, functions, function_call):
    
    chain = (prompt
        | llm.bind_functions(functions=functions, function_call=function_call)
        | JsonOutputFunctionsParser())
    
    return chain




