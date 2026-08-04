from loader import data_extraction
from parser import prompt_template
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = "gpt-4", temperature = 0, max_completion_tokens = 1000)
template , parser = prompt_template()
chain = template | model | parser
def extract_resume(file_path):
    data = data_extraction(resume_file_path=file_path)
    result = chain.invoke({"resume" : data})
    return result

print(extract_resume(file_path = r"C:\Users\Admin\Desktop\projects\Agentic AI\Tushar Khitoliya resume.pdf" ))