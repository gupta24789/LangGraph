from graph.state import AgentState
from graph.chains import agent_reason


def run_agent_reasoning_node(state: AgentState):
    agent_outcome = agent_reason.react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}






