#from langchain_openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

"""
* OPEN AI WORKING *

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the Capital of India")

print(result)
"""

llm = ChatGoogleGenerativeAI(model ="gemini-2.0-flash")

result = llm.invoke("What is the capital of India")

print(result)