from langgraph.graph import StateGraph, START, END
from state import LLMState
from node import llm_qa

def graph_workflow():
    graph = StateGraph(LLMState)
    graph.add_node("llm_qa", llm_qa)

    graph.add_edge(START, "llm_qa")
    graph.add_edge("llm_qa", END)

    workflow = graph.compile()
    return workflow
