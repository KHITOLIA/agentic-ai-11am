# from langchain_experimental.tools import PythonREPLTool
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# load_dotenv()
# model = ChatOpenAI(model = 'gpt-5')
# response = model.invoke("Return me only the code logic for printing numbers from 1 to 10 using for loop nothing else is required just give me the code")
# code = str(response.content)
# python_tool = PythonREPLTool()
# result = python_tool.invoke(code)
# print(result)

# exec("print(5 * 5)")