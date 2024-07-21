import json
from graph.tools.websearch import tavily_tool
from graph.state import State
from langchain_core.messages import ToolMessage, AIMessage, BaseMessage
from langchain_core.output_parsers import PydanticToolsParser, JsonOutputToolsParser
from langgraph.prebuilt import ToolInvocation, ToolExecutor
from typing import List
from collections import defaultdict


parser = JsonOutputToolsParser(return_id=True)
tool_executor = ToolExecutor([tavily_tool])

def execute_tools_node(state: List[BaseMessage]) -> List[ToolMessage]:
    tool_invocation: AIMessage = state['messages'][-1]
    parsed_tool_calls = parser.invoke(tool_invocation)
    ids = []
    tool_invocations = []
    
    for parsed_call in parsed_tool_calls:
        for query in parsed_call["args"]["search_queries"]:
            tool_invocations.append(
                ToolInvocation(
                    tool="tavily_search_results_json",
                    tool_input=query,
                )
            )
            ids.append(parsed_call["id"])

    outputs = tool_executor.batch(tool_invocations)

    # Map each output to its corresponding ID and tool input
    outputs_map = defaultdict(dict)
    for id_, output, invocation in zip(ids, outputs, tool_invocations):
        outputs_map[id_][invocation.tool_input] = output

    # Convert the mapped outputs to ToolMessage objects
    tool_messages = []
    for id_, mapped_output in outputs_map.items():
        tool_messages.append(
            ToolMessage(content=json.dumps(mapped_output), tool_call_id=id_)
        )

    return {"messages" : tool_messages}
    

