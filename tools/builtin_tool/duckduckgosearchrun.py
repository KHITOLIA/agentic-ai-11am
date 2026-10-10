from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Create Wikipedia API wrapper
wikipedia = WikipediaAPIWrapper()

# Create Wikipedia tool
tool = WikipediaQueryRun(api_wrapper=wikipedia)

# Run query
result = tool.invoke("Who is MS Dhoni?")

print(result)