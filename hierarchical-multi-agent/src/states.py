import operator
from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage

class ResearchTeamState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    team_members: List[str]
    next : str


class DocWritingState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    team_members: str
    next: str
    current_files: str


class SupervisorState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    next: str