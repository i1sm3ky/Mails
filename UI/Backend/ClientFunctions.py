import mysql.connector as MyConn
import re
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QInputDialog, QLineEdit

from .ClientSocket import HostConnection
from .MessageBox import ShowMessageBox
from .Cryption import Encrypt

def ConnectServer(ServerIP, ServerPort):
    global Connection
    
    Connection = HostConnection()
    Connection.ConnectHost(ServerIP, ServerPort)
    Password, Ok = QInputDialog.getText(None, "Attention", "Please enter Server Password to connect:", 
                                    QLineEdit.Password)
    if Ok and Password:
        Result = Connection.Send(Password)
        if Result == "!*Correct":
            return True
        else:
            ShowMessageBox(QMessageBox.Critical, "Incorrect Password!", "Incorrect Password, Please Enter correct password to connect.", QMessageBox.Ok)
    elif Ok and Password == '':
        ShowMessageBox(QMessageBox.Warning, "No Password Given!", "Please enter a password to connect.", QMessageBox.Ok)

def ServerLogin(EmailPhoneNumber, Password):
    Result = Connection.Send(f"CheckUser~{EmailPhoneNumber}~{Encrypt(Password)}")
    if Result[:14] == "ServerDetails~":
        MySqlDetails = Result[14:].split("~")
        MySqlDetails.insert(0, True)
        return MySqlDetails
    elif Result == "Incorrect Email!":
        ShowMessageBox(QMessageBox.Critical, "Incorrect Email/Phone Number!", "The Email/Phone Number you entered doesn't belong to any user.", QMessageBox.Ok)
    elif Result == "Incorrect Password!":
        ShowMessageBox(QMessageBox.Critical, "Incorrect Password!", "The password you entered is incorrect.", QMessageBox.Ok)

def CheckEmailValidity(Email):
    Regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(Regex, Email):
        return True
    else:
        return False
    
def CheckEmailPhoneNumberPresence(Email, PhoneNumber=''):
    if PhoneNumber == '':
        PhoneNumber = Email
    Result = Connection.Send(f'CheckUserPresence~{Email}~{PhoneNumber}')
    if Result == "1":
        return True
    elif Result == "0":
        return False

def CreateNewUser(FirstName, LastName, Email, PhoneNumber, Password, Question, Answer):
    Result = Connection.Send(f"CreateNewUser~{FirstName}~{LastName}~{Email}~{PhoneNumber}~{Encrypt(Password)}~{Question}~{Encrypt(Answer)}")
    if Result == "!*Success":
        ShowMessageBox(QMessageBox.Information, "Success!", "Account Created Successfully!", QMessageBox.Ok)
        return True
        
def GetSecurityQuestion(EmailPhoneNumber):
    Result = Connection.Send(f"GetSecurityQuestion~{EmailPhoneNumber}")
    return Result

def CheckSecurityAnswer(EmailPhoneNumber, SecurityAnswer):
    Result = Connection.Send(f"CheckSecurityAnswer~{EmailPhoneNumber}~{Encrypt(SecurityAnswer)}")
    if Result == "!*Correct":
        return True
    elif Result == "!*Incorrect":
        return False

def ChangeNewPassword(EmailPhoneNumber, NewPassword):
    Result = Connection.Send(f"ChangePassword~{EmailPhoneNumber}~{Encrypt(NewPassword)}")
    if Result == "!*Successful":
        ShowMessageBox(QMessageBox.Information, "Success!", "Password Changed Successfully!", QMessageBox.Ok)
        
def GetNumberIfEmail(EmailPhoneNumber):
    if CheckEmailValidity(EmailPhoneNumber):
        Result = Connection.Send(f"GetNumberIfEmail~{EmailPhoneNumber}")
        return Result
    else:
        return EmailPhoneNumber

def GetNameFromEmail(Email):
    Result = Connection.Send(f"GetNameFromEmail~{Email}")
    return Result

def ChangeToAlpha(Number):
    Num = "0123456789"
    Char = "abcdefghi"
    AlphaName = ""
    for Digit in Number:
        AlphaName += Char[Num.index(Digit)]
    return AlphaName


def CommitChanges(FirstName, LastName, PhoneNumber, SecurityQuestion, SecurityAnswer):
    pass
