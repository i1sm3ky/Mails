from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from UI.Backend.ClientSocket import SearchHosts
from UI.HostNamesUI import Ui_HostNameWidget

app = QtWidgets.QApplication(sys.argv)

class Ui_ChooseServerWidget(object):
    def setupUi(self, ChooseServerWidget):
        ChooseServerWidget.setObjectName("ChooseServerWidget")
        ChooseServerWidget.resize(400, 550)
        ChooseServerWidget.setMinimumSize(QtCore.QSize(400, 550))
        ChooseServerWidget.setMaximumSize(QtCore.QSize(400, 550))
        ChooseServerWidget.setStyleSheet("QWidget#ChooseServerWidget {\n"
"    background: #FFFFFF;\n"
"}")
        self.ChooseServerLabel = QtWidgets.QLabel(ChooseServerWidget)
        self.ChooseServerLabel.setGeometry(QtCore.QRect(0, 60, 401, 38))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ChooseServerLabel.setFont(font)
        self.ChooseServerLabel.setStyleSheet("QLabel#ChooseServerLabel {\n"
"    color: #393939;\n"
"}")
        self.ChooseServerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChooseServerLabel.setObjectName("ChooseServerLabel")
        self.ChooseServerScrollArea = QtWidgets.QScrollArea(ChooseServerWidget)
        self.ChooseServerScrollArea.setGeometry(QtCore.QRect(0, 139, 401, 411))
        self.ChooseServerScrollArea.setStyleSheet("QScrollArea#ChooseServerScrollArea {\n"
"    background: #FFFFFF;\n"
"}")
        self.ChooseServerScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ChooseServerScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ChooseServerScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ChooseServerScrollArea.setWidgetResizable(True)
        self.ChooseServerScrollArea.setObjectName("ChooseServerScrollArea")
        self.ChooseServerScrollAreaWidget = QtWidgets.QWidget()
        self.ChooseServerScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 401, 411))
        self.ChooseServerScrollAreaWidget.setStyleSheet("QWidget#ChooseServerScrollAreaWidget {\n"
"    background: #FFFFFF;\n"
"}")
        self.ChooseServerScrollAreaWidget.setObjectName("ChooseServerScrollAreaWidget")
        self.ChooseServerScrollAreaWidgetLayout = QtWidgets.QVBoxLayout(self.ChooseServerScrollAreaWidget)
        self.ChooseServerScrollAreaWidgetLayout.setContentsMargins(30, 0, 20, 30)
        self.ChooseServerScrollAreaWidgetLayout.setSpacing(0)
        self.ChooseServerScrollAreaWidgetLayout.setObjectName("ChooseServerScrollAreaWidgetLayout")
        self.ChooseServerScrollArea.setWidget(self.ChooseServerScrollAreaWidget)
        self.RefreshChooserServerButton = QtWidgets.QPushButton(ChooseServerWidget)
        self.RefreshChooserServerButton.setGeometry(QtCore.QRect(300, 100, 81, 21))
        self.RefreshChooserServerButton.setStyleSheet("QPushButton#RefreshChooserServerButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid #1884ff;\n"
"    border-radius: 10;\n"
"    color: #1884ff;\n"
"}\n"
"\n"
"QPushButton#RefreshChooserServerButton:hover {\n"
"    color: #419aff;\n"
"    border: 1px solid #419aff;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QPushButton#RefreshChooserServerButton:pressed {\n"
"    color: #004cff;\n"
"    border: 1px solid #004cff;\n"
"    border-radius: 10;\n"
"}")
        self.RefreshChooserServerButton.setObjectName("RefreshChooserServerButton")
        self.RefreshChooserServerButton.clicked.connect(self.RefreshHostNames)

        self.retranslateUi(ChooseServerWidget)
        QtCore.QMetaObject.connectSlotsByName(ChooseServerWidget)

    def retranslateUi(self, ChooseServerWidget):
        _translate = QtCore.QCoreApplication.translate
        ChooseServerWidget.setWindowTitle(_translate("ChooseServerWidget", "Form"))
        self.ChooseServerLabel.setText(_translate("ChooseServerWidget", "Choose a Server to connect"))
        self.RefreshChooserServerButton.setText(_translate("ChooseServerWidget", "Refresh"))
        
    def RefreshHostNames(self):
        for _ in reversed(range(self.ChooseServerScrollAreaWidgetLayout.count())): 
            self.ChooseServerScrollAreaWidgetLayout.itemAt(_).widget().setParent(None)
        
        SearchResult = SearchHosts()
        
        if SearchResult != []:
            for HostDetail in SearchResult:
                HostNameWidget = QtWidgets.QWidget()
                HostNameWidget_UI = Ui_HostNameWidget(ChooseServerWidget, HostDetail)
                HostNameWidget_UI.setupUi(HostNameWidget)
                self.ChooseServerScrollAreaWidgetLayout.addWidget(HostNameWidget)
        else:
            NoHostLabel = QtWidgets.QLabel()
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(16)
            font.setBold(False)
            font.setWeight(62)
            NoHostLabel.setFont(font)
            NoHostLabel.setStyleSheet("QLabel#NoHostLabel {\n"
"    color: #393939;\n"
"}")
            NoHostLabel.setAlignment(QtCore.Qt.AlignCenter)
            NoHostLabel.setObjectName("NoHostLabel")
            NoHostLabel.setText("No Server online currently :(")
            self.ChooseServerScrollAreaWidgetLayout.addWidget(NoHostLabel)

def Run():
    global ChooseServerWidget
    ChooseServerWidget = QtWidgets.QWidget()
    ui = Ui_ChooseServerWidget()
    ui.setupUi(ChooseServerWidget)
    ChooseServerWidget.show()
    ui.RefreshHostNames()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Run()
