from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
import pickle

from UI.Backend.MessageBox import ShowMessageBox
from UI.Backend.ClientFunctions import CheckEmailValidity, CreateNewUser, CheckEmailPhoneNumberPresence, ChangeNewPassword, ServerLogin, GetSecurityQuestion, CheckSecurityAnswer, GetNumberIfEmail
import UI.Signup1UI as Signup1UI
import UI.Signup2UI as Signup2UI
import UI.ForgotPassword1UI as ForgotPassword1UI
import UI.ForgotPassword2UI as ForgotPassword2UI
import UI.ForgotPassword3UI as ForgotPassword3UI

def LoginClicked():
    Signup1Window.hide()
    LoginWidget.show()

def SignupNext():
    if Signup1_UI.SignupFirstNameInput.text() != '' and Signup1_UI.SignupLastNameInput.text() != '' and CheckEmailValidity(Signup1_UI.SignupEmailInput.text()) and Signup1_UI.SignupPhoneNumberInput.text() != '' and Signup1_UI.SignupPhoneNumberInput.text().isdigit() and Signup1_UI.SignupPasswordInput.text() != '' and Signup1_UI.SignupPasswordInput.text() == Signup1_UI.SignupConfirmPasswordInput.text():
        if CheckEmailPhoneNumberPresence(Signup1_UI.SignupEmailInput.text(), Signup1_UI.SignupPhoneNumberInput.text()) == False:
            Signup1Window.hide()
            Signup2Window.show()
        else:
            ShowMessageBox(QMessageBox.Critical, "User already exists!", "User already exists, cannot create a new account.", QMessageBox.Ok)
    elif Signup1_UI.SignupFirstNameInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter First Name.", QMessageBox.Ok)
    elif Signup1_UI.SignupLastNameInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter Last Name.", QMessageBox.Ok)
    elif Signup1_UI.SignupEmailInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter an email.", QMessageBox.Ok)
    elif CheckEmailValidity(Signup1_UI.SignupEmailInput.text()) == False:
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter a valid email.", QMessageBox.Ok)
    elif Signup1_UI.SignupPhoneNumberInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter a phone number.", QMessageBox.Ok)
    elif Signup1_UI.SignupPhoneNumberInput.text().isdigit() == False:
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter a valid phone number.", QMessageBox.Ok)
    elif Signup1_UI.SignupPasswordInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter a password.", QMessageBox.Ok)
    elif Signup1_UI.SignupConfirmPasswordInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please confirm password.", QMessageBox.Ok)
    elif Signup1_UI.SignupPasswordInput.text() != Signup1_UI.SignupConfirmPasswordInput.text():
        ShowMessageBox(QMessageBox.Warning, "Passwords Don't Match!", "Passwords don't match, Please enter same password below.", QMessageBox.Ok)

def CreateUser():
    if Signup2_UI.SignupQuestionInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter a Security question.", QMessageBox.Ok)
    elif Signup2_UI.SignupAnswerInput.text() == '':
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter an answer.", QMessageBox.Ok)
    elif Signup2_UI.SignupQuestionInput.text() != '' and Signup2_UI.SignupAnswerInput.text() != '':
        if CreateNewUser(Signup1_UI.SignupFirstNameInput.text(), Signup1_UI.SignupLastNameInput.text(), Signup1_UI.SignupEmailInput.text(), Signup1_UI.SignupPhoneNumberInput.text(), Signup1_UI.SignupPasswordInput.text(), Signup2_UI.SignupQuestionInput.text(), Signup2_UI.SignupAnswerInput.text()):
            Signup2Window.hide()
            LoginWidget.show()
        
def ForgotPasswordNext():
    if ForgotPassword1_UI.ForgotPasswordEmailPhoneNumberInput.text() != '':
        if CheckEmailPhoneNumberPresence(ForgotPassword1_UI.ForgotPasswordEmailPhoneNumberInput.text()):
            ForgotPassword2_UI.ForgotPasswordQuestionLabel.setText(GetSecurityQuestion(ForgotPassword1_UI.ForgotPasswordEmailPhoneNumberInput.text()))
            ForgotPassword1Window.hide()
            ForgotPassword2Window.show()
        else:
            ShowMessageBox(QMessageBox.Critical, "User doesn't exist!", "User doesn't exist, Please enter correct email address.", QMessageBox.Ok)
    else:
        ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter email to change your password.", QMessageBox.Ok)

def ForgotVerify():
    if ForgotPassword2_UI.ForgotPasswordAnswerInput.text() != '':
        if CheckSecurityAnswer(ForgotPassword1_UI.ForgotPasswordEmailPhoneNumberInput.text(), ForgotPassword2_UI.ForgotPasswordAnswerInput.text()):
            ForgotPassword2Window.hide()
            ForgotPassword3Window.show()
        else:
            ShowMessageBox(QMessageBox.Critical, "Answer doesn't match!", "Please enter the correct answer to change your password.", QMessageBox.Ok)
    else:
        ShowMessageBox(QMessageBox.Critical, "Empty Field!", "Please answer the above question to change your password.", QMessageBox.Ok)

