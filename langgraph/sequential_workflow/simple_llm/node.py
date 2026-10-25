from state import LLMState
from langchain_google_genai import ChatGoogleGenerativeAI
# define the nodes
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash", temperature = 0)

def llm_qa(state : LLMState) -> LLMState:
    question = state['question']

    prompt = f'Answer the following question {question}'
    # response
    answer = model.invoke(prompt).content[0]['text']
    state['answer'] = answer
    return state