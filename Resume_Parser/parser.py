from typing import List, Optional
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate


class Resume(BaseModel):
    name : str = Field(description = "Give me the name of the candidate : ")
    phone : str = Field(description = "Give me the contact detail of the candidate : ")
    email : str = Field(description = "Provide me the email id mentioned in the resume : ")
    skills : Optional[List[str]] = Field(description = "return all the skill set the candidate have : ") 
    experience : Optional[List[str]] = Field(description = "how much experience does this candidate have along with the respective companies : ")
    projects : Optional[List[str]] = Field(description = "give me the projects mentioned in the resume : ")


def prompt_template():
    parser = PydanticOutputParser(pydantic_object=Resume)
    template = PromptTemplate(
        template = '''
        Give me the entire details of the candidate from the uploaded resume {resume} \n {format_instruction}''',
        input_variables = ['resume'],
        partial_variables = {"format_instruction" : parser.get_format_instructions()})
    return template, parser

#  product name
#  reviewer name
#  date of submission
#  pros
#  cons
#  summary
#  sentiment
#  rating

# if sentiment is not good:
    # then mail the review back to the customer care(tushar@trainingbasekt.co)