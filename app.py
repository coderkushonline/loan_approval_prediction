from flask import Flask, render_template, request, url_for, redirect
import pickle
import pandas as pd
app = Flask(__name__)

### Reading pickle files
scaler = pickle.load(open('artifacts/scaler.pkl', 'rb'))
model = pickle.load(open('artifacts/model.pkl', 'rb'))
# encoder = pickle.load(open('artifacts/encoder.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    pred = request.args.get('prediction', "2") 
    # print(pred, type(int(pred)))
    # print(list(pred))
    return render_template('index.html', prediction=int(pred))

@app.route('/predict', methods=['POST'])
def predict():
    income = float(request.form.get('income'))
    c_score = float(request.form.get('c_score'))
    loan_amt = float(request.form.get('loan_amt'))
    emp_yrs = float(request.form.get('emp_yrs'))
    
    loan_income_pct = (loan_amt/income) * 100

    data = {
        "credit_score": c_score,
        "years_employed": emp_yrs,
        "income_loan_pct": loan_income_pct
    }

    df = pd.DataFrame(data, index=[0])

    df_scaled = scaler.transform(df)

    prediction=model.predict(df_scaled)
    return redirect(url_for('home', prediction=int(prediction)))

if __name__ == "__main__" :
    app.run(debug=False, port=5000, host="0.0.0.0")