from langchain.chat_models import ChatOpenAI
from langchain.callbacks import *
from langchain.prompts import *
from langchain.chains import *
from langchain.memory import *
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

API_KEY="sk-IC2OJ7DsSiY0EziklaNNWlodCHwNEHd0Mr6O3Yx1l3Hsp70p"
API_BASE="https://api.closeai-proxy.xyz/v1"

def Create_ChatModel():
    chat_model = ChatOpenAI()
    chat_model.openai_api_key = API_KEY
    chat_model.openai_api_base = API_BASE
    chat_model.model_name = "gpt-3.5-turbo"
    chat_model.temperature = 0.0
    return chat_model
