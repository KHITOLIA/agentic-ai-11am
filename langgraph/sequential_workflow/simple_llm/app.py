from graph import graph_workflow

initial_state = {"question" : input("Enter the question : ")}

final_state = graph_workflow().invoke(initial_state)

print(final_state)