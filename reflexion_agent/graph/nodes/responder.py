from graph.state import State
from graph.chains.responder import responder_chain


def responder_node(state : State):
    res =  responder_chain.invoke({"messages": state['messages']})
    return {"messages": res}







