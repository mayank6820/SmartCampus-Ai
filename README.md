# SmartCampus AI 🎓🤖

SmartCampus AI is a machine-learning based early-warning system for predicting student academic risk and generating simple personalized recommendations.

## Features
- Student academic-risk prediction
- Random Forest ML model
- Risk confidence score
- Personalized recommendations
- Flask web interface
- Sample dataset for experimentation
- GitHub-ready project structure

## Risk classes
- **Low Risk** – student is performing well
- **Needs Support** – student may benefit from additional support
- **High Risk** – student may need immediate academic intervention

## Project structure

```text
SmartCampus_AI/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── data/
│   └── student_data.csv
├── models/
│   └── student_success_model.pkl
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally

### 1. Create a virtual environment
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Retrain the model

```bash
python train_model.py
```

## Important note
This is an educational ML project. Predictions are indicators for academic support, not definitive judgments about a student's ability or future.

## Suggested future improvements
- Login and role-based access
- PostgreSQL/Firebase database
- Attendance API integration
- Explainable AI with SHAP
- Model monitoring
- Student progress history
- Cloud deployment

## Author
Mayank

B.tech Ai/Ml
