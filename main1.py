# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(10, 50, 381, 241))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.bEdit = QtWidgets.QPushButton(Form)
        self.bEdit.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.bEdit.setObjectName("bEdit")
        self.bAdd = QtWidgets.QPushButton(Form)
        self.bAdd.setGeometry(QtCore.QRect(120, 10, 75, 23))
        self.bAdd.setObjectName("bAdd")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bEdit.setText(_translate("Form", "Edit"))
        self.bAdd.setText(_translate("Form", "Add"))
