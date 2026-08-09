from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model = ChatGroq(model = "llama-3.3-70b-versatile", temperature = 0, max_tokens = 4000)
str_parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

pydantic_parser = PydanticOutputParser(pydantic_object = Feedback )

prompt1 = PromptTemplate(
    template = '''Classify the sentiment of the following feedback into positive and negative  \ {feedback} \t
    Return only json object sentiment
    do not return anything else except json object
    {format_instruction}''',
    input_variables = ['feedback'],
    partial_variables = {
        'format_instruction' : pydantic_parser.get_format_instructions()
    }
)

classifier_chain = prompt1 | model | pydantic_parser

# print(classifier_chain.invoke({"feedback" : "This samsung phone is very good"}).sentiment)

prompt2 = PromptTemplate(
    template = '''Write an appropriate one line response to this positive feedback \n {feedback}''',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = '''Write an appropriate one line response to this negative feedback \n {feedback}''',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model | str_parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | str_parser),
    RunnableLambda(lambda x : "Could not find the sentiment of the feedback")
)

chain = classifier_chain | branch_chain
feedback = '''After using the Samsung Galaxy A56 for two weeks, I honestly don't understand many of the negative reviews. My experience has been excellent—the display is gorgeous, performance is smooth, the cameras take great photos, battery life easily lasts a full day, and UI feels polished and reliable.

I was initially worried after reading complaints about heating, battery drain, and lag but I haven't faced any of those issues in normal day-to-day use.'''

result = chain.invoke({"feedback" : feedback})

print(result)