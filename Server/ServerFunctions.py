import pickle
import mysql.connector as MyConn
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtWidgets import QMessageBox
import socket
import os

from Cryption import *
from MessageBox import ShowMessageBox
from VerificationServer import VerificationServer
from CreateProfilePicture import CreateProfilePicture

def CheckServerPresence(Server_Name):
    with open("Config/ServerDetails.dat", "rb") as File:
        Flag = False
        try:
            while True:
                Result = pickle.load(File)
                if Result[0] == Server_Name:
                    Flag = True
        except:
            pass
        return Flag
    
def CreateNewServer(Server_Name):
    Password, Ok = QInputDialog.getText(None, "Attention", "Please enter MySql root Password:", 
                                    QLineEdit.Password)
    if Ok and Password:
        try:
            MySqlUserName = "DashMails_Server_" + Server_Name
            MySqlPassword = GeneratePassword()
            MySqlCredentialsDb = "DashMails_Credentials_" + Server_Name
            MySqlDataBaseName = "DashMails_Db_" + Server_Name

            with open("Config/ServerDetails.dat", "ab") as File:
                pickle.dump([Server_Name, MySqlUserName, MySqlPassword, MySqlDataBaseName, MySqlCredentialsDb], File)

            Db = MyConn.connect(host="localhost", user="root", passwd=Password)

            Cursor = Db.cursor()
            Cursor.execute(f'''CREATE USER {"'" + MySqlUserName + "'"}@'%' IDENTIFIED BY {"'" + MySqlPassword + "'"}''')
            Cursor.execute(f"""GRANT ALL ON *.* TO {"'" + MySqlUserName + "'"}@'%'""")
            Cursor.execute("FLUSH PRIVILEGES")

            Db = MyConn.connect(host=socket.gethostname(), user=MySqlUserName, passwd=MySqlPassword)

            Cursor = Db.cursor()
            Cursor.execute(f"CREATE DATABASE {MySqlCredentialsDb}")
            Cursor.execute(f"CREATE DATABASE {MySqlDataBaseName}")

            Db = MyConn.connect(host=socket.gethostname(), user=MySqlUserName, passwd=MySqlPassword, database=MySqlCredentialsDb)

            Cursor = Db.cursor()
            Cursor.execute("CREATE TABLE Credentials(Email VARCHAR(256) PRIMARY KEY, PhoneNumber VARCHAR(32), Password VARCHAR(32) NOT NULL, Salt VARCHAR(16) NOT NULL, SecurityQuestion VARCHAR(512) NOT NULL, SecurityAnswer VARCHAR(128))")        

            Db = MyConn.connect(host=socket.gethostname(), user=MySqlUserName, passwd=MySqlPassword, database=MySqlDataBaseName)

            Cursor = Db.cursor()
            Cursor.execute("CREATE TABLE UserDetails(Email VARCHAR(256) PRIMARY KEY, FirstName VARCHAR(128) NOT NULL, LastName VARCHAR(128) NOT NULL, ProfilePicture LONGBLOB NOT NULL)")
            Cursor.execute("CREATE TABLE Mails(MailID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Subject VARCHAR(512) NOT NULL, Body VARCHAR(8196) NOT NULL, MediaIDs VARCHAR(1024))")
            Cursor.execute("CREATE TABLE Media(MediaID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Content LONGBLOB NOT NULL)")

            return "Successful!"
    
        except MyConn.Error as error:
            ShowMessageBox(QMessageBox.Critical, "MySQL Error!", "An Error occured in MySQL...", QMessageBox.Ok, SubMessage=f"MySQL Error: {error}")
        
def StartServerInstance(Server_Name, Server_Password):
    with open("Config/ServerDetails.dat", "rb") as File:
        try:
            while True:
                Result = pickle.load(File)
                if Result[0] == Server_Name:
                    MySql_Details = Result[1:]
        except:
            pass
    
    VerificationServer(Server_Name, Server_Password, MySql_Details)
    
def DeleteServerInstance(Server_Name):
    Password, Ok = QInputDialog.getText(None, "Attention", "Please enter MySql root Password:", 
                                    QLineEdit.Password)
    if Ok and Password:
        try:
            with open("Config/ServerDetails.dat", "rb") as File:
                with open("Config/TempServerDetails.dat", "ab") as TempFile:
                    try:
                        while True:
                            Result = pickle.load(File)
                            if Result[0] != Server_Name:
                                pickle.dump(Result, TempFile)
                            else:
                                MySql_Details = Result
                    except:
                        pass
            os.remove("Config/ServerDetails.dat")
            os.rename("Config/TempServerDetails.dat", "Config/ServerDetails.dat")
            
            Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[1], passwd=MySql_Details[2])
            Cursor = Db.cursor()
            Cursor.execute("DROP DATABASE " + MySql_Details[3])
            Cursor.execute("DROP DATABASE " + MySql_Details[4])
            
            Db = MyConn.connect(host="localhost", user="root", passwd=Password)
            Cursor = Db.cursor()
            Cursor.execute(f"""DROP USER {"'" + MySql_Details[1] + "'"}@'%'""")
            
            ShowMessageBox(QMessageBox.Information, "Success!", "Server Deleted Successfully!", QMessageBox.Ok)
            
        except MyConn.Error as error:
            ShowMessageBox(QMessageBox.Critical, "MySQL Error!", "An Error occured in MySQL...", QMessageBox.Ok, SubMessage=f"MySQL Error: {error}")
                
