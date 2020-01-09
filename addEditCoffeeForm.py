# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(120, 0, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.sort = QtWidgets.QLineEdit(Dialog)
        self.sort.setGeometry(QtCore.QRect(160, 30, 113, 20))
        self.sort.setObjectName("sort")
        self.roast = QtWidgets.QLineEdit(Dialog)
        self.roast.setGeometry(QtCore.QRect(160, 70, 113, 20))
        self.roast.setObjectName("roast")
        self.ground = QtWidgets.QCheckBox(Dialog)
        self.ground.setGeometry(QtCore.QRect(160, 110, 70, 17))
        self.ground.setText("")
        self.ground.setObjectName("ground")
        self.volume = QtWidgets.QDoubleSpinBox(Dialog)
        self.volume.setGeometry(QtCore.QRect(160, 230, 111, 22))
        self.volume.setObjectName("volume")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.taste = QtWidgets.QLineEdit(Dialog)
        self.taste.setGeometry(QtCore.QRect(160, 150, 113, 20))
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QDoubleSpinBox(Dialog)
        self.price.setGeometry(QtCore.QRect(160, 190, 111, 22))
        self.price.setObjectName("price")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sort"))
        self.label_6.setText(_translate("Dialog", "Volume"))
        self.label_2.setText(_translate("Dialog", "Roast Degree"))
        self.label_5.setText(_translate("Dialog", "Price"))
        self.label_4.setText(_translate("Dialog", "Taste"))
        self.label_3.setText(_translate("Dialog", "Ground"))
