from langchain_ollama import ChatOllama
from warnings import filterwarnings
filterwarnings("ignore")

model = ChatOllama(
    model = "mistral",
    temperature = 0.3, 
    max_tokens = 100
)

result = model.invoke("What is machine learning?")
print()
print(result.content)