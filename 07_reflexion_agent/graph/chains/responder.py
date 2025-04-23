from config import cfg
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field


## define llm
llm = cfg.llm

## Create Chain
class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing.")
    superfluous: str = Field(description="Critique of what is superfluous")


class AnswerQuestion(BaseModel):
    """Answer the question."""

    answer: str = Field(description="~250 word detailed answer to the question.")
    reflection: Reflection = Field(description="Your reflection on the initial answer.")
    search_queries: List[str] = Field(description="1-3 search queries for researching improvements to address the critique of your current answer.")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert researcher.

            Response must contains below keys 
            1. answer : 250 word detailed answer to the question.
            1. reflection : Reflect and critique your answer. Be severe to maximize improvement.
            2. search_queries : Recommend search queries for question to improve your answer.""",
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

responder_chain = prompt | llm.bind_tools(tools=[AnswerQuestion], tool_choice='AnswerQuestion')



