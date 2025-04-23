from enum import Enum
from typing import Union, Any, Annotated
from langchain.pydantic_v1 import BaseModel, Field
from langchain.utils.openai_functions import convert_pydantic_to_openai_function

# Supervisor
class SupervisorMember(Enum):
    ResearchTeam : str = "ResearchTeam"
    PaperWritingTeam : str = "PaperWritingTeam"

class SupervisorRoute(BaseModel):
    next : Union[SupervisorMember, Any] = Field(title = 'next', description = 'next role')

supervisor_members = [member.name for member in SupervisorMember]   
supervisor_options = ['FINISH'] +  supervisor_members
supervisor_functions = [convert_pydantic_to_openai_function(SupervisorRoute)]
supervisor_function_call = "SupervisorRoute"

# Research team
class ResearchTeamMember(Enum):
    """team members"""
    Search : str = "Search"
    WebScraper : str = "WebScraper"

class ResearchTeamRoute(BaseModel):
    """Next role"""
    next : Union[ResearchTeamMember, Any] = Field(title = "Next", description = "next role from research team")


research_team_members = [member.name for member in ResearchTeamMember]   
research_team_options = ['FINISH'] +  research_team_members
research_team_functions = [convert_pydantic_to_openai_function(ResearchTeamRoute)]
research_team_function_call = "ResearchTeamRoute"


# Doc Writing Member
class DocWritingTeamMember(Enum):
    DocWriter :  str = "DocWriter"
    NoteTaker :  str = "NoteTaker"
    ChartGenerator : str = "ChartGenerator"

class DocWritingTeamRoute(BaseModel):
    """Next role"""
    next : Annotated[Union[DocWritingTeamMember, Any], "next role"] = Field(title = "Next", 
                                                             description = "next role from doc writing team")
    
doc_writing_members = [member.name for member in DocWritingTeamMember]
doc_writing_options = ['FINISH'] +  doc_writing_members
doc_writing_functions = [convert_pydantic_to_openai_function(DocWritingTeamRoute)]
doc_writing_function_call = "DocWritingTeamRoute"



