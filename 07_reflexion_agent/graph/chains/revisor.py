from config import cfg
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from graph.chains.responder import AnswerQuestion

## define llm
llm = cfg.llm

# Define Chain
class ReviseAnswer(AnswerQuestion):
    """Revise your original answer to your question."""
    references: List[str] = Field(description="Citations motivating your updated answer.")


instruction = """Revise your previous answer using the new information.
    - You should use the previous critique to add important information to your answer.
        - You MUST include numerical citations in your revised answer to ensure it can be verified.
        - Add a "References" section to the bottom of your answer (which does not count towards the word limit). In form of:
            - [1] https://example.com
            - [2] https://example.com
    - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert researcher.

            {instruction} 

            Response must contains below keys 
            1. answer : Revised answr based on new info
            1. reflection : Reflect and critique your answer. Be severe to maximize improvement.
            2. search_queries : Recommend search queries for question to improve your answer.""",
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
).partial(instruction = instruction)


revisor_chain = prompt | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")
