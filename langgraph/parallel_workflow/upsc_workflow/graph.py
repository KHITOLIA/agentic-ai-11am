from langgraph.graph import StateGraph, START, END
from state import UPSCState, EvaluationSchema
from nodes import evalaute_thoughts, evaluate_analysis, evaluate_language, final_evaluation

def graph_workflow(initial_state):

    graph = StateGraph(UPSCState)

    graph.add_node("evaluate_language" , evaluate_language)
    graph.add_node("evaluate_analysis" , evaluate_analysis)
    graph.add_node("evaluate_thoughts", evalaute_thoughts)
    graph.add_node("final_evaluation", final_evaluation)

    graph.add_edge(START, "evaluate_language")
    graph.add_edge(START, "evaluate_analysis")
    graph.add_edge(START, "evaluate_thoughts")

    graph.add_edge("evaluate_language", "final_evaluation")
    graph.add_edge("evaluate_analysis", "final_evaluation")
    graph.add_edge("evaluate_thoughts", "final_evaluation")

    graph.add_edge("final_evaluation", END)

    workflow = graph.compile()

    return workflow.invoke(initial_state)