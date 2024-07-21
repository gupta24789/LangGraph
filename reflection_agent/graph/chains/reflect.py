from config import cfg
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

## define llm
llm = cfg.llm

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


reflect_chain = reflection_prompt | llm