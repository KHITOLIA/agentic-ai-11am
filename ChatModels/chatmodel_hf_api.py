from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

def llm_model():
    llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000)
    model = ChatHuggingFace(llm = llm)
    return model