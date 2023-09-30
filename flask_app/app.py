import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from  flask import Flask, request, render_template, jsonify

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

#роутинг
@app.route('/', methods = ['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html') #возвращаем стартовую страницу с формой
    
    if request.method == 'POST':
        #Получаем жданные с формы html (поле name)
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

        #собираем вектор категориальных признаков (порядок должен совпадать с порадокм, который был при обучении
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
        #Собираем вектор числовых признаков, порядок должен также совпадать
        x_num = num_scaler.transform([[balance, 
                day, 
                duration, 
                campaign, 
                pdays, 
                previous]])[0]
        #объединяем категориальные и числовые признаки для прогноза, порядок должен совпадать
        X = []
        X.extend(x_cat)
        X.extend(x_num)
        print(X)
        #прогноз
        prediction = RFR.predict([X])
        print(f'Примерный возраст клиента по введенным данных : {prediction}')
        return render_template('main.html', result = prediction)#возвращаем прогноз в html  в поле result

@app.route('/flskapi/v1/add_message/', methods = ['GET', 'POST']) #API
def api_message():
    x =  request.json #получаем json на входе из других сервисов
    print(x['X_get_age'])
    #нужнео сделать scaler и labelencoder, т.к. сторонний сервис не знает про масштабирование и кодирование даннеых дя модели
    prediction = RFR.predict([x['X_get_age']])#прогноз

    return jsonify(str(prediction)) #возвращаем результат в сервсис, который запросил прогноз

@app.route('/flskapi/v2/add_message/', methods = ['GET', 'POST']) #API
def api_message():
    x =  request.json #получаем json на входе из других сервисов
    print(x['X_get_age'])
    #нужнео сделать scaler и labelencoder, т.к. сторонний сервис не знает про масштабирование и кодирование даннеых дя модели
    prediction = RFR2.predict([x['X_get_age']])#прогноз

    return jsonify(str(prediction)) #возвращаем результат в сервсис, который запросил прогноз


if __name__ == '__main__':
    app.run(debug=True)