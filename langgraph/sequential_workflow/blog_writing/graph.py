from langgraph.graph import StateGraph, START, END
from node import outline, blog

def graph_workflow(state):
    graph = StateGraph(state)
    graph.add_node("outline", outline)
    graph.add_node("blog", blog)

    graph.add_edge(START, "outline")
    graph.add_edge("outline", "blog")
    graph.add_edge("blog", END)

    workflow = graph.compile()
    return workflow
