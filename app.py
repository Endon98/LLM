import os
import openai
from dotenv import find_dotenv, load_dotenv
# from langchain.llms import OpenAI # Deprecated
from langchain_openai import OpenAI

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

llm = OpenAI(temperature=0.0)   # Measure of creativity in the response (low 0, 0.7 high)

# print(llm.predict('Who is Ralph Gonsalves')) #deprecated 
print(llm.invoke('Who is Ralph Gonsalves'))
