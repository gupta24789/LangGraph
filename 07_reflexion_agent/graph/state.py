from typing import List, TypedDict, Annotated, Sequence
from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage


class State(TypedDict):
    messages :Annotated[Sequence[BaseMessage], add_messages]