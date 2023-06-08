from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from threading import Thread

class Ui_LogWidget(object):
    def setupUi(self, LogWidget):
        LogWidget.setObjectName("LogWidget")
        LogWidget.resize(550, 400)
        LogWidget.setMinimumSize(QtCore.QSize(550, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(LogWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LogListWidget = QtWidgets.QListWidget(LogWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LogListWidget.setFont(font)
        self.LogListWidget.setStyleSheet("QListWidget#LogListWidget {\n"
"    background: #111111;\n"
"    color: #FFFFFF;\n"
"}")
        self.LogListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LogListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LogListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LogListWidget.setMovement(QtWidgets.QListView.Static)
        self.LogListWidget.setWordWrap(True)
        self.LogListWidget.setObjectName("LogListWidget")
        self.verticalLayout.addWidget(self.LogListWidget)

        self.retranslateUi(LogWidget)
        QtCore.QMetaObject.connectSlotsByName(LogWidget)

    def retranslateUi(self, LogWidget):
        _translate = QtCore.QCoreApplication.translate
        LogWidget.setWindowTitle(_translate("LogWidget", "Form"))

def PrintLog(LogWIdget_UI):
    while True:
        try:
            with open("Config/TempLog.txt", "r") as TempLog:
                LogItem = TempLog.readline()
                if LogItem != '':
                    if LogItem != '!Disconnect':
                        LogItem_ = QListWidgetItem(LogItem)
                        LogWIdget_UI.LogListWidget.addItem(LogItem_)
                        with open("Config/TempLog.txt", "r") as TempLog:
                            TempItem = TempLog.readlines()
                        with open("Config/TempLog.txt", "w") as TempLog:
                            TempLog.writelines(TempItem[1:])
                    else:
                        LogItem_ = QListWidgetItem("Server Disconnected!")
                        LogWIdget_UI.LogListWidget.addItem(LogItem_)
                        break
        except:
            pass

def StartLog(LogWidget_UI):
    PrintLog_ = Thread(target=PrintLog, args=(LogWidget_UI,))
    PrintLog_.daemon = True
    PrintLog_.start()
    
if __name__ == "__main__":
    StartLog()
