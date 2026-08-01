from typing import TypedDict, List, Dict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

def llm_model():
    llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000)
    model = ChatHuggingFace(llm = llm)
    return model

model = ChatOpenAI()

class Review(BaseModel):
    key_themes : list[str] = Field(description = "Write down all the major key themes discuesse in the review")
    summary : str = Field(description = "A brief summarization of the review")
    sentiment : Literal["+ve", "-ve"] = Field(description="Write the sentiment of the review  either negative , positive or neutral")
    pros : Optional[list[str]] = Field(description="Write all the pros of the product in the review")
    cons : Optional[list[str]] =  Field(description= "Write all the cons of the prodcut in the review")
    name : Optional[str] =  Field(description = "Write down the name of reviewer mentioned in the review")

honest_review = '''

Kunal
1 out of 5 starsFaulty Phone
Reviewed in India on 8 July 2026
Size: 4GB + 64GBStyle Name: 2026Colour: Sage Green
Verified Purchase
Bought a brand new **Samsung Galaxy M06 5G** from this seller with **Open Box Inspection** and got a faulty phone. The delivery associate was in a hurry and only asked my elderly parents to check for physical damage before leaving. There was no time to test the phone's speaker.


After setup, we found the speaker volume was extremely low—even at maximum volume, you have to hold the phone close to your ear to hear videos or calls. Amazon Customer Service refused to replace or return the phone and instead asked us to visit a Samsung service centre. My elderly parents went there the very next day, only to be told that this is the "maximum sound" because it's a budget phone, which is not an acceptable explanation for a brand-new device.


Very disappointed with both the product quality and the after-sales support. Buyers should thoroughly test every function during Open Box Inspection, as getting a replacement or return later may not be easy.
'''
structured_model = model.with_structured_output(Review)
result = structured_model.invoke(honest_review)

print(result)