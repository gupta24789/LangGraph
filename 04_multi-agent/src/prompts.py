from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_agent_prompt_template(prompt : str):
    prompt_template = ChatPromptTemplate.from_messages([
        ('system',prompt),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad')
    ])

    return prompt_template


## Researcher
researcher_pmt = """
You are a helpful AI assistant, collaborating with other assistants.
Use the provided tools to progress towards answering the question.
If you are unable to fully answer, that's OK, another assistant with different tools
will help where you left off. Execute what you can to make progress.
If you or any of the other assistants have the final answer or deliverable,
prefix your response with FINAL ANSWER so the team knows to stop.

You should provide accurate data for the chart_generator to use.
"""
researcher_template = get_agent_prompt_template(researcher_pmt)


## ChartGenerator
chart_gen_pmt = """
You are a helpful AI assistant, collaborating with other assistants.
Use the provided tools to progress towards answering the question.
If you are unable to fully answer, that's OK, another assistant with different tools
will help where you left off. Execute what you can to make progress.
If you or any of the other assistants have the final answer or deliverable,
prefix your response with FINAL ANSWER so the team knows to stop.

Any charts you display will be visible by the user.
"""

chart_gen_template = get_agent_prompt_template(chart_gen_pmt)