from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from InIngreso2 import Ui_MainWiningreso
from InEstudiante import Ui_MainWindow
import sys

class paEstudiante(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class paIngreso(QMainWindow, Ui_MainWiningreso):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ingresa.clicked.connect(self.estu)
        self.estudiante = paEstudiante()
    def estu(self):
        self.estudiante.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = paIngreso()
    Window.show()
    sys.exit(app.exec_())