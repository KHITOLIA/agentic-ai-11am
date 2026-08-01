from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
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

chat_template = ChatPromptTemplate(
    [
        ("sytem", "You are a helpful assistant or an agent in tech field "),
        MessagesPlaceholder(variable_name = "chat_history"),
        ("human", "{query}")
    ]
)

chat_history = []