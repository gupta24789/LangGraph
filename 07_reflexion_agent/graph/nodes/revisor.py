from graph.state import State
from langchain_core.messages import HumanMessage
from graph.chains.revisor import revisor_chain

def revisor_node(state : State):

    res = revisor_chain.invoke(state)
    
    return {
        "messages": res
    }








