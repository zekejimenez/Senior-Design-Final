# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Feeding.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 320)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 280, 211, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(230, 20, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setAccelerated(True)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(2000)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(230, 100, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setTabletTracking(False)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.timeEdit.setAccelerated(True)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(380, 100, 93, 71))
        self.Add.setObjectName("Add")
        self.Presets = QtWidgets.QPushButton(Dialog)
        self.Presets.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.Presets.setObjectName("Presets")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 120, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 180, 461, 91))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "How many calories per day?"))
        self.Add.setText(_translate("Dialog", "Add Time"))
        self.Presets.setText(_translate("Dialog", "Preset Options"))
        self.label_2.setText(_translate("Dialog", "Feeding Time?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
