from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartingWelcomeWidget(object):
    def setupUi(self, StartingWelcomeWidget):
        StartingWelcomeWidget.setObjectName("StartingWelcomeWidget")
        StartingWelcomeWidget.resize(700, 600)
        StartingWelcomeWidget.setMinimumSize(QtCore.QSize(700, 600))
        StartingWelcomeWidget.setStyleSheet("QWidget#StartingWelcomeWidget {\n"
"    background: #cccccc;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(StartingWelcomeWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StartingWelcomeLabel = QtWidgets.QLabel(StartingWelcomeWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.StartingWelcomeLabel.setFont(font)
        self.StartingWelcomeLabel.setStyleSheet("QLabel#StartingWelcomeLabel {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 20;\n"
"    color: #393939;\n"
"}")
        self.StartingWelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StartingWelcomeLabel.setObjectName("StartingWelcomeLabel")
        self.verticalLayout.addWidget(self.StartingWelcomeLabel)

        self.retranslateUi(StartingWelcomeWidget)
        QtCore.QMetaObject.connectSlotsByName(StartingWelcomeWidget)

    def retranslateUi(self, StartingWelcomeWidget):
        _translate = QtCore.QCoreApplication.translate
        StartingWelcomeWidget.setWindowTitle(_translate("StartingWelcomeWidget", "Form"))
        self.StartingWelcomeLabel.setText(_translate("StartingWelcomeWidget", "Welcome to Mail Services!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartingWelcomeWidget = QtWidgets.QWidget()
    ui = Ui_StartingWelcomeWidget()
    ui.setupUi(StartingWelcomeWidget)
    StartingWelcomeWidget.show()
    sys.exit(app.exec_())
