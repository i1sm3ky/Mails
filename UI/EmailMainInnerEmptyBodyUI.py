from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmailMainInnerEmptyBodyWidget(object):
    def setupUi(self, EmailMainInnerEmptyBodyWidget):
        EmailMainInnerEmptyBodyWidget.setObjectName("EmailMainInnerEmptyBodyWidget")
        EmailMainInnerEmptyBodyWidget.resize(465, 598)
        EmailMainInnerEmptyBodyWidget.setMinimumSize(QtCore.QSize(465, 598))
        self.verticalLayout = QtWidgets.QVBoxLayout(EmailMainInnerEmptyBodyWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EmailMainInnerEmptyBodyLabel = QtWidgets.QLabel(EmailMainInnerEmptyBodyWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.EmailMainInnerEmptyBodyLabel.setFont(font)
        self.EmailMainInnerEmptyBodyLabel.setStyleSheet("QLabel#EmailMainInnerEmptyBodyLabel {\n"
"    color: #393939;\n"
"}")
        self.EmailMainInnerEmptyBodyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailMainInnerEmptyBodyLabel.setObjectName("EmailMainInnerEmptyBodyLabel")
        self.verticalLayout.addWidget(self.EmailMainInnerEmptyBodyLabel)

        self.retranslateUi(EmailMainInnerEmptyBodyWidget)
        QtCore.QMetaObject.connectSlotsByName(EmailMainInnerEmptyBodyWidget)

    def retranslateUi(self, EmailMainInnerEmptyBodyWidget):
        _translate = QtCore.QCoreApplication.translate
        EmailMainInnerEmptyBodyWidget.setWindowTitle(_translate("EmailMainInnerEmptyBodyWidget", "Form"))
        self.EmailMainInnerEmptyBodyLabel.setText(_translate("EmailMainInnerEmptyBodyWidget", "Choose an email to open!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmailMainInnerEmptyBodyWidget = QtWidgets.QWidget()
    ui = Ui_EmailMainInnerEmptyBodyWidget()
    ui.setupUi(EmailMainInnerEmptyBodyWidget)
    EmailMainInnerEmptyBodyWidget.show()
    sys.exit(app.exec_())
