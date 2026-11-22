# define the graph
from langgraph.graph import StateGraph, START, END
from state import BMIState
from nodes import calculate_bmi, label_bmi

def graph_workflow(initial_state):
        graph = StateGraph(BMIState)
        graph.add_node("calculate_bmi", calculate_bmi)
        graph.add_node("label_bmi", label_bmi)

        graph.add_edge(START, "calculate_bmi")
        graph.add_edge("calculate_bmi", "label_bmi")
        graph.add_edge("label_bmi", END)

        workflow = graph.compile()
        final_state = workflow.invoke(initial_state)
        return final_state