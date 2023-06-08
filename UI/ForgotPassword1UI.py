from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgotPasswordWidget(object):
    def setupUi(self, ForgotPasswordWidget):
        ForgotPasswordWidget.setObjectName("ForgotPasswordWidget")
        ForgotPasswordWidget.resize(400, 550)
        ForgotPasswordWidget.setMinimumSize(QtCore.QSize(400, 550))
        ForgotPasswordWidget.setMaximumSize(QtCore.QSize(400, 550))
        ForgotPasswordWidget.setStyleSheet("QWidget#ForgotPasswordWidget {\n"
"    background: #FFFFFF;\n"
"}")
        self.ForgetPasswordBackgroundImage = QtWidgets.QLabel(ForgotPasswordWidget)
        self.ForgetPasswordBackgroundImage.setGeometry(QtCore.QRect(-80, 50, 431, 471))
        self.ForgetPasswordBackgroundImage.setText("")
        self.ForgetPasswordBackgroundImage.setPixmap(QtGui.QPixmap("Images/ForgotPasswordPicture.png"))
        self.ForgetPasswordBackgroundImage.setObjectName("ForgetPasswordBackgroundImage")
        self.ForgotPasswordLabel = QtWidgets.QLabel(ForgotPasswordWidget)
        self.ForgotPasswordLabel.setGeometry(QtCore.QRect(0, 250, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ForgotPasswordLabel.setFont(font)
        self.ForgotPasswordLabel.setStyleSheet("QLabel#ForgotPasswordLabel {\n"
"    color: #393939;\n"
"}")
        self.ForgotPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPasswordLabel.setObjectName("ForgotPasswordLabel")
        self.ForgotPasswordDetailLabel2 = QtWidgets.QLabel(ForgotPasswordWidget)
        self.ForgotPasswordDetailLabel2.setGeometry(QtCore.QRect(0, 290, 401, 31))
        self.ForgotPasswordDetailLabel2.setStyleSheet("QLabel#ForgotPasswordDetailLabel2 {\n"
"    color: #7f7f7f;\n"
"}")
        self.ForgotPasswordDetailLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPasswordDetailLabel2.setObjectName("ForgotPasswordDetailLabel2")
        self.ForgotPasswordDetailLabel1 = QtWidgets.QLabel(ForgotPasswordWidget)
        self.ForgotPasswordDetailLabel1.setGeometry(QtCore.QRect(0, 281, 401, 20))
        self.ForgotPasswordDetailLabel1.setStyleSheet("QLabel#ForgotPasswordDetailLabel1 {\n"
"    color: #7f7f7f;\n"
"}")
        self.ForgotPasswordDetailLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPasswordDetailLabel1.setObjectName("ForgotPasswordDetailLabel1")
        self.ForgotPasswordEmailPhoneNumberInput = QtWidgets.QLineEdit(ForgotPasswordWidget)
        self.ForgotPasswordEmailPhoneNumberInput.setGeometry(QtCore.QRect(90, 350, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ForgotPasswordEmailPhoneNumberInput.sizePolicy().hasHeightForWidth())
        self.ForgotPasswordEmailPhoneNumberInput.setSizePolicy(sizePolicy)
        self.ForgotPasswordEmailPhoneNumberInput.setStyleSheet("QLineEdit#ForgotPasswordEmailPhoneNumberInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.ForgotPasswordEmailPhoneNumberInput.setObjectName("ForgotPasswordEmailPhoneNumberInput")
        self.ForgotPasswordNextButton = QtWidgets.QPushButton(ForgotPasswordWidget)
        self.ForgotPasswordNextButton.setGeometry(QtCore.QRect(150, 410, 91, 21))
        self.ForgotPasswordNextButton.setStyleSheet("QPushButton#ForgotPasswordNextButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#ForgotPasswordNextButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#ForgotPasswordNextButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.ForgotPasswordNextButton.setObjectName("ForgotPasswordNextButton")

        self.retranslateUi(ForgotPasswordWidget)
        QtCore.QMetaObject.connectSlotsByName(ForgotPasswordWidget)

    def retranslateUi(self, ForgotPasswordWidget):
        _translate = QtCore.QCoreApplication.translate
        ForgotPasswordWidget.setWindowTitle(_translate("ForgotPasswordWidget", "Form"))
        self.ForgotPasswordLabel.setText(_translate("ForgotPasswordWidget", "Did someone forget their password?"))
        self.ForgotPasswordDetailLabel2.setText(_translate("ForgotPasswordWidget", "Just enter your password below to change your password"))
        self.ForgotPasswordDetailLabel1.setText(_translate("ForgotPasswordWidget", "That\'s ok..."))
        self.ForgotPasswordEmailPhoneNumberInput.setPlaceholderText(_translate("ForgotPasswordWidget", "  Email or Phone Number"))
        self.ForgotPasswordNextButton.setText(_translate("ForgotPasswordWidget", "Next"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPasswordWidget = QtWidgets.QWidget()
    ui = Ui_ForgotPasswordWidget()
    ui.setupUi(ForgotPasswordWidget)
    ForgotPasswordWidget.show()
    sys.exit(app.exec_())
