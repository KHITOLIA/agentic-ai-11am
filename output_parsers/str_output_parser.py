from typing import TypedDict, List, Dict, Annotated, Optional, Literal
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def llm_model():
    llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000)
    model = ChatHuggingFace(llm = llm)
    return model

model = llm_model()
parser = StrOutputParser()


template_1 = PromptTemplate(
    template = "Write a detailed report on the {topic}",
    input_variables = ['topic'] 
)

template_2 = PromptTemplate(
    template = "Write a summary in 5 lines of the text {text}",
    input_variables = ['text']
)

chain = template_1 | model | parser | template_2 | model | parser

result = chain.invoke({"topic" : input("Enter the topic")})
print(result)

