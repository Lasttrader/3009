import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QGroupBox, 
    QLabel,
    QMessageBox
)
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

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.x_for_predict = {}
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | 
                                     QDialogButtonBox.StandardButton.Cancel)
        buttonBox.accepted.connect(self.my_predict)# самописная реакция на нажатие кнопки ОК
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Age prediction app")
        
    def createFormGroupBox(self):
        '''
        заполняем поля в окне 
        '''
        self.formGroupBox = QGroupBox("My Form layout")
        self.layout =QFormLayout()
        
        for index, label in enumerate(["Введите Job", "Введите marital", "Введите education",
            "Введите default", "Введите housing", "Введите loan",
            "Введите contact", "Введите month",  "Введите poutcome", "Введите y", "Введите balance", 
            "Введите day", "Введите duration", "Введите campaign", "Введите pdays", "Введите previous"]):
            x = QLineEdit()
            x.textEdited.connect(self.make_x_for_predict(index + 1))
            self.layout.addRow(QLabel(label), x)        

        self.formGroupBox.setLayout(self.layout)

    def make_x_for_predict(self, x):
        '''
        Функция собирает веткор для предикта
        '''
        def savedX(text):
            self.x_for_predict[x] = text
        return savedX


    def my_predict(self):
        '''
        функция выполняет логику ML и возвращает прогноз в новом окне
        '''
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Ваш прогноз")
        dlg.setGeometry(200, 200, 560, 160)
        x_list = list(self.x_for_predict.values())
        #print(x_list)
        x_cat = [] #список с категориальными признаками
        #print(x_list)
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
        #print(X)
        prediction = RFR.predict([X])
        #print(prediction)

        dlg.setText(f'Прогнозный возраст равен_ {prediction}')
        dlg.exec()


#запуск и закрытие приложения
app = QApplication(sys.argv)
dialog = Dialog()
dialog.exec()
print(dialog.x_for_predict) #техническое сообщение с вектором на прогноз
app.exit()

