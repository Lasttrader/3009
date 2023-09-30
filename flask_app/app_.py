import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import flask


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


contact = contact_le.transform([input('Введите contact: ')])[0]
default = default_le.transform([input('Введите default: ')])[0]
education = education_le.transform([input('Введите education: ')])[0]
housing = housing_le.transform([input('Введите housing: ')])[0]
job = job_le.transform([input('Введите job: ')])[0]
loan = loan_le.transform([input('Введите loan: ')])[0]
marital = marital_le.transform([input('Введите marital: ')])[0]
month = month_le.transform([input('Введите month: ')])[0]
poutcome = poutcome_le.transform([input('Введите poutcome: ')])[0]
y = y_le.transform([input('Введите y: ')])[0]
balance = float(input('Введите balance'))
day = float(input('Введите day'))
duration = float(input('Введите duration'))
campaign = float(input('Введите campaign'))
pdays = float(input('Введите pdays'))
previous= float(input('Введите previous'))


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
# X = [10, 1, 1, 0,  1, 1, 0, 8, 3, 0, 1.1186442, 0.37405208,
#      -0.515577, -0.5768295,  2.899143,   2.0417337 ]
prediction = RFR.predict([X])
print(f'Примерный возраст клиента по введенным данных : {prediction}')
