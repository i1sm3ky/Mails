from PyQt5 import QtCore, QtGui, QtWidgets

from UI.Backend.ClientFunctions import ConnectServer
from UI.LoginUI import *

class Ui_HostNameWidget(object):
    def __init__(self, Object, HostDetails):
        self.HostName = HostDetails[0]
        self.HostIP = HostDetails[1]
        self.HostPort = HostDetails[2]
        self.Object = Object
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 46)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ConnectHostFrame = QtWidgets.QFrame(Form)
        self.ConnectHostFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ConnectHostFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ConnectHostFrame.setObjectName("ConnectHostFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ConnectHostFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HostNameLabel = QtWidgets.QLabel(self.ConnectHostFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.HostNameLabel.setFont(font)
        self.HostNameLabel.setStyleSheet("QLabel#HostNameLabel {\n"
"    color: #393939;\n"
"    padding-bottom: 10;\n"
"    padding-top: 6;\n"
"}")
        self.HostNameLabel.setObjectName("HostNameLabel")
        self.horizontalLayout.addWidget(self.HostNameLabel)
        self.ConnectHostButton = QtWidgets.QPushButton(self.ConnectHostFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectHostButton.sizePolicy().hasHeightForWidth())
        self.ConnectHostButton.setSizePolicy(sizePolicy)
        self.ConnectHostButton.setStyleSheet("QPushButton#ConnectHostButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 10;\n"
"    padding: 3;\n"
"    padding-left: 5;\n"
"    padding-right: 5;\n"
"}\n"
"\n"
"QPushButton#ConnectHostButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#ConnectHostButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.ConnectHostButton.setObjectName("ConnectHostButton")
        self.ConnectHostButton.clicked.connect(lambda : self.ConnectButtonClicked(self.HostIP, self.HostPort))
        self.horizontalLayout.addWidget(self.ConnectHostButton)
        self.verticalLayout.addWidget(self.ConnectHostFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.HostNameLabel.setText(_translate("Form", self.HostName))
        self.ConnectHostButton.setText(_translate("Form", "Connect"))

    def ConnectButtonClicked(self, HostIP, HostPort):
        if ConnectServer(HostIP, HostPort):
            self.Object.hide()
            LoginWidget.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HostNameWidget = QtWidgets.QWidget()
    ui = Ui_HostNameWidget()
    ui.setupUi(HostNameWidget)
    HostNameWidget.show()
    sys.exit(app.exec_())
