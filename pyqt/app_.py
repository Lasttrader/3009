
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor

#load models
contact_le = pickle.load(open('../flask_app/models_tech/contact_le.pkl', 'rb'))
default_le = pickle.load(open('../flask_app/models_tech/default_le.pkl', 'rb'))
education_le = pickle.load(open('../flask_app/models_tech/education_le.pkl', 'rb'))
housing_le = pickle.load(open('../flask_app/models_tech/housing_le.pkl', 'rb'))
job_le = pickle.load(open('../flask_app/models_tech/job_le.pkl', 'rb'))
loan_le = pickle.load(open('../flask_app/models_tech/loan_le.pkl', 'rb'))
marital_le =pickle.load(open('../flask_app/models_tech/marital_le.pkl', 'rb'))
month_le =pickle.load(open('../flask_app/models_tech/month_le.pkl', 'rb'))
poutcome_le = pickle.load(open('../flask_app/models_tech/poutcome_le.pkl', 'rb'))
y_le = pickle.load(open('../flask_app/models_tech/y_le.pkl', 'rb'))
num_scaler = pickle.load(open('../flask_app/models_tech/num_scaler.pkl', 'rb'))
RFR = pickle.load(open('../flask_app/models_ml/RFR.pkl', 'rb'))
print('import done')

x_list = ['unemployed', 'married', 'primary', 'no', 'yes', 'no', 'cellular', 'may', 'unknown', 'no', 4343, 19, 220, 1, 300, 0]

print(x_list)
x_cat = [] #список с категориальными признаками
le_list = [job_le, marital_le, education_le, default_le,
           housing_le, loan_le, contact_le, month_le, poutcome_le, y_le] #список с le
#идём циклом и кодируем категориальные признаки
for i in range(len(x_list[0:10])):
    print(type(x_list[i]))
    x_list[i] = le_list[i].transform([x_list[i]])[0]
    x_cat.append(x_list[i])

#Масштабируем числовые признаки во второй части входного с формы вектора   
x_num = num_scaler.transform([x_list[10:]])[0]
X = []
X.extend(x_cat)
X.extend(x_num)
print(X)
prediction = RFR.predict([X])
print(prediction)