from langgraph.graph import StateGraph, START, END
from graph.state import State
from graph.constant import REFLECT, GENERATE
from graph.nodes.generate import generation_node
from graph.nodes.reflection import reflect_node
from graph.state import State

def should_continue(state: State):
    messages = state['messages']

    if len(messages) > 6:
        return END
    return REFLECT



workflow = StateGraph(State)
workflow.add_node(REFLECT, reflect_node)
workflow.add_node(GENERATE, generation_node)
workflow.set_entry_point(GENERATE)
workflow.add_conditional_edges(GENERATE, should_continue)
workflow.add_edge(REFLECT, GENERATE)
app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path= "graph.png")