def CheckUser(MySql_Details, UserDetails):
    UserDetails = UserDetails.split("~")
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("SELECT EXISTS(SELECT Email FROM Credentials WHERE Email=%s OR PhoneNumber=%s)",(UserDetails[0], UserDetails[0]))
    
    Result = [_ for _ in Cursor]
    if Result[0][0] == 1:
        Cursor.execute("SELECT Password,Salt FROM Credentials WHERE Email=%s OR PhoneNumber=%s",(UserDetails[0], UserDetails[0]))
        Result = [_ for _ in Cursor]
        if UserDetails[1] == Result[0][0]:
            return "Matched"
        else:
            return "Incorrect Password!"
    else:
        return "Incorrect Email!"
    
def CheckUserPresence(MySql_Details, UserDetail):
    UserDetails = UserDetail.split("~")
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("SELECT EXISTS(SELECT Email FROM Credentials WHERE Email=%s OR PhoneNumber=%s)",(UserDetails[0], UserDetails[0]))
    
    Result = [_ for _ in Cursor]
    return Result[0][0]
    
def CreateNewUser(MySql_Details, UserDetails):
    UserDetails = UserDetails.split("~")
    
    Salt = GeneratePassword()
    Password = UserDetails[4]
    
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("INSERT INTO Credentials (Email, PhoneNumber, Password, Salt, SecurityQuestion, SecurityAnswer) VALUES (%s,%s,%s,%s,%s,%s)",(UserDetails[2], UserDetails[3], Password, Salt, UserDetails[5], UserDetails[6],))
    Db.commit()
    
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[2])
    
    Cursor = Db.cursor()
    Cursor.execute("INSERT INTO UserDetails (Email, FirstName, LastName, ProfilePicture) VALUES (%s,%s,%s,%s)",(UserDetails[2], UserDetails[0], UserDetails[1], CreateProfilePicture(UserDetails[0] + " " + UserDetails[1])))
    Cursor.execute("CREATE TABLE " + ChangeToAlpha(UserDetails[3]) + "(MailID INT PRIMARY KEY, SendersEmail VARCHAR(256) NOT NULL, SendersName VARCHAR(256) NOT NULL, Status VARCHAR(32) NOT NULL)")
    
    Db.commit()
    return "!*Success"

def SendSecurityQuestion(MySql_Details, EmailPhoneNumber):
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("SELECT SecurityQuestion FROM Credentials WHERE Email=%s OR PhoneNumber=%s",(EmailPhoneNumber, EmailPhoneNumber))
    
    for Result in Cursor:
        return Result[0]
    
def CheckSecurityAnswer(MySql_Details, UserInputs):
    UserInputs = UserInputs.split("~")
    
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("SELECT SecurityAnswer FROM Credentials WHERE Email=%s OR PhoneNumber=%s",(UserInputs[0], UserInputs[0]))
    
    for Result in Cursor:
        if Result[0] == UserInputs[1]:
            return "!*Correct"
        else:
            return "!*Incorrect"
    
def ChangeUserPassword(MySql_Details, UserInputs):
    UserInputs = UserInputs.split("~")
    
    Salt = GeneratePassword()
    Password = UserInputs[1]
    
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("UPDATE Credentials SET Password=%s,Salt=%s WHERE Email=%s OR PhoneNumber=%s",(Password, Salt, UserInputs[0], UserInputs[0]))
    Db.commit()
    return "!*Successful"
    
def SendNumberIfEmail(MySql_Details, Email):
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[3])
    
    Cursor = Db.cursor()
    Cursor.execute("SELECT PhoneNumber FROM Credentials WHERE Email=%s",(Email,))
    
    for Result in Cursor:
        return Result[0]
    
def SendNameFromEmail(MySql_Details, Email):
    Db = MyConn.connect(host=socket.gethostname(), user=MySql_Details[0], passwd=MySql_Details[1], database=MySql_Details[2])
    
    Cursor = Db.cursor()
    Cursor.execute("SELECT FirstName,LastName FROM UserDetails WHERE Email=%s",(Email,))
    
    for Result in Cursor:
        Return = Result[0] + " " + Result[1]
        return Return
    