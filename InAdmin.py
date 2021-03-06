# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.522, y1:0.516909, x2:0.517, y2:1, stop:0.448864 rgba(65, 63, 205, 75), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 87 18pt \"Arial Black\";\n"
"color: rgb(0,0,0);\n"
"background-color: rgba(0, 0, 0,0%);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(120, 120))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.AdBotGesDoc = QtWidgets.QPushButton(self.frame)
        self.AdBotGesDoc.setStyleSheet("QPushButton{\n"
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
        self.AdBotGesDoc.setObjectName("AdBotGesDoc")
        self.verticalLayout_2.addWidget(self.AdBotGesDoc)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(120, 120))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.AdBotGesEst = QtWidgets.QPushButton(self.frame)
        self.AdBotGesEst.setStyleSheet("QPushButton{\n"
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
        self.AdBotGesEst.setObjectName("AdBotGesEst")
        self.verticalLayout.addWidget(self.AdBotGesEst)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(120, 120))
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.AdBotHisto = QtWidgets.QPushButton(self.frame)
        self.AdBotHisto.setStyleSheet("QPushButton{\n"
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
        self.AdBotHisto.setObjectName("AdBotHisto")
        self.verticalLayout_3.addWidget(self.AdBotHisto)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.AcBotSal = QtWidgets.QPushButton(self.frame)
        self.AcBotSal.setStyleSheet("QPushButton{\n"
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
        self.AcBotSal.setObjectName("AcBotSal")
        self.horizontalLayout_5.addWidget(self.AcBotSal)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenido Administrador"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/imagenes/klipartz.com (22).png\"/></p></body></html>"))
        self.AdBotGesDoc.setText(_translate("MainWindow", "Gestionar docente"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/imagenes/klipartz.com (23).png\"/></p></body></html>"))
        self.AdBotGesEst.setText(_translate("MainWindow", "Gestionar estudiante"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/imagenes/klipartz.com (24).png\"/></p></body></html>"))
        self.AdBotHisto.setText(_translate("MainWindow", "Historial cl??nico"))
        self.AcBotSal.setText(_translate("MainWindow", "Salir"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
