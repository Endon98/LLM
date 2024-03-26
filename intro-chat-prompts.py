import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"
chat_model = ChatOpenAI(model=llm_model, temperature=0.1)

answer = chat_model.invoke("Who is Ralph Gonsalves")
print(answer.content)