def ChangePassword():
    if ForgotPassword3_UI.ChangePasswordInput.text() != '' and ForgotPassword3_UI.ChangeConfirmPasswordInput.text() == ForgotPassword3_UI.ChangePasswordInput.text():
        ChangeNewPassword(ForgotPassword1_UI.ForgotPasswordEmailPhoneNumberInput.text(), ForgotPassword3_UI.ChangePasswordInput.text())
        ForgotPassword3Window.hide()
        LoginWidget.show()
    elif ForgotPassword3_UI.ChangePasswordInput.text() == '':
        ShowMessageBox(QMessageBox.Critical, "No password given!", "This field cannot be empty, Please enter a password.", QMessageBox.Ok)
    elif ForgotPassword3_UI.ChangeConfirmPasswordInput.text() == '':
        ShowMessageBox(QMessageBox.Critical, "No password given!", "This field cannot be empty, Please re-enter the password.", QMessageBox.Ok)
    elif ForgotPassword3_UI.ChangeConfirmPasswordInput.text() != ForgotPassword3_UI.ChangePasswordInput.text():
        ShowMessageBox(QMessageBox.Warning, "Passwords don't match!", "Password don't match, Please enter the same password in both fields.", QMessageBox.Ok)

app = QtWidgets.QApplication(sys.argv)

Signup1Window = QtWidgets.QWidget()
Signup1_UI = Signup1UI.Ui_SignupWidget()
Signup1_UI.setupUi(Signup1Window)
Signup1_UI.SignupLoginButton.clicked.connect(LoginClicked)
Signup1_UI.SignupNextButton.clicked.connect(SignupNext)

Signup2Window = QtWidgets.QWidget()
Signup2_UI = Signup2UI.Ui_SignupConfirmationWidget()
Signup2_UI.setupUi(Signup2Window)
Signup2_UI.CreateAccountButton.clicked.connect(CreateUser)

ForgotPassword1Window = QtWidgets.QWidget()
ForgotPassword1_UI = ForgotPassword1UI.Ui_ForgotPasswordWidget()
ForgotPassword1_UI.setupUi(ForgotPassword1Window)
ForgotPassword1_UI.ForgotPasswordNextButton.clicked.connect(ForgotPasswordNext)

ForgotPassword2Window = QtWidgets.QWidget()
ForgotPassword2_UI = ForgotPassword2UI.Ui_ForgotPasswordVerifyWidget()
ForgotPassword2_UI.setupUi(ForgotPassword2Window)
ForgotPassword2_UI.ForgotPasswordVerifyButton.clicked.connect(ForgotVerify)

