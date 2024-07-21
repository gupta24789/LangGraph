from graph.state import State
from langgraph.graph import StateGraph, START, END

from langchain_core.messages import ToolMessage
from graph.constant import RESPONDER, REVISOR, EXECUTE_TOOLS
from graph.nodes.responder import responder_node
from graph.nodes.revisor import revisor_node
from graph.nodes.execute_tools import execute_tools_node


def event_loop(state) -> str:
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in state['messages'])
    num_iterations = count_tool_visits
    print(f"num_iterations : {num_iterations}")

    if num_iterations > MAX_ITERATIONS:
        return END
    return EXECUTE_TOOLS


MAX_ITERATIONS = 2
builder = StateGraph(State)
builder.add_node(RESPONDER, responder_node)
builder.add_node(EXECUTE_TOOLS, execute_tools_node)
builder.add_node(REVISOR, revisor_node)

builder.add_edge(RESPONDER, EXECUTE_TOOLS)
builder.add_edge(EXECUTE_TOOLS, REVISOR)
builder.add_conditional_edges(REVISOR, 
                              event_loop,
                              {
                                  END : END,
                                  EXECUTE_TOOLS : EXECUTE_TOOLS
                              }
                              )
builder.set_entry_point(RESPONDER)
app = builder.compile()

app.get_graph().draw_mermaid_png(output_file_path= "graph.png")




