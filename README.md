# Loan Approval Prediction

**Dataset Overview**

[Dataset Link](https://www.kaggle.com/datasets/anishdevedward/loan-approval-dataset)

This dataset simulates loan applications and their approval outcomes for 2,000 individuals. It includes a range of demographic, financial, and employment-related attributes such as age, income, credit score, loan amount, employment status, and existing debts.
The dataset aims to model credit risk and loan approval prediction, providing an excellent opportunity to practice binary classification, data preprocessing, and feature engineering in the financial domain.


☀️**Objective:**

Build a machine learning model that predicts whether a loan application will be approved or rejected based on applicant attributes.

🖥️**Applications:**

* Credit risk modeling

* Loan approval prediction

* Customer profiling

* Model interpretability and fairness analysis

### 🚀Project Workflow
1. Import Libraries & Load Dataset
    
2. Exploratory Data Analysis (EDA) & Feature Engineering

3. Data Preprocessing

4. Model Building

5. Hyperparameter Tuning (if necessary)

6. Model Evaluation

7. Model Export

8. UI Design

9. Deployment

### Project Setup Instructions

Clone the repo:
```bash
git clone https://github.com/coderkushonline/loan_approval_prediction
cd loan_approval_prediction
```

Check Status:
```bash
git status
```

Setup virtual environment & requirements:
```bash
python -m venv venv

# For Linux
source venv/Scripts/activate

# For Windows
cd venv/Scripts
activate.bat

# Install requirements
pip install -r requirements.txt
```

Run flask server
```bash
flask run -p 5000

### OR
python3 app.py
```

### Run from DockerHub
```bash
docker pull coderkush/loan_predictor
docker run -p 5000:5000 coderkush/loan_predictor
```

## Conclusion
Hence, the loan approvement system was made successfully. Additional analysis information are given in loan_approval_classification.ipynb file. 

