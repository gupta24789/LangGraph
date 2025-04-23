import os
import yaml
from langchain_openai import ChatOpenAI

config = yaml.safe_load(open("config.yaml"))
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']
os.environ['TAVILY_API_KEY'] = config['TAVILY_API_KEY']

os.environ['LANGCHAIN_TRACING_V2'] = config['LANGCHAIN_TRACING_V2']
os.environ['LANGCHAIN_ENDPOINT'] = config['LANGCHAIN_ENDPOINT']
os.environ['LANGCHAIN_PROJECT'] = config['LANGCHAIN_PROJECT']
os.environ['LANGCHAIN_API_KEY'] = config['LANGCHAIN_API_KEY']



## Define llm model
class Config:

    llm = ChatOpenAI(model = config['OPENAI_MODEL_NAME'])


cfg = Config()