ForgotPassword3Window = QtWidgets.QWidget()
ForgotPassword3_UI = ForgotPassword3UI.Ui_ForgotPasswordChangePasswordWidget()
ForgotPassword3_UI.setupUi(ForgotPassword3Window)
ForgotPassword3_UI.ChangePasswordButton.clicked.connect(ChangePassword)

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.resize(400, 550)
        LoginWidget.setMinimumSize(QtCore.QSize(400, 550))
        LoginWidget.setMaximumSize(QtCore.QSize(400, 550))
        LoginWidget.setStyleSheet("QWidget#LoginWidget {\n"
"    background: #FFFFFF;\n"
"}")
        self.WelcomeBackLabel = QtWidgets.QLabel(LoginWidget)
        self.WelcomeBackLabel.setGeometry(QtCore.QRect(-1, 100, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeBackLabel.setFont(font)
        self.WelcomeBackLabel.setStyleSheet("QLabel#WelcomeBackLabel {\n"
"    color: #393939;\n"
"}")
        self.WelcomeBackLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeBackLabel.setObjectName("WelcomeBackLabel")
        self.LoginDetailLabel = QtWidgets.QLabel(LoginWidget)
        self.LoginDetailLabel.setGeometry(QtCore.QRect(0, 140, 401, 20))
        self.LoginDetailLabel.setStyleSheet("QLabel#LoginDetailLabel {\n"
"    color: #7f7f7f;\n"
"}")
        self.LoginDetailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginDetailLabel.setObjectName("LoginDetailLabel")
        self.LoginEmailPhoneNumberInput = QtWidgets.QLineEdit(LoginWidget)
        self.LoginEmailPhoneNumberInput.setGeometry(QtCore.QRect(90, 230, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginEmailPhoneNumberInput.sizePolicy().hasHeightForWidth())
        self.LoginEmailPhoneNumberInput.setSizePolicy(sizePolicy)
        self.LoginEmailPhoneNumberInput.setStyleSheet("QLineEdit#LoginEmailPhoneNumberInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.LoginEmailPhoneNumberInput.setObjectName("LoginEmailPhoneNumberInput")
        self.LoginPasswordInput = QtWidgets.QLineEdit(LoginWidget)
        self.LoginPasswordInput.setGeometry(QtCore.QRect(90, 280, 241, 31))
        self.LoginPasswordInput.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LoginPasswordInput.setStyleSheet("QLineEdit#LoginPasswordInput {\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 13;\n"
"}")
        self.LoginPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginPasswordInput.setObjectName("LoginPasswordInput")
        self.LoginButton = QtWidgets.QPushButton(LoginWidget)
        self.LoginButton.setGeometry(QtCore.QRect(160, 350, 91, 21))
        self.LoginButton.setStyleSheet("QPushButton#LoginButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#LoginButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#LoginButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.LoginClicked)
        self.ForgotPasswordButton = QtWidgets.QPushButton(LoginWidget)
        self.ForgotPasswordButton.setGeometry(QtCore.QRect(220, 310, 111, 21))
        self.ForgotPasswordButton.clicked.connect(self.ForgotPasswordClicked)
        self.ForgotPasswordButton.setStyleSheet("QPushButton#ForgotPasswordButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"    color: #1884ff;\n"
"    text-align: left;\n"
"    padding-top: 5;\n"
"}\n"
"\n"
"QPushButton#ForgotPasswordButton:hover {\n"
"    color: #419aff;\n"
"}\n"
"\n"
"QPushButton#ForgotPasswordButton:pressed {\n"
"    color: #004cff;\n"
"}")
        self.ForgotPasswordButton.setObjectName("ForgotPasswordButton")
        self.CreateAccountFrame = QtWidgets.QFrame(LoginWidget)
        self.CreateAccountFrame.setGeometry(QtCore.QRect(28, 499, 341, 31))
        self.CreateAccountFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CreateAccountFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CreateAccountFrame.setObjectName("CreateAccountFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.CreateAccountFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CreateAccountLabel = QtWidgets.QLabel(self.CreateAccountFrame)
        self.CreateAccountLabel.setStyleSheet("QLabel#CreateAccountLabel {\n"
"    padding-top: 3;\n"
"}")
        self.CreateAccountLabel.setObjectName("CreateAccountLabel")
        self.horizontalLayout.addWidget(self.CreateAccountLabel)
        self.SignupButton = QtWidgets.QPushButton(self.CreateAccountFrame)
        self.SignupButton.clicked.connect(self.SignupClicked)
        self.SignupButton.setStyleSheet("QPushButton#SignupButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"    color: #1884ff;\n"
"    padding-left: 10;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton#SignupButton:hover {\n"
"    color: #419aff;\n"
"}\n"
"\n"
"QPushButton#SignupButton:pressed {\n"
"    color: #004cff;\n"
"}")
        self.SignupButton.setObjectName("SignupButton")
        self.horizontalLayout.addWidget(self.SignupButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(LoginWidget)
        QtCore.QMetaObject.connectSlotsByName(LoginWidget)

    def retranslateUi(self, LoginWidget):
        _translate = QtCore.QCoreApplication.translate
        LoginWidget.setWindowTitle(_translate("LoginWidget", "Form"))
        self.WelcomeBackLabel.setText(_translate("LoginWidget", "Welcome back!"))
        self.LoginDetailLabel.setText(_translate("LoginWidget", "Enter your Email or Phone Number and Password to Log in"))
        self.LoginEmailPhoneNumberInput.setPlaceholderText(_translate("LoginWidget", "  Email or Phone Number"))
        self.LoginPasswordInput.setPlaceholderText(_translate("LoginWidget", "  Password"))
        self.LoginButton.setText(_translate("LoginWidget", "Log in"))
        self.ForgotPasswordButton.setText(_translate("LoginWidget", "Forgot Password?"))
        self.CreateAccountLabel.setText(_translate("LoginWidget", "Don\'t have an account?"))
        self.SignupButton.setText(_translate("LoginWidget", "Create an account"))
        
    def SignupClicked(self):
        LoginWidget.hide()
        Signup1Window.show()

    def ForgotPasswordClicked(self):
        LoginWidget.hide()
        ForgotPassword1Window.show()
        
    def LoginClicked(self):
        if self.LoginEmailPhoneNumberInput.text() != '' and self.LoginPasswordInput.text() != '':
            Result = ServerLogin(self.LoginEmailPhoneNumberInput.text(), self.LoginPasswordInput.text())
            try:
                if Result[0]:
                    File = open("UI/Backend/TempConfig/Results.dat", "ab")
                    pickle.dump([Result[1:], GetNumberIfEmail(self.LoginEmailPhoneNumberInput.text()), self.LoginEmailPhoneNumberInput.text()], File)
                    File.close()
                    LoginWidget.close()
            except:
                pass
        elif self.LoginEmailPhoneNumberInput.text() == '':
            ShowMessageBox(QMessageBox.Warning, "Empty Field!", "Please enter Email or Phone Number to login.", QMessageBox.Ok)
        elif self.LoginPasswordInput.text() == '':
            ShowMessageBox(QMessageBox.Warning, "Field Empty!", "Enter Password to log in.", QMessageBox.Ok)
        
LoginWidget = QtWidgets.QWidget()
ui = Ui_LoginWidget()
ui.setupUi(LoginWidget)

if __name__ == "__main__":
    LoginWidget.show()
    sys.exit(app.exec_())
