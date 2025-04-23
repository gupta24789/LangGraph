from graph.state import AgentState, AgentFinish
from graph.constant import ACT, AGENT_REASON
from graph.nodes import agent_reason, execute_tools
from langgraph.graph import StateGraph, START, END



def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT


flow = StateGraph(AgentState)

flow.add_node(AGENT_REASON, agent_reason.run_agent_reasoning_node)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, execute_tools.execute_tools_node)


flow.add_conditional_edges(
    AGENT_REASON,
    should_continue,
)

flow.add_edge(ACT, AGENT_REASON)
app = flow.compile()

app.get_graph().draw_mermaid_png(output_file_path= "graph.png")




