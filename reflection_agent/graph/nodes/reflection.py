from graph.chains.reflect import reflect_chain
from graph.state import State
from langchain_core.messages import HumanMessage


def reflect_node(state : State):
    messages = state['messages']
    res = reflect_chain.invoke({"messages": messages})
    return {
        "messages": HumanMessage(content= res.content)
    }








