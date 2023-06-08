from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import sys

from ServerFunctions import *
import ServerLogUI
from MessageBox import ShowMessageBox

app = QtWidgets.QApplication(sys.argv)

LogWidget = QtWidgets.QWidget()
LogWidget_UI = ServerLogUI.Ui_LogWidget()
LogWidget_UI.setupUi(LogWidget)

class Ui_StartServerWindow(object):
    def setupUi(self, StartServerWindow):
        StartServerWindow.setObjectName("StartServerWindow")
        StartServerWindow.resize(400, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(StartServerWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ConfigureHostLabel = QtWidgets.QLabel(StartServerWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ConfigureHostLabel.setFont(font)
        self.ConfigureHostLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ConfigureHostLabel.setObjectName("ConfigureHostLabel")
        self.verticalLayout.addWidget(self.ConfigureHostLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.HostNameLabel = QtWidgets.QLabel(StartServerWindow)
        self.HostNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HostNameLabel.setObjectName("HostNameLabel")
        self.verticalLayout.addWidget(self.HostNameLabel)
        self.ServerName = QtWidgets.QLineEdit(StartServerWindow)
        self.ServerName.setText("")
        self.ServerName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ServerName.setObjectName("ServerName")
        self.verticalLayout.addWidget(self.ServerName)
        self.HostPasswordLabel = QtWidgets.QLabel(StartServerWindow)
        self.HostPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HostPasswordLabel.setObjectName("HostPasswordLabel")
        self.verticalLayout.addWidget(self.HostPasswordLabel)
        self.ServerPassword = QtWidgets.QLineEdit(StartServerWindow)
        self.ServerPassword.setInputMask("")
        self.ServerPassword.setText("")
        self.ServerPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ServerPassword.setObjectName("ServerPassword")
        self.verticalLayout.addWidget(self.ServerPassword)
        self.StartServerFrame = QtWidgets.QFrame(StartServerWindow)
        self.StartServerFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.StartServerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartServerFrame.setObjectName("StartServerFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.StartServerFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StartServerButton = QtWidgets.QPushButton(self.StartServerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartServerButton.sizePolicy().hasHeightForWidth())
        self.StartServerButton.setSizePolicy(sizePolicy)
        self.StartServerButton.setObjectName("StartServerButton")
        self.StartServerButton.clicked.connect(self.StartServer)
        self.horizontalLayout_3.addWidget(self.StartServerButton)
        self.verticalLayout.addWidget(self.StartServerFrame)
        self.CreateNewServerFrame = QtWidgets.QFrame(StartServerWindow)
        self.CreateNewServerFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CreateNewServerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CreateNewServerFrame.setObjectName("CreateNewServerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.CreateNewServerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CreateNewServerButton = QtWidgets.QPushButton(self.CreateNewServerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateNewServerButton.sizePolicy().hasHeightForWidth())
        self.CreateNewServerButton.setSizePolicy(sizePolicy)
        self.CreateNewServerButton.setObjectName("CreateNewServerButton")
        self.CreateNewServerButton.clicked.connect(self.CreateServer)
        self.horizontalLayout_2.addWidget(self.CreateNewServerButton)
        self.verticalLayout.addWidget(self.CreateNewServerFrame)
        self.DeleteServerFrame = QtWidgets.QFrame(StartServerWindow)
        self.DeleteServerFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DeleteServerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DeleteServerFrame.setObjectName("DeleteServerFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.DeleteServerFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeleteServerButton = QtWidgets.QPushButton(self.DeleteServerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteServerButton.sizePolicy().hasHeightForWidth())
        self.DeleteServerButton.setSizePolicy(sizePolicy)
        self.DeleteServerButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DeleteServerButton.setStyleSheet("")
        self.DeleteServerButton.setObjectName("DeleteServerButton")
        self.DeleteServerButton.clicked.connect(self.DeleteServer)
        self.horizontalLayout.addWidget(self.DeleteServerButton)
        self.verticalLayout.addWidget(self.DeleteServerFrame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(10, 2)

        self.retranslateUi(StartServerWindow)
        QtCore.QMetaObject.connectSlotsByName(StartServerWindow)

    def retranslateUi(self, StartServerWindow):
        _translate = QtCore.QCoreApplication.translate
        StartServerWindow.setWindowTitle(_translate("StartServerWindow", "Form"))
        self.ConfigureHostLabel.setText(_translate("StartServerWindow", "Configure your Server"))
        self.HostNameLabel.setText(_translate("StartServerWindow", "Enter Desired Host/Server Name"))
        self.ServerName.setPlaceholderText(_translate("StartServerWindow", "Host"))
        self.HostPasswordLabel.setText(_translate("StartServerWindow", "Enter Password to connect"))
        self.ServerPassword.setPlaceholderText(_translate("StartServerWindow", "Password"))
        self.StartServerButton.setText(_translate("StartServerWindow", "Start Server"))
        self.CreateNewServerButton.setText(_translate("StartServerWindow", "Create New Server"))
        self.DeleteServerButton.setText(_translate("StartServerWindow", "Delete Server"))
        
    def StartServer(self):
        if self.ServerName.text() != '':
            if CheckServerPresence(self.ServerName.text()):
                if self.ServerPassword.text() != '':
                    StartServerInstance(self.ServerName.text(), self.ServerPassword.text())
                    LogWidget.show()
                    ServerLogUI.StartLog(LogWidget_UI)
                else:
                    ShowMessageBox(QMessageBox.Critical, "Missing Password!", "Please enter a password to start the server.", QMessageBox.Ok, SubMessage="This password will be required by the users to join this server.")
            else:
                ShowMessageBox(QMessageBox.Information, "Server not available!", "The server you're trying to start doesn't exist.", QMessageBox.Ok)
        else:
            ShowMessageBox(QMessageBox.Critical, "Misisng Server Name!", "Please enter the server name to start it.", QMessageBox.Ok)

    def CreateServer(self):
        if self.ServerName.text() != '':
            if CheckServerPresence(self.ServerName.text()) == False:
                if CreateNewServer(self.ServerName.text()) == "Successful!":
                    if self.ServerPassword.text() != '':
                        self.StartServerInstance(self.ServerName.text(), self.ServerPassword.text())
                        LogWidget.show()
                        ServerLogUI.StartLog(LogWidget_UI)
                    else:
                        ShowMessageBox(QMessageBox.Information, "Server Created!", "Server Created Successfully!", QMessageBox.Ok, SubMessage="Please enter password and start the server to use it.")
            else:
                if self.ServerPassword.text() != '':
                    Return = ShowMessageBox(QMessageBox.Warning, "Server Already Created!", "Server has already been created! Please start the server to use it.", (QMessageBox.Yes | QMessageBox.No), QMessageBox.Yes, "Do you want to start the server?")
                    if Return == "&Yes":
                        self.StartServerInstance(self.ServerName.text(), self.ServerPassword.text())
                else:
                    Return = ShowMessageBox(QMessageBox.Critical, "Server Already Created!", "Server has already been created! Please enter a password and Start the server to use it.", QMessageBox.Ok)
        else:
            ShowMessageBox(QMessageBox.Critical, "Please Enter Server Name!", "Please enter a server name to create a new server.", QMessageBox.Ok)

    def DeleteServer(self):
        if self.ServerName.text() != '':
            if CheckServerPresence(self.ServerName.text()):
                DeleteServerInstance(self.ServerName.text())
            else:
                ShowMessageBox(QMessageBox.Information, "Server not available!", "The server you're trying to delete doesn't exist.", QMessageBox.Ok)
        else:
            ShowMessageBox(QMessageBox.Critical, "Missing Server Name!", "Please enter a server name to delete it.", QMessageBox.Ok)

def StopServer():
    LogWidget.hide()
    app.exec_()
    try:
        os.remove("Config/TempLog.txt")
    except:
        pass

def RunServer():
    StartServerWindow = QtWidgets.QWidget()
    ui = Ui_StartServerWindow()
    ui.setupUi(StartServerWindow)
    StartServerWindow.show()
    sys.exit(StopServer())

if __name__ == "__main__":
    RunServer()
