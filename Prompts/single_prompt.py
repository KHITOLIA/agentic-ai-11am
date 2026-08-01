from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
def llm_model():
    llm = HuggingFaceEndpoint(
        repo_id = "openai/gpt-oss-120b",
        task = "text-generation",
        temperature = 0,
        max_new_tokens = 3000
    )
    model = ChatHuggingFace(llm = llm)
    return model
hf_model = llm_model()


input_prompt = input("Enter your query : ")
response = hf_model.invoke(input_prompt).content
print(response)
