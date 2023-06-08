from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SendWidget(object):
    def setupUi(self, SendWidget):
        SendWidget.setObjectName("SendWidget")
        SendWidget.resize(700, 600)
        SendWidget.setMinimumSize(QtCore.QSize(467, 600))
        SendWidget.setStyleSheet("QWidget#SendWidget {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 20;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SendWidget)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 20)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SendTopFrame = QtWidgets.QFrame(SendWidget)
        self.SendTopFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SendTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SendTopFrame.setObjectName("SendTopFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.SendTopFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.SendTitleLabel = QtWidgets.QLabel(self.SendTopFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.SendTitleLabel.setFont(font)
        self.SendTitleLabel.setStyleSheet("QLabel#SendTitleLabel {\n"
"    color: #393939;\n"
"}")
        self.SendTitleLabel.setObjectName("SendTitleLabel")
        self.gridLayout.addWidget(self.SendTitleLabel, 0, 2, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.ExitSendMailButton = QtWidgets.QPushButton(self.SendTopFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitSendMailButton.sizePolicy().hasHeightForWidth())
        self.ExitSendMailButton.setSizePolicy(sizePolicy)
        self.ExitSendMailButton.setStyleSheet("QPushButton#ExitSendMailButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    text-align: left;\n"
"}")
        self.ExitSendMailButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WindowIcons/SVGs/WindowIcons/CloseWindowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitSendMailButton.setIcon(icon)
        self.ExitSendMailButton.setObjectName("ExitSendMailButton")
        self.gridLayout.addWidget(self.ExitSendMailButton, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.SendTopFrame)
        self.SendDeatilsFrame = QtWidgets.QFrame(SendWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendDeatilsFrame.sizePolicy().hasHeightForWidth())
        self.SendDeatilsFrame.setSizePolicy(sizePolicy)
        self.SendDeatilsFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.SendDeatilsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SendDeatilsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SendDeatilsFrame.setObjectName("SendDeatilsFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SendDeatilsFrame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SendToFrame = QtWidgets.QFrame(self.SendDeatilsFrame)
        self.SendToFrame.setStyleSheet("QFrame#SendToFrame {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 5;\n"
"}")
        self.SendToFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SendToFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SendToFrame.setObjectName("SendToFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.SendToFrame)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SendToLabel = QtWidgets.QLabel(self.SendToFrame)
        self.SendToLabel.setStyleSheet("QLabel#SendToLabel {\n"
"    color: #393939;\n"
"}")
        self.SendToLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SendToLabel.setObjectName("SendToLabel")
        self.horizontalLayout.addWidget(self.SendToLabel)
        self.SendToInput = QtWidgets.QLineEdit(self.SendToFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendToInput.sizePolicy().hasHeightForWidth())
        self.SendToInput.setSizePolicy(sizePolicy)
        self.SendToInput.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.SendToInput.setFont(font)
        self.SendToInput.setStyleSheet("QLineEdit#SendToInput {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 5;\n"
"    color: #393939;\n"
"}\n"
"\n"
"QLineEdit#SendToInput:hover {\n"
"    border: 2px solid #1884ff;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QLineEdit#SendToInput:focus {\n"
"    border: 2px solid #1884ff;\n"
"    border-radius: 5;\n"
"}")
        self.SendToInput.setObjectName("SendToInput")
        self.horizontalLayout.addWidget(self.SendToInput)
        self.verticalLayout.addWidget(self.SendToFrame)
        self.SendSubjectFrame = QtWidgets.QFrame(self.SendDeatilsFrame)
        self.SendSubjectFrame.setStyleSheet("QFrame#SendSubjectFrame {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 5;\n"
"}")
        self.SendSubjectFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SendSubjectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SendSubjectFrame.setObjectName("SendSubjectFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SendSubjectFrame)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SendSubjectLabel = QtWidgets.QLabel(self.SendSubjectFrame)
        self.SendSubjectLabel.setStyleSheet("QLabel#SendSubjectLabel {\n"
"    color: #393939;\n"
"}")
        self.SendSubjectLabel.setObjectName("SendSubjectLabel")
        self.horizontalLayout_2.addWidget(self.SendSubjectLabel)
        self.SendSubjectInput = QtWidgets.QLineEdit(self.SendSubjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendSubjectInput.sizePolicy().hasHeightForWidth())
        self.SendSubjectInput.setSizePolicy(sizePolicy)
        self.SendSubjectInput.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.SendSubjectInput.setFont(font)
        self.SendSubjectInput.setStyleSheet("QLineEdit#SendSubjectInput {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 5;\n"
"    color: #393939;\n"
"}\n"
"\n"
"QLineEdit#SendSubjectInput:hover {\n"
"    border: 2px solid #1884ff;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QLineEdit#SendSubjectInput:focus {\n"
"    border: 2px solid #1884ff;\n"
"    border-radius: 5;\n"
"}")
        self.SendSubjectInput.setObjectName("SendSubjectInput")
        self.horizontalLayout_2.addWidget(self.SendSubjectInput)
        self.verticalLayout.addWidget(self.SendSubjectFrame)
        self.verticalLayout_2.addWidget(self.SendDeatilsFrame)
        self.SendEmailBody = QtWidgets.QTextEdit(SendWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.SendEmailBody.setFont(font)
        self.SendEmailBody.setStyleSheet("QTextEdit#SendEmailBody {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 15;\n"
"    color: #393939;\n"
"}")
        self.SendEmailBody.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SendEmailBody.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SendEmailBody.setObjectName("SendEmailBody")
        self.verticalLayout_2.addWidget(self.SendEmailBody)
        self.SendOptionsFrame = QtWidgets.QFrame(SendWidget)
        self.SendOptionsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SendOptionsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SendOptionsFrame.setObjectName("SendOptionsFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SendOptionsFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.AddAttachmentsButton = QtWidgets.QPushButton(self.SendOptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAttachmentsButton.sizePolicy().hasHeightForWidth())
        self.AddAttachmentsButton.setSizePolicy(sizePolicy)
        self.AddAttachmentsButton.setStyleSheet("QPushButton#AddAttachmentsButton {\n"
"    background: #0077ff;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 5;\n"
"    color: #FFFFFF;\n"
"    padding-top: 3;\n"
"    padding-bottom: 3;\n"
"    padding-left: 5;\n"
"    padding-right: 5;\n"
"}\n"
"\n"
"QPushButton#AddAttachmentsButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#AddAttachmentsButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/SVGs/FileIcons/PaperClipIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddAttachmentsButton.setIcon(icon1)
        self.AddAttachmentsButton.setIconSize(QtCore.QSize(20, 20))
        self.AddAttachmentsButton.setObjectName("AddAttachmentsButton")
        self.horizontalLayout_4.addWidget(self.AddAttachmentsButton)
        self.SendButton = QtWidgets.QPushButton(self.SendOptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendButton.sizePolicy().hasHeightForWidth())
        self.SendButton.setSizePolicy(sizePolicy)
        self.SendButton.setStyleSheet("QPushButton#SendButton {\n"
"    background: #0077ff;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 5;\n"
"    color: #FFFFFF;\n"
"    padding: 5;\n"
"}\n"
"\n"
"QPushButton#SendButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#SendButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}")
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout_4.addWidget(self.SendButton)
        self.verticalLayout_2.addWidget(self.SendOptionsFrame)

        self.retranslateUi(SendWidget)
        QtCore.QMetaObject.connectSlotsByName(SendWidget)

    def retranslateUi(self, SendWidget):
        _translate = QtCore.QCoreApplication.translate
        SendWidget.setWindowTitle(_translate("SendWidget", "Form"))
        self.SendTitleLabel.setText(_translate("SendWidget", "Compose a Mail"))
        self.SendToLabel.setText(_translate("SendWidget", "To : "))
        self.SendSubjectLabel.setText(_translate("SendWidget", "Subject : "))
        self.AddAttachmentsButton.setText(_translate("SendWidget", "Add Attachments"))
        self.SendButton.setText(_translate("SendWidget", "Send"))

import Resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SendWidget = QtWidgets.QWidget()
    ui = Ui_SendWidget()
    ui.setupUi(SendWidget)
    SendWidget.show()
    sys.exit(app.exec_())
