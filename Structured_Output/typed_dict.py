from typing import TypedDict, List, Dict
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

model = llm_model()

class Review(TypedDict):
    summary : str
    sentiment : str

structured_model = model.with_structured_output(Review)
honest_review = '''
I recently bought this phone and unfortunately it has not lived up to the expectations.


• Severe Overheating: The phone gets uncomfortably hot during basic tasks like browsing and charging.

• Performance Lags: Apps stutter, freeze, and sometimes crash entirely during routine use.


I cannot recommend this device in its current state. For a newly launched phone, the day-to-day optimization is lacking.

I am hoping a software update fixes these optimization bugs soon, but for now, look elsewhere.
'''

result = structured_model.invoke(honest_review)
print(result)