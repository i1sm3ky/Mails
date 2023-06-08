from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignupWidget(object):
    def setupUi(self, SignupWidget):
        SignupWidget.setObjectName("SignupWidget")
        SignupWidget.resize(400, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(55)
        sizePolicy.setHeightForWidth(SignupWidget.sizePolicy().hasHeightForWidth())
        SignupWidget.setSizePolicy(sizePolicy)
        SignupWidget.setMinimumSize(QtCore.QSize(400, 550))
        SignupWidget.setMaximumSize(QtCore.QSize(400, 550))
        SignupWidget.setStyleSheet("QWidget#SignupWidget {\n"
"    background: #FFFFFF;\n"
"}")
        self.SignupLabel = QtWidgets.QLabel(SignupWidget)
        self.SignupLabel.setGeometry(QtCore.QRect(-1, 70, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.SignupLabel.setFont(font)
        self.SignupLabel.setStyleSheet("QLabel#SignupLabel {\n"
"    color: #393939;\n"
"}")
        self.SignupLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SignupLabel.setObjectName("SignupLabel")
        self.SignupDetailLabel = QtWidgets.QLabel(SignupWidget)
        self.SignupDetailLabel.setGeometry(QtCore.QRect(0, 110, 401, 20))
        self.SignupDetailLabel.setStyleSheet("QLabel#SignupDetailLabel {\n"
"    color: #7f7f7f;\n"
"}")
        self.SignupDetailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SignupDetailLabel.setObjectName("SignupDetailLabel")
        self.SignupEmailInput = QtWidgets.QLineEdit(SignupWidget)
        self.SignupEmailInput.setGeometry(QtCore.QRect(80, 240, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignupEmailInput.sizePolicy().hasHeightForWidth())
        self.SignupEmailInput.setSizePolicy(sizePolicy)
        self.SignupEmailInput.setStyleSheet("QLineEdit#SignupEmailInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupEmailInput.setObjectName("SignupEmailInput")
        self.SignupFirstNameInput = QtWidgets.QLineEdit(SignupWidget)
        self.SignupFirstNameInput.setGeometry(QtCore.QRect(80, 160, 241, 31))
        self.SignupFirstNameInput.setStyleSheet("QLineEdit#SignupFirstNameInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupFirstNameInput.setObjectName("SignupFirstNameInput")
        self.SignupLastNameInput = QtWidgets.QLineEdit(SignupWidget)
        self.SignupLastNameInput.setGeometry(QtCore.QRect(80, 200, 241, 31))
        self.SignupLastNameInput.setStyleSheet("QLineEdit#SignupLastNameInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupLastNameInput.setObjectName("SignupLastNameInput")
        self.SignupPasswordInput = QtWidgets.QLineEdit(SignupWidget)
        self.SignupPasswordInput.setGeometry(QtCore.QRect(80, 320, 241, 31))
        self.SignupPasswordInput.setStyleSheet("QLineEdit#SignupPasswordInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignupPasswordInput.setObjectName("SignupPasswordInput")
        self.SignupConfirmPasswordInput = QtWidgets.QLineEdit(SignupWidget)
        self.SignupConfirmPasswordInput.setGeometry(QtCore.QRect(80, 360, 241, 31))
        self.SignupConfirmPasswordInput.setStyleSheet("QLineEdit#SignupConfirmPasswordInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupConfirmPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignupConfirmPasswordInput.setObjectName("SignupConfirmPasswordInput")
        self.SignupPhoneNumberInput = QtWidgets.QLineEdit(SignupWidget)
        self.SignupPhoneNumberInput.setGeometry(QtCore.QRect(80, 280, 241, 31))
        self.SignupPhoneNumberInput.setStyleSheet("QLineEdit#SignupPhoneNumberInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupPhoneNumberInput.setObjectName("SignupPhoneNumberInput")
        self.SignupNextButton = QtWidgets.QPushButton(SignupWidget)
        self.SignupNextButton.setGeometry(QtCore.QRect(150, 400, 91, 21))
        self.SignupNextButton.setStyleSheet("QPushButton#SignupNextButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#SignupNextButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#SignupNextButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.SignupNextButton.setObjectName("SignupNextButton")
        self.SignupLoginFrame = QtWidgets.QFrame(SignupWidget)
        self.SignupLoginFrame.setGeometry(QtCore.QRect(28, 499, 341, 31))
        self.SignupLoginFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SignupLoginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SignupLoginFrame.setObjectName("SignupLoginFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.SignupLoginFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SignupLoginLabel = QtWidgets.QLabel(self.SignupLoginFrame)
        self.SignupLoginLabel.setStyleSheet("QLabel#SignupLoginLabel {\n"
"    padding-top: 3;\n"
"}")
        self.SignupLoginLabel.setObjectName("SignupLoginLabel")
        self.horizontalLayout.addWidget(self.SignupLoginLabel)
        self.SignupLoginButton = QtWidgets.QPushButton(self.SignupLoginFrame)
        self.SignupLoginButton.setStyleSheet("QPushButton#SignupLoginButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"    color: #1884ff;\n"
"    padding-left: 10;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton#SignupLoginButton:hover {\n"
"    color: #419aff;\n"
"}\n"
"\n"
"QPushButton#SignupLoginButton:pressed {\n"
"    color: #004cff;\n"
"}")
        self.SignupLoginButton.setObjectName("SignupLoginButton")
        self.horizontalLayout.addWidget(self.SignupLoginButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(SignupWidget)
        QtCore.QMetaObject.connectSlotsByName(SignupWidget)

    def retranslateUi(self, SignupWidget):
        _translate = QtCore.QCoreApplication.translate
        SignupWidget.setWindowTitle(_translate("SignupWidget", "Form"))
        self.SignupLabel.setText(_translate("SignupWidget", "Let\'s Get Started!"))
        self.SignupDetailLabel.setText(_translate("SignupWidget", "Create an account and get started"))
        self.SignupEmailInput.setPlaceholderText(_translate("SignupWidget", "  Email"))
        self.SignupFirstNameInput.setPlaceholderText(_translate("SignupWidget", "  First Name"))
        self.SignupLastNameInput.setPlaceholderText(_translate("SignupWidget", "  Last Name"))
        self.SignupPasswordInput.setPlaceholderText(_translate("SignupWidget", "  Password"))
        self.SignupConfirmPasswordInput.setPlaceholderText(_translate("SignupWidget", "  Confirm Password"))
        self.SignupPhoneNumberInput.setPlaceholderText(_translate("SignupWidget", "  Phone Number"))
        self.SignupNextButton.setText(_translate("SignupWidget", "Next"))
        self.SignupLoginLabel.setText(_translate("SignupWidget", "Already have an account?"))
        self.SignupLoginButton.setText(_translate("SignupWidget", "Login here"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupWidget = QtWidgets.QWidget()
    ui = Ui_SignupWidget()
    ui.setupUi(SignupWidget)
    SignupWidget.show()
    sys.exit(app.exec_())
