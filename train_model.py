import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
from pathlib import Path

df = pd.read_csv("data/student_data.csv")

features = [
    "attendance", "study_hours", "assignment_score",
    "internal_marks", "previous_gpa", "sleep_hours",
    "extracurricular_hours"
]
X = df[features]
y = df["risk_level"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=200, max_depth=8, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print(classification_report(y_test, pred))

Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/student_success_model.pkl")
print("Saved: models/student_success_model.pkl")
