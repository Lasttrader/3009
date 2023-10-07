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
        
        self.e1 = QLineEdit()
        self.e1.textEdited.connect(self.make_x_for_predict(1))
        self.layout.addRow(QLabel("Введите Job"), self.e1)
        self.e2 = QLineEdit()
        self.e2.textEdited.connect(self.make_x_for_predict(2))
        self.layout.addRow(QLabel("Введите marital"), self.e2)
        self.e3 = QLineEdit()
        self.e3.textEdited.connect(self.make_x_for_predict(3))
        self.layout.addRow(QLabel("Введите education"), self.e3)
        self.e4 = QLineEdit()
        self.e4.textEdited.connect(self.make_x_for_predict(4))
        self.layout.addRow(QLabel("Введите default"), self.e4)        
        self.e5 = QLineEdit()
        self.e5.textEdited.connect(self.make_x_for_predict(5))
        self.layout.addRow(QLabel("Введите housing"), self.e5) 
        self.e6 = QLineEdit()
        self.e6.textEdited.connect(self.make_x_for_predict(6))
        self.layout.addRow(QLabel("Введите loan"), self.e6) 
        self.e7 = QLineEdit()
        self.e7.textEdited.connect(self.make_x_for_predict(7))
        self.layout.addRow(QLabel("Введите contact"), self.e7)         
        self.e8 = QLineEdit()
        self.e8.textEdited.connect(self.make_x_for_predict(8))
        self.layout.addRow(QLabel("Введите month"), self.e8) 
        self.e9 = QLineEdit()
        self.e9.textEdited.connect(self.make_x_for_predict(9))
        self.layout.addRow(QLabel("Введите poutcome"), self.e9) 
        self.e10 = QLineEdit()
        self.e10.textEdited.connect(self.make_x_for_predict(10))
        self.layout.addRow(QLabel("Введите y"), self.e10)
        self.e11 = QLineEdit()
        self.e11.textEdited.connect(self.make_x_for_predict(11))
        self.layout.addRow(QLabel("Введите balance"), self.e11)
        self.e12 = QLineEdit()
        self.e12.textEdited.connect(self.make_x_for_predict(12))
        self.layout.addRow(QLabel("Введите day"), self.e12)
        self.e13 = QLineEdit()
        self.e13.textEdited.connect(self.make_x_for_predict(13))
        self.layout.addRow(QLabel("Введите duration"), self.e13)
        self.e14 = QLineEdit()
        self.e14.textEdited.connect(self.make_x_for_predict(14))
        self.layout.addRow(QLabel("Введите campaign"), self.e14)
        self.e15 = QLineEdit()
        self.e15.textEdited.connect(self.make_x_for_predict(16))
        self.layout.addRow(QLabel("Введите pdays"), self.e15)
        self.e17 = QLineEdit()
        self.e17.textEdited.connect(self.make_x_for_predict(17))
        self.layout.addRow(QLabel("Введите previous"), self.e17)

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

