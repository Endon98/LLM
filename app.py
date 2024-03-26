import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")



llm_model = "gpt-3.5-turbo"


prompt = "How old is the Universe"
messages = [HumanMessage(content=prompt)]
# llm = OpenAI(temperature=0.7)   # Measure of creativity in the response (low 0, 0.7 high)
chat_model = ChatOpenAI(temperature=0.0)

# print(llm.invoke('Who is Ralph Gonsalves'))
# print("======================")
# print(chat_model.invoke("Who is Ralph Gonsalves"))
print(chat_model.invoke(messages).content)
