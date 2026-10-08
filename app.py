from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("models/student_success_model.pkl")

FEATURES = [
    "attendance",
    "study_hours",
    "assignment_score",
    "internal_marks",
    "previous_gpa",
    "sleep_hours",
    "extracurricular_hours",
]

def recommendation(risk, row):
    if risk == "High Risk":
        return "Increase attendance, study 2+ focused hours daily, submit all assignments, and meet a faculty mentor."
    if risk == "Needs Support":
        return "Maintain regular attendance and improve weak subjects through weekly revision and practice."
    return "Keep your current routine and continue building projects, communication skills, and technical depth."

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        values = {f: float(request.form[f]) for f in FEATURES}
        X = pd.DataFrame([values])
        risk = model.predict(X)[0]
        probability = model.predict_proba(X).max() * 100
        result = {
            "risk": risk,
            "confidence": round(probability, 1),
            "recommendation": recommendation(risk, values),
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
