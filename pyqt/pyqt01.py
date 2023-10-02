import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

#app
app = QApplication([])

#window
window = QWidget()
window.setWindowTitle('App # 1')
window.setGeometry(200, 200, 560, 160)
my_message = QLabel("<h1>Hello my first app </h1>", parent=window)
my_message.move(120,30)

window.show()

sys.exit(app.exec())