from state import UPSCState
from model import structure_model

def evaluate_language(state : UPSCState):
    prompt = f'Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10'
    output = structure_model.invoke(prompt)
    return {"language_feedback" : output.feedback, "individual_scores" : [int(output.score)]}


def evaluate_analysis(state : UPSCState):
    prompt = f'Evaluate the depth of analysis of the following essay and provide a feedback and assign a score out of 10'
    output = structure_model.invoke(prompt)
    return {"analysis_feedback" : output.feedback, "individual_scores" : [int(output.score)]}


def evalaute_thoughts(state : UPSCState):
    prompt = f'Evaluate the clarity of thought of the following essay and provide a feedback and assign a score out of 10'
    output = structure_model.invoke(prompt)
    return {"clarity_feedback" : output.feedback, "individual_scores" : [int(output.score)]}

def final_evaluation(state : UPSCState):

    prompt = f'''Based on the following feedback create a summarized feedback \n
    language feedback {state['language_feedback']} \n
    analysis feedback {state['analysis_feedback']} \n
    clarity feedback {state['clarity_feedback']}'''

    overall_feedback = structure_model.invoke(prompt)
    avg_score = sum(state['individual_scores'])/len(state['individual_scores'])

    return {"overall_feedback" : overall_feedback, "avg_score" : avg_score}