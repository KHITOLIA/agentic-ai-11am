# from flask import Flask, redirect, request, render_template
# from ChatModels.chatmodel_hf_api import llm_model
# from Prompts.prompt_template import PT

# template = PT()
# model = llm_model()

# app = Flask(__name__)

# # url : /

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == 'POST':
#         paper_input = request.form['paper_input']
#         style_input = request.form['style_input']
#         length_input = request.form['length_input']

#         prompt = template.invoke({
#             "paper_input": paper_input,
#             "style_input": style_input,
#             "length_input": length_input
#         })
#         response = model.invoke(prompt).content

#         # NOTE: the original code rendered home.html without passing
#         # `response` back to the template, so the result never showed up
#         # on the page. Passing it (plus the selections) is what makes the
#         # "Readout" panel in the new UI actually display something.
#         return render_template(
#             "home.html",
#             response=response,
#             paper_input=paper_input,
#             style_input=style_input,
#             length_input=length_input
#         )

#     return render_template("home.html")


# if __name__ == "__main__":
#     app.run(debug=True)


from typing import TypedDict, AnyStr, List, Dict

class Person(TypedDict):
    name: str
    age : int

new_person: Person = {"name": "Tushar", "age" : "45"}  
print(new_person)