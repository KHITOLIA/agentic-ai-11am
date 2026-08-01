from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
model = ChatOpenAI(model = "gpt-5.5", temperature = 0, max_completion_tokens = 1000)


class Person(BaseModel):
    name : str = Field(description = "Write the name of the person")
    age : int = Field(description = "write the age of the person")
    city : str = Field(description = "write down city of the person")

parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = '''Give me the name , age, city of any character {movie} \n {format_instruction}''',
    input_variables = ['movie'],
    partial_variables = {"format_instruction" : parser.get_format_instructions()}
)


# chain = template | model | parser
# response = chain.invoke({"movie" : "Captain America Civil War"})
# print(response)

# print(template.invoke({"movie" : "Captain America Civil War"}))
# prompt = '''Give me the name , age, city of any character Captain America Civil War \n The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "Write the name of the person", "title": "Name", "type": "string"}, "age": {"description": "write the age of the person", "title": "Age", "type": "integer"}, "city": {"description": "write down city of the person", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'''
# print(model.invoke(prompt))
