import os
import yaml
from langchain_openai import ChatOpenAI

# Load the config
config = yaml.safe_load(open("config.yaml"))


# Get the openai config
openai_config = config['GENAI_CREDS']

## Set the env variable
os.environ["OPENAI_API_KEY"] = openai_config['OPENAI_API_KEY']
os.environ["TAVILY_API_KEY"] = openai_config['TAVILY_API_KEY']
os.environ['LANGCHAIN_TRACING_V2'] = openai_config['LANGCHAIN_TRACING_V2']
os.environ['LANGCHAIN_PROJECT'] = openai_config['LANGCHAIN_PROJECT']
os.environ['LANGCHAIN_API_KEY'] = openai_config['LANGCHAIN_API_KEY']

class Config:

    # Intialize the model
    llm = ChatOpenAI(
            openai_api_key = openai_config['OPENAI_API_KEY'],
            model = openai_config['OPENAI_MODEL_NAME'],
            temperature = 0,
            max_retries = 5,
            model_kwargs = {"seed" : 121}
        )



cfg = Config()


