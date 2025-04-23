from graph.chains.generate import generate_chain
from graph.state import State


def generation_node(state : State):
    messages = state['messages']
    res =  generate_chain.invoke({"messages": messages})

    return {"messages": res}







