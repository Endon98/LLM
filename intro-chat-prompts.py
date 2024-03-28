import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"
chat_model = ChatOpenAI(model=llm_model, temperature=0.7)

def get_completion(prompt, model=llm_model):
    messages = [{"role":"user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

# Translate text, review
customer_review = """
    Your product is terrible! I don't know how
    you were able to get this to the market.
    I don't want this!
"""
tone = "an aggresive tone"
language = "chinese"

prompt = f"""
    Rewrite the following {customer_review} into {tone} and
    translate it into {language}.
"""

rewrite = get_completion(prompt=prompt)
# ================== Using Langchain and prompt templates =======================

# Set up template string
template_string = """
    Rewrite the following {customer_review} into {tone}
    translate it into {language}.
"""

# Prompt template
Promp_template = ChatPromptTemplate.from_template(
    template_string
)

# The placeholders in the template string become parameters for the translated message.
translate_message = Promp_template.format_messages(
    customer_review = customer_review,
    language = language,
    tone = tone
)

# Invoke a respones.
response = chat_model.invoke(translate_message)

print(response.content)