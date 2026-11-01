from state import BlogState
from model import llm
# define the outline node

def outline(state : BlogState) -> BlogState:
    topic = state['topic']
    prompt  = f"Generate the detailed outline about the topic {topic}"
    outline = llm.invoke(prompt).content
    state['outline'] = outline
    return state

# define the blog node

def blog(state : BlogState) -> BlogState:
    outline = state['outline']
    topic = state['topic']
    prompt = f"Generate the proper and detailed blog from the topic \n{topic} and the outline \n {outline}"
    state['blog'] = llm.invoke(prompt).content
    return state
