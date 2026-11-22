from flask import Flask, render_template, redirect, url_for, request
from graph import graph_workflow

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        weight_kg = request.form['weight_kg']
        height_m = request.form['height_m']
        initial_state = {"weight_kg" : weight_kg ,
                 "height_m" : height_m}
        final_state = graph_workflow(initial_state)
        return render_template("home.html", final_state = final_state)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
