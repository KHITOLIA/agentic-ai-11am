from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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

chat_history = [
    SystemMessage(content = "You are a helpful assistant in Tech field!")
]

while True:
    user_input = input("enter the query : ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == "stop":
        break
    response = hf_model.invoke(chat_history).content
    chat_history.append(AIMessage(content = response))
    print(f"AI : {response}")

print(chat_history)