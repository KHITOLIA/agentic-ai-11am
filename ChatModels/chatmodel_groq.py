from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile", temperature = 0)
result = model.invoke("What is machine learning ? ")
print(result.content)