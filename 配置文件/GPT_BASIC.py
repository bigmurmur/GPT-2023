#This file is basicly used for the configuration of Big Language Model from OpanAI.
#The default model is gpt-3.5-turbo,which can be replaced with gpt-4 temporarily.
#from GPT_BASIC import Get_completion

import os
import openai
import tiktoken
openai.api_base="web"
#from dotenv import load_dotenv,find_dotenv
#load_dotenv(find_dotenv())
# If you are concerned about security issues, please use the code above.
openai.api_key="key"

def Get_completion(prompt,model="gpt-3.5-turbo"):
    messages=[{"role":"user","content":prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
    )
    return response.choices[0].message.content

