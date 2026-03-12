from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("data/sample_scholarships.csv")

@app.route("/", methods=["GET","POST"])
def home():

    results = data

    if request.method == "POST":

        query = request.form.get("search").lower()

        results = data[
            data["name"].str.lower().str.contains(query) |
            data["country"].str.lower().str.contains(query) |
            data["field"].str.lower().str.contains(query)
        ]

    return render_template("index.html", scholarships=results.to_dict("records"))

if __name__ == "__main__":
    app.run(debug=True)
