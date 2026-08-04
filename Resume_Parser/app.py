from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from resume_tool import extract_resume

app = Flask(__name__)

upload_folder = "uploads"

app.config["upload_folder"] = upload_folder
os.makedirs(upload_folder, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/extract", methods = ["POST"])
def extract():

    file = request.files["resume"]
    filename = secure_filename(file.filename)
    path = os.path.join(app.config["upload_folder"], filename)

    file.save(path)
    result = extract_resume(path)
    return render_template("result.html", resume = result)

if __name__ == "__main__":
    app.run(debug=True)
