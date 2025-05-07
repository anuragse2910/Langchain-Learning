from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv  import load_dotenv


load_dotenv()
model = ChatGoogleGenerativeAI(model = 'Gemini-2.0-Flash Lite')

result = model.invoke("what is the capital of India")

print(result.context)