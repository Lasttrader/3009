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
        dlg.setText(f'Ваши данные {self.x_for_predict}')
        dlg.exec()




#запуск и закрытие приложения
app = QApplication(sys.argv)
dialog = Dialog()
dialog.exec()
print(dialog.x_for_predict) #техническое сообщение с вектором на прогноз
app.exit()