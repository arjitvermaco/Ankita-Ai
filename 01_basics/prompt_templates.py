from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def create_prompt_template():
    return PromptTemplate(template="write a short story about a {animal} in {word_count} words", input_variables=["animal","word_count"])

aimodel = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt = create_prompt_template()

formatted_prompt = prompt.format(animal="lion", word_count=100)

response = aimodel.invoke(formatted_prompt)

print(response.content)

# def calculate_sum(a, b):
#     return a + b

# print(calculate_sum(1, 2))