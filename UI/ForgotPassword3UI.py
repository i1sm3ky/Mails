from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgotPasswordChangePasswordWidget(object):
    def setupUi(self, ForgotPasswordChangePasswordWidget):
        ForgotPasswordChangePasswordWidget.setObjectName("ForgotPasswordChangePasswordWidget")
        ForgotPasswordChangePasswordWidget.resize(400, 550)
        ForgotPasswordChangePasswordWidget.setMinimumSize(QtCore.QSize(400, 550))
        ForgotPasswordChangePasswordWidget.setMaximumSize(QtCore.QSize(400, 550))
        self.ChangePasswordInput = QtWidgets.QLineEdit(ForgotPasswordChangePasswordWidget)
        self.ChangePasswordInput.setGeometry(QtCore.QRect(90, 300, 241, 31))
        self.ChangePasswordInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ChangePasswordInput.setStyleSheet("QLineEdit#ChangePasswordInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.ChangePasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ChangePasswordInput.setObjectName("ChangePasswordInput")
        self.ChangePasswordButton = QtWidgets.QPushButton(ForgotPasswordChangePasswordWidget)
        self.ChangePasswordButton.setGeometry(QtCore.QRect(160, 410, 91, 21))
        self.ChangePasswordButton.setStyleSheet("QPushButton#ChangePasswordButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#ChangePasswordButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#ChangePasswordButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.ChangePasswordButton.setObjectName("ChangePasswordButton")
        self.ChangePasswordLabel = QtWidgets.QLabel(ForgotPasswordChangePasswordWidget)
        self.ChangePasswordLabel.setGeometry(QtCore.QRect(0, 180, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ChangePasswordLabel.setFont(font)
        self.ChangePasswordLabel.setStyleSheet("QLabel#ChangePasswordLabel {\n"
"    color: #393939;\n"
"}")
        self.ChangePasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangePasswordLabel.setObjectName("ChangePasswordLabel")
        self.ChangePasswordDetail = QtWidgets.QLabel(ForgotPasswordChangePasswordWidget)
        self.ChangePasswordDetail.setGeometry(QtCore.QRect(0, 220, 401, 20))
        self.ChangePasswordDetail.setStyleSheet("QLabel#ChangePasswordDetail {\n"
"    color: #7f7f7f;\n"
"}")
        self.ChangePasswordDetail.setAlignment(QtCore.Qt.AlignCenter)
        self.ChangePasswordDetail.setObjectName("ChangePasswordDetail")
        self.ChangePasswordPicture = QtWidgets.QLabel(ForgotPasswordChangePasswordWidget)
        self.ChangePasswordPicture.setGeometry(QtCore.QRect(100, 50, 191, 161))
        self.ChangePasswordPicture.setText("")
        self.ChangePasswordPicture.setPixmap(QtGui.QPixmap("Images/ForgotPasswordPicture2.png"))
        self.ChangePasswordPicture.setObjectName("ChangePasswordPicture")
        self.ChangeConfirmPasswordInput = QtWidgets.QLineEdit(ForgotPasswordChangePasswordWidget)
        self.ChangeConfirmPasswordInput.setGeometry(QtCore.QRect(90, 340, 241, 31))
        self.ChangeConfirmPasswordInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ChangeConfirmPasswordInput.setStyleSheet("QLineEdit#ChangeConfirmPasswordInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.ChangeConfirmPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ChangeConfirmPasswordInput.setObjectName("ChangeConfirmPasswordInput")

        self.retranslateUi(ForgotPasswordChangePasswordWidget)
        QtCore.QMetaObject.connectSlotsByName(ForgotPasswordChangePasswordWidget)

    def retranslateUi(self, ForgotPasswordChangePasswordWidget):
        _translate = QtCore.QCoreApplication.translate
        ForgotPasswordChangePasswordWidget.setWindowTitle(_translate("ForgotPasswordChangePasswordWidget", "Form"))
        self.ChangePasswordInput.setPlaceholderText(_translate("ForgotPasswordChangePasswordWidget", "  Enter Password"))
        self.ChangePasswordButton.setText(_translate("ForgotPasswordChangePasswordWidget", "Change"))
        self.ChangePasswordLabel.setText(_translate("ForgotPasswordChangePasswordWidget", "All Done!"))
        self.ChangePasswordDetail.setText(_translate("ForgotPasswordChangePasswordWidget", "Enter your new password below"))
        self.ChangeConfirmPasswordInput.setPlaceholderText(_translate("ForgotPasswordChangePasswordWidget", "  Confirm Password"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPasswordChangePasswordWidget = QtWidgets.QWidget()
    ui = Ui_ForgotPasswordChangePasswordWidget()
    ui.setupUi(ForgotPasswordChangePasswordWidget)
    ForgotPasswordChangePasswordWidget.show()
    sys.exit(app.exec_())
