from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgotPasswordVerifyWidget(object):
    def setupUi(self, ForgotPasswordVerifyWidget):
        ForgotPasswordVerifyWidget.setObjectName("ForgotPasswordVerifyWidget")
        ForgotPasswordVerifyWidget.resize(400, 550)
        ForgotPasswordVerifyWidget.setMinimumSize(QtCore.QSize(400, 550))
        ForgotPasswordVerifyWidget.setMaximumSize(QtCore.QSize(400, 550))
        self.ForgotPasswordAnswerInput = QtWidgets.QLineEdit(ForgotPasswordVerifyWidget)
        self.ForgotPasswordAnswerInput.setGeometry(QtCore.QRect(80, 260, 241, 31))
        self.ForgotPasswordAnswerInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ForgotPasswordAnswerInput.setStyleSheet("QLineEdit#ForgotPasswordAnswerInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.ForgotPasswordAnswerInput.setText("")
        self.ForgotPasswordAnswerInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ForgotPasswordAnswerInput.setObjectName("ForgotPasswordAnswerInput")
        self.ForgotPasswordVerifyButton = QtWidgets.QPushButton(ForgotPasswordVerifyWidget)
        self.ForgotPasswordVerifyButton.setGeometry(QtCore.QRect(150, 330, 91, 21))
        self.ForgotPasswordVerifyButton.setStyleSheet("QPushButton#ForgotPasswordVerifyButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#ForgotPasswordVerifyButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#ForgotPasswordVerifyButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.ForgotPasswordVerifyButton.setObjectName("ForgotPasswordVerifyButton")
        self.ForgotPasswordVerifyLabel = QtWidgets.QLabel(ForgotPasswordVerifyWidget)
        self.ForgotPasswordVerifyLabel.setGeometry(QtCore.QRect(-1, 110, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ForgotPasswordVerifyLabel.setFont(font)
        self.ForgotPasswordVerifyLabel.setStyleSheet("QLabel#ForgotPasswordVerifyLabel {\n"
"    color: #393939;\n"
"}")
        self.ForgotPasswordVerifyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPasswordVerifyLabel.setObjectName("ForgotPasswordVerifyLabel")
        self.ForgotPasswordVerifyDetailLabel = QtWidgets.QLabel(ForgotPasswordVerifyWidget)
        self.ForgotPasswordVerifyDetailLabel.setGeometry(QtCore.QRect(0, 140, 401, 20))
        self.ForgotPasswordVerifyDetailLabel.setStyleSheet("QLabel#ForgotPasswordVerifyDetailLabel {\n"
"    color: #7f7f7f;\n"
"}")
        self.ForgotPasswordVerifyDetailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPasswordVerifyDetailLabel.setObjectName("ForgotPasswordVerifyDetailLabel")
        self.ForgotPasswordQuestionLabel = QtWidgets.QLabel(ForgotPasswordVerifyWidget)
        self.ForgotPasswordQuestionLabel.setGeometry(QtCore.QRect(10, 220, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.ForgotPasswordQuestionLabel.setFont(font)
        self.ForgotPasswordQuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPasswordQuestionLabel.setObjectName("ForgotPasswordQuestionLabel")

        self.retranslateUi(ForgotPasswordVerifyWidget)
        QtCore.QMetaObject.connectSlotsByName(ForgotPasswordVerifyWidget)

    def retranslateUi(self, ForgotPasswordVerifyWidget):
        _translate = QtCore.QCoreApplication.translate
        ForgotPasswordVerifyWidget.setWindowTitle(_translate("ForgotPasswordVerifyWidget", "Form"))
        self.ForgotPasswordAnswerInput.setPlaceholderText(_translate("ForgotPasswordVerifyWidget", "  Answer"))
        self.ForgotPasswordVerifyButton.setText(_translate("ForgotPasswordVerifyWidget", "Verify"))
        self.ForgotPasswordVerifyLabel.setText(_translate("ForgotPasswordVerifyWidget", "Let us verify it\'s you"))
        self.ForgotPasswordVerifyDetailLabel.setText(_translate("ForgotPasswordVerifyWidget", "Answer the question below to change your password"))
        self.ForgotPasswordQuestionLabel.setText(_translate("ForgotPasswordVerifyWidget", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPasswordVerifyWidget = QtWidgets.QWidget()
    ui = Ui_ForgotPasswordVerifyWidget()
    ui.setupUi(ForgotPasswordVerifyWidget)
    ForgotPasswordVerifyWidget.show()
    sys.exit(app.exec_())
