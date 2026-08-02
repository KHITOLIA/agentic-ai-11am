from loader import data_extraction
from parser import prompt_template
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = "gpt-4", temperature = 0, max_completion_tokens = 1000)
data = data_extraction()
template , parser = prompt_template()
chain = template | model | parser
result = chain.invoke({"resume" : data})
print(result.skills)