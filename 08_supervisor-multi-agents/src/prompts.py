from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_agent_prompt_template(prompt : str):
    prompt_template = ChatPromptTemplate.from_messages([
        ('system',prompt),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad')
    ])

    return prompt_template


def get_supervisor_prompt_template(before_prompt, after_prompt):

    supervisor_template = ChatPromptTemplate.from_messages([
                            ('system',before_prompt),
                            MessagesPlaceholder(variable_name='messages'),
                            ('system', after_prompt)
                         ])
    
    return supervisor_template


# Supervisor
before_pmt = """
You are a supervisor tasked with managing a conversation between the 
following workers:  {members}. Given the following user request
respond with the worker to act next. Each worker will perform a
task and respond with their results and status. 
When finished, respond with FINISH.
"""
after_pmt = """
Given the conversation above, who should act next?
Or should we FINISH? Select one of: {options}
"""

supervisor_template = get_supervisor_prompt_template(before_pmt, after_pmt)


## Researcher
researcher_pmt = """
You are a web researcher.
"""
researcher_template = get_agent_prompt_template(researcher_pmt)


## Coder
coder_pmt = """
You are a coder. Your task is to generate amd test the code for user request.
"""

coder_template = get_agent_prompt_template(coder_pmt)





