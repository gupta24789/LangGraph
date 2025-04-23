from langgraph.prebuilt.tool_executor import ToolExecutor
from graph.state import AgentState
from graph.tools import websearch, triplet_number

tool_executor = ToolExecutor([websearch.tavily_tool, triplet_number.triple])

def execute_tools_node(state: AgentState):
    agent_action = state["agent_outcome"]
    output = tool_executor.invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}

    

