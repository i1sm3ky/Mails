from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignupConfirmationWidget(object):
    def setupUi(self, SignupConfirmationWidget):
        SignupConfirmationWidget.setObjectName("SignupConfirmationWidget")
        SignupConfirmationWidget.resize(400, 550)
        SignupConfirmationWidget.setMinimumSize(QtCore.QSize(400, 550))
        SignupConfirmationWidget.setMaximumSize(QtCore.QSize(400, 550))
        SignupConfirmationWidget.setStyleSheet("QWidget#SignupConfirmationWidget {\n"
"    background: #FFFFFF;\n"
"}")
        self.SignupAnswerInput = QtWidgets.QLineEdit(SignupConfirmationWidget)
        self.SignupAnswerInput.setGeometry(QtCore.QRect(80, 260, 241, 31))
        self.SignupAnswerInput.setStyleSheet("QLineEdit#SignupAnswerInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupAnswerInput.setText("")
        self.SignupAnswerInput.setObjectName("SignupAnswerInput")
        self.SignupConfirmationDetailLabel1 = QtWidgets.QLabel(SignupConfirmationWidget)
        self.SignupConfirmationDetailLabel1.setGeometry(QtCore.QRect(0, 110, 401, 20))
        self.SignupConfirmationDetailLabel1.setStyleSheet("QLabel#SignupConfirmationDetailLabel1 {\n"
"    color: #7f7f7f;\n"
"}")
        self.SignupConfirmationDetailLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.SignupConfirmationDetailLabel1.setObjectName("SignupConfirmationDetailLabel1")
        self.SignupQuestionInput = QtWidgets.QLineEdit(SignupConfirmationWidget)
        self.SignupQuestionInput.setGeometry(QtCore.QRect(80, 220, 241, 31))
        self.SignupQuestionInput.setStyleSheet("QLineEdit#SignupQuestionInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.SignupQuestionInput.setText("")
        self.SignupQuestionInput.setObjectName("SignupQuestionInput")
        self.SignupConfirmationLabel = QtWidgets.QLabel(SignupConfirmationWidget)
        self.SignupConfirmationLabel.setGeometry(QtCore.QRect(-1, 70, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.SignupConfirmationLabel.setFont(font)
        self.SignupConfirmationLabel.setStyleSheet("QLabel#SignupConfirmationLabel {\n"
"    color: #393939;\n"
"}")
        self.SignupConfirmationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SignupConfirmationLabel.setObjectName("SignupConfirmationLabel")
        self.CreateAccountButton = QtWidgets.QPushButton(SignupConfirmationWidget)
        self.CreateAccountButton.setGeometry(QtCore.QRect(130, 380, 131, 21))
        self.CreateAccountButton.setStyleSheet("QPushButton#CreateAccountButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#CreateAccountButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#CreateAccountButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.CreateAccountButton.setObjectName("CreateAccountButton")
        self.SignupConfirmationDetailLabel2 = QtWidgets.QLabel(SignupConfirmationWidget)
        self.SignupConfirmationDetailLabel2.setGeometry(QtCore.QRect(0, 119, 401, 31))
        self.SignupConfirmationDetailLabel2.setStyleSheet("QLabel#SignupConfirmationDetailLabel2 {\n"
"    color: #7f7f7f;\n"
"}")
        self.SignupConfirmationDetailLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.SignupConfirmationDetailLabel2.setObjectName("SignupConfirmationDetailLabel2")

        self.retranslateUi(SignupConfirmationWidget)
        QtCore.QMetaObject.connectSlotsByName(SignupConfirmationWidget)

    def retranslateUi(self, SignupConfirmationWidget):
        _translate = QtCore.QCoreApplication.translate
        SignupConfirmationWidget.setWindowTitle(_translate("SignupConfirmationWidget", "Form"))
        self.SignupAnswerInput.setPlaceholderText(_translate("SignupConfirmationWidget", "  Answer"))
        self.SignupConfirmationDetailLabel1.setText(_translate("SignupConfirmationWidget", "Set a Security question and password for when you forgot"))
        self.SignupQuestionInput.setPlaceholderText(_translate("SignupConfirmationWidget", "  Enter a question"))
        self.SignupConfirmationLabel.setText(_translate("SignupConfirmationWidget", "Just one more minute"))
        self.CreateAccountButton.setText(_translate("SignupConfirmationWidget", "Create Account"))
        self.SignupConfirmationDetailLabel2.setText(_translate("SignupConfirmationWidget", "your password"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupConfirmationWidget = QtWidgets.QWidget()
    ui = Ui_SignupConfirmationWidget()
    ui.setupUi(SignupConfirmationWidget)
    SignupConfirmationWidget.show()
    sys.exit(app.exec_())
