from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

Model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature=0)
