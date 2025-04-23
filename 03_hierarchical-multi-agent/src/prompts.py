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
following teams: {team_members}. Given the following user request,
respond with the worker to act next. Each worker will perform a
task and respond with their results and status. 
When finished,respond with FINISH.
"""
after_pmt = """
Given the conversation above, who should act next?
Or should we FINISH? Select one of: {options}"
"""
supervisor_template = get_supervisor_prompt_template(before_pmt, after_pmt)




# Research Team Supervisor
before_pmt = """
You are a supervisor tasked with managing a conversation between the
following workers:  {research_team_members}. Given the following user request
respond with the worker to act next. Each worker will perform a
task and respond with their results and status. 
When finished, respond with FINISH.
"""
after_pmt = """
Given the conversation above, who should act next?
Or should we FINISH? Select one of: {options}",
"""
research_team_supervisor_template = get_supervisor_prompt_template(before_pmt, after_pmt)

# Search
search_pmt = """
You are a research assistant who can search for up-to-date info using the tavily search engine.
"""
searcher_template = get_agent_prompt_template(search_pmt)

# Scrapper
scrapper_pmt = """
You are a research assistant who can scrape specified urls for more detailed information using the scrape_webpages function
"""
scrapper_template = get_agent_prompt_template(scrapper_pmt)



# Doc Writer
before_pmt = """
You are a supervisor tasked with managing a conversation between the
following workers:  {doc_writer_members}. Given the following user request,
respond with the worker to act next. Each worker will perform a
task and respond with their results and status. 
When finished,respond with FINISH.
"""
after_pmt = """
Given the conversation above, who should act next?
Or should we FINISH? Select one of: {options}",
"""
doc_writing_team_supervisor_template = get_supervisor_prompt_template(before_pmt, after_pmt)



# Writer
writer_pmt = """
You are an expert writing a research document.
Below are files currently in your directory:\n{current_files}
"""
writer_template = get_agent_prompt_template(writer_pmt)


# Note Taker
note_taker_pmt = """
You are an expert senior researcher tasked with writing a paper outline and
taking notes to craft a perfect paper.{current_files}
"""
note_taker_template = get_agent_prompt_template(note_taker_pmt)


# Chart Generator
chart_gen_pmt = """
You are a data viz expert tasked with generating charts for a research project.
{current_files}
"""
chart_gen_template = get_agent_prompt_template(chart_gen_pmt)







