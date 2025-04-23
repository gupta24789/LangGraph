import operator
from typing import Annotated, Sequence, List, TypedDict
from langchain_core.messages import BaseMessage


class State(TypedDict):
    """
    Used to create the state. This will be used for agent communication.
    """
    messages : Annotated[List[Sequence[BaseMessage]], operator.add]
    sender: str