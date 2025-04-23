from enum import Enum
from typing import Union, Any, Annotated
from langchain.pydantic_v1 import BaseModel, Field
from langchain.utils.openai_functions import convert_pydantic_to_openai_function

# Supervisor
class Member(Enum):
    Researcher : str = 'Researcher'
    Coder : str = 'Coder'

class Route(BaseModel):
        """
        Select the next role.
        """
        next : Union[Member, Any] = Field(title='next', description="next role")

members = [member.name for member in Member]   
options = ['FINISH'] +  members
functions = [convert_pydantic_to_openai_function(Route)]
function_call = "Route"





