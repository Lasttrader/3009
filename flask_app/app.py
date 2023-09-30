import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from  flask import Flask, request, render_template

#load models
contact_le = pickle.load(open('models_tech/contact_le.pkl', 'rb'))
default_le = pickle.load(open('models_tech/default_le.pkl', 'rb'))
education_le = pickle.load(open('models_tech/education_le.pkl', 'rb'))
housing_le = pickle.load(open('models_tech/housing_le.pkl', 'rb'))
job_le = pickle.load(open('models_tech/job_le.pkl', 'rb'))
loan_le = pickle.load(open('models_tech/loan_le.pkl', 'rb'))
marital_le =pickle.load(open('models_tech/marital_le.pkl', 'rb'))
month_le =pickle.load(open('models_tech/month_le.pkl', 'rb'))
poutcome_le = pickle.load(open('models_tech/poutcome_le.pkl', 'rb'))
y_le = pickle.load(open('models_tech/y_le.pkl', 'rb'))
num_scaler = pickle.load(open('models_tech/num_scaler.pkl', 'rb'))
RFR = pickle.load(open('models_ml/RFR.pkl', 'rb'))

#app
app = Flask(__name__,  template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    
    if request.method == 'POST':
        contact = contact_le.transform([request.form['contact']])[0]
        default = default_le.transform([request.form['default']])[0]
        education = education_le.transform([request.form['education']])[0]
        housing = housing_le.transform([request.form['housing']])[0]
        job = job_le.transform([request.form['job']])[0]
        loan = loan_le.transform([request.form['loan']])[0]
        marital = marital_le.transform([request.form['marital']])[0]
        month = month_le.transform([request.form['month']])[0]
        poutcome = poutcome_le.transform([request.form['poutcome']])[0]
        y = y_le.transform([request.form['y']])[0]
        balance = float(request.form['balance'])
        day = float(request.form['day'])
        duration = float(request.form['duration'])
        campaign = float(request.form['campaign'])
        pdays = float(request.form['pdays'])
        previous= float(request.form['previous'])

        x_cat = [job,
                marital,	
                education,	
                default,	
                housing,	
                loan,	
                contact,	
                month,	
                poutcome,	
                y]

        x_num = num_scaler.transform([[balance, 
                day, 
                duration, 
                campaign, 
                pdays, 
                previous]])[0]
        X = []
        X.extend(x_cat)
        X.extend(x_num)
        prediction = RFR.predict([X])
        print(f'Примерный возраст клиента по введенным данных : {prediction}')
        return render_template('main.html', result = prediction)


if __name__ == '__main__':
    app.run(debug=True)