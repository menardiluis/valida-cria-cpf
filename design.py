# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(517, 149)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.inputValidaCpf = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.inputValidaCpf.setFont(font)
        self.inputValidaCpf.setObjectName("inputValidaCpf")
        self.gridLayout.addWidget(self.inputValidaCpf, 0, 1, 1, 1)
        self.btnValidaCpf = QtWidgets.QPushButton(self.centralwidget)
        self.btnValidaCpf.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnValidaCpf.setFont(font)
        self.btnValidaCpf.setObjectName("btnValidaCpf")
        self.gridLayout.addWidget(self.btnValidaCpf, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.BtnGeraCpf = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BtnGeraCpf.setFont(font)
        self.BtnGeraCpf.setObjectName("BtnGeraCpf")
        self.gridLayout.addWidget(self.BtnGeraCpf, 1, 2, 1, 1)
        self.labelRetorno = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelRetorno.setFont(font)
        self.labelRetorno.setStyleSheet("color: green;\n"
"font: 26pt \"MS Reference Sans Serif\";")
        self.labelRetorno.setInputMethodHints(QtCore.Qt.ImhNone)
        self.labelRetorno.setText("")
        self.labelRetorno.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRetorno.setObjectName("labelRetorno")
        self.gridLayout.addWidget(self.labelRetorno, 2, 0, 1, 3)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Gera ou Valida CPF"))
        self.label_2.setText(_translate("mainWindow", "Validar CPF"))
        self.btnValidaCpf.setText(_translate("mainWindow", "Validar"))
        self.label.setText(_translate("mainWindow", "Gerar CPF"))
        self.BtnGeraCpf.setText(_translate("mainWindow", "Gerar"))
