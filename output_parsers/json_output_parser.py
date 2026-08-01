from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


def llm_model():
    llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000)
    model = ChatHuggingFace(llm = llm)
    return model

model = llm_model()
parser = JsonOutputParser()

# template = PromptTemplate(
#     template = 'Give me 5 facts about {topic} \n {format_instruction}',
#     input_variables = ['topic'],
#     partial_variables = {"format_instruction" : parser.get_format_instructions()}
# )

template = PromptTemplate(
    template = 'Give me the name, age, city of any marvel character in real life  \n {format_instruction}',
    input_variables = [],
    partial_variables = {"format_instruction" : parser.get_format_instructions()} 
)

chain = template | model | parser
result = chain.invoke({"topic" : "Black Panther"})
print(result)