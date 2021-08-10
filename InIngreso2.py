# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InIngreso2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Metodos import*
import InGestionarEstudiante
import InEstudiante
import logo

class Ui_MainWiningreso(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.522, y1:0.516909, x2:0.517, y2:1, stop:0.448864 rgba(65, 63, 205, 75), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(180, 0))
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem4, 3, 1, 1, 1)
        self.conta = QtWidgets.QLineEdit(self.frame)
        self.conta.setMinimumSize(QtCore.QSize(180, 30))
        self.conta.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border: none;\n"
"font: 12pt \"Arial\";\n"
"border-bottom: 1px solid black;")
        self.conta.setObjectName("conta")
        self.gridLayout.addWidget(self.conta, 4, 1, 1, 1)
        self.user = QtWidgets.QLineEdit(self.frame)
        self.user.setMinimumSize(QtCore.QSize(180, 30))
        self.user.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border: none;\n"
"font: 13pt \"Arial\";\n"
"border-bottom: 1px solid black;")
        self.user.setText("")
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem6, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.ingresa = QtWidgets.QPushButton(self.frame)
        self.ingresa.setMinimumSize(QtCore.QSize(180, 30))
        self.ingresa.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:#00aaff;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.ingresa.setObjectName("ingresa")
        self.gridLayout.addWidget(self.ingresa, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(226, 0, 0);\n"
"font: 13pt \"Arial\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"font:13pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Reg = QtWidgets.QPushButton(self.frame)
        self.Reg.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:#00aaff;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"background-color: rgb(0, 0, 0);")
        self.Reg.setObjectName("Reg")
        self.horizontalLayout_2.addWidget(self.Reg)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ingresa.clicked.connect(self.inicio)
        self.label_5.setVisible(False)
        self.datosTotal = Metodos()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/imagenes/klipartz.com (5).png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/imagenes/klipartz.com (26).png\"/></p></body></html>"))
        self.conta.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.user.setPlaceholderText(_translate("MainWindow", "Ingrese su usuario"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/imagenes/klipartz.com (6).png\"/></p></body></html>"))
        self.ingresa.setText(_translate("MainWindow", "Ingresar"))
        self.label_5.setText(_translate("MainWindow", "Usuario o contraseña incorrecto"))
        self.label.setText(_translate("MainWindow", "¿No tiene una cuenta?"))
        self.Reg.setText(_translate("MainWindow", "Crear"))

    def abrirInGestionar(self):
        self.ventana = QtWidgets.QMainWindow()
        self.cru = InGestionarEstudiante.Ui_MainWindowGestionar()
        self.cru.setupUi(self.ventana)
        self.ventana.show()
        MainWindow.hide()

    def abrirInEstudia(self,nom,apell,ide):
        self.ventana = QtWidgets.QMainWindow()
        self.cru = InEstudiante.Ui_MainWindow()
        self.cru.setupUi(self.ventana)
        self.cru.var = ide
        self.cru.EstLabel.setText(nom +" "+ apell )
        self.ventana.show()
        MainWindow.hide()


    def inicio(self):

        if not self.conta.text() or not self.user.text():
            confirmar = QtWidgets.QMessageBox()
            confirmar.setIcon(confirmar.Warning)
            confirmar.setText("¡Hay campos vacíos!")
            confirmar.exec_()
            self.label_5.setVisible(True)
        elif self.user.text() == "admin" and self.conta.text() == "123":
            self.abrirInGestionar()
        else:
            idd=self.user.text()
            idd= ("'" + idd + "'")
            co=self.conta.text()
            co = ("'" + co + "'")
            datosA=self.datosTotal.ingresar(idd,co)
            if not datosA:
               self.label_5.setVisible(True)

            else:
                self.label_5.setVisible(False)
                #self.abrirInEstudia(datosA[0][0],datosA[0][1],datosA[0][2])
                self.abrirInGestionar()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWiningreso()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())