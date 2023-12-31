from langchain.chat_models import ChatOpenAI
from langchain.callbacks import *
from langchain.prompts import *
from langchain.chains import *
from langchain.memory import *
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

API_KEY="KEY"
API_BASE="BASE"

def Create_ChatModel():
    chat_model = ChatOpenAI()
    chat_model.openai_api_key = API_KEY
    chat_model.openai_api_base = API_BASE
    chat_model.model_name = "gpt-3.5-turbo"
    chat_model.temperature = 0.0
    return chat_model


def CreateConversation(memory):
    chat_model = ChatOpenAI()
    chat_model.openai_api_key = API_KEY
    chat_model.openai_api_base = API_BASE
    chat_model.model_name = "gpt-3.5-turbo"
    chat_model.temperature = 0.0
    conversation = ConversationChain(
        llm=chat_model,
        memory=memory,
        verbose=True
    )
    return conversation

