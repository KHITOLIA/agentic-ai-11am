from state import BlogState
from graph import graph_workflow

initial_state = {"topic" : input("Enter the topic")}
workflow = graph_workflow(BlogState)
final_state = workflow.invoke(initial_state)

print(workflow)

print()

print(final_state)