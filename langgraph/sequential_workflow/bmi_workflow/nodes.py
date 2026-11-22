from state import BMIState
from model import Model

def calculate_bmi(state : BMIState) -> BMIState:
    weight = state['weight_kg']
    height = state['height_m']

    bmi = weight/(height ** 2)
    state['bmi'] = bmi
    return state


def label_bmi(state : BMIState) -> BMIState:
    bmi = state['bmi']
    prompt = f"Analyse the bmi value {bmi} and returns me the category in which the bmi falls in return me only the category name"
    
    category = Model.invoke(prompt).content[0]['text']
    state['category'] = category
    return state