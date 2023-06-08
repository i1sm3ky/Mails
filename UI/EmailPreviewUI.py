from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import mysql.connector as MyConn

class Ui_EmailPreviewWidget(object):
    def __init__(self, MailDetails, MySqlDetails):
        self.MailDetails = MailDetails
        self.MySqlDetails = MySqlDetails
        
    def setupUi(self, EmailPreviewWidget):
        EmailPreviewWidget.setObjectName("EmailPreviewWidget")
        EmailPreviewWidget.resize(200, 95)
        EmailPreviewWidget.setFixedSize(QtCore.QSize(200, 95))
        self.verticalLayout = QtWidgets.QVBoxLayout(EmailPreviewWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EmailPreviewFrame = QtWidgets.QFrame(EmailPreviewWidget)
        self.EmailPreviewFrame.setStyleSheet("QFrame#EmailPreviewFrame {\n"
"    background: #e0e0e0;\n"
"    border: 2px solid #b5b5b5;\n"
"    border-radius: 10;\n"
"}\n"
"\n"
"QFrame#EmailPreviewFrame:hover {\n"
"    background: #cecece;\n"
"}")
        self.EmailPreviewFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailPreviewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailPreviewFrame.setObjectName("EmailPreviewFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.EmailPreviewFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.EmailPreviewFrame_ = QtWidgets.QFrame(self.EmailPreviewFrame)
        self.EmailPreviewFrame_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailPreviewFrame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailPreviewFrame_.setObjectName("EmailPreviewFrame_")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.EmailPreviewFrame_)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EmailPreviewDetailsFrame = QtWidgets.QFrame(self.EmailPreviewFrame_)
        self.EmailPreviewDetailsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailPreviewDetailsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailPreviewDetailsFrame.setObjectName("EmailPreviewDetailsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.EmailPreviewDetailsFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EmailPreviewProfilePicLabel = QtWidgets.QLabel(self.EmailPreviewDetailsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmailPreviewProfilePicLabel.sizePolicy().hasHeightForWidth())
        self.EmailPreviewProfilePicLabel.setSizePolicy(sizePolicy)
        self.EmailPreviewProfilePicLabel.setStyleSheet("padding-right:3;")
        self.EmailPreviewProfilePicLabel.setText("")
        self.EmailPreviewProfilePicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailPreviewProfilePicLabel.setObjectName("EmailPreviewProfilePicLabel")
        self.horizontalLayout.addWidget(self.EmailPreviewProfilePicLabel)
        self.EmailPreviewDetailsFrame_ = QtWidgets.QFrame(self.EmailPreviewDetailsFrame)
        self.EmailPreviewDetailsFrame_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailPreviewDetailsFrame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailPreviewDetailsFrame_.setObjectName("EmailPreviewDetailsFrame_")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.EmailPreviewDetailsFrame_)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.EmailPreviewSubjectLabel = QtWidgets.QLabel(self.EmailPreviewDetailsFrame_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EmailPreviewSubjectLabel.setFont(font)
        self.EmailPreviewSubjectLabel.setStyleSheet("QLabel#EmailPreviewSubjectLabel {\n"
"    color:#393939;\n"
"}")
        self.EmailPreviewSubjectLabel.setText("")
        self.EmailPreviewSubjectLabel.setObjectName("EmailPreviewSubjectLabel")
        self.verticalLayout_2.addWidget(self.EmailPreviewSubjectLabel)
        self.EmailPreviewFromLabel = QtWidgets.QLabel(self.EmailPreviewDetailsFrame_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.EmailPreviewFromLabel.setFont(font)
        self.EmailPreviewFromLabel.setStyleSheet("QLabel#EmailPreviewFromLabel {\n"
"    color:#606060;\n"
"}")
        self.EmailPreviewFromLabel.setText("")
        self.EmailPreviewFromLabel.setObjectName("EmailPreviewFromLabel")
        self.verticalLayout_2.addWidget(self.EmailPreviewFromLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.EmailPreviewDetailsFrame_)
        self.verticalLayout_3.addWidget(self.EmailPreviewDetailsFrame)
        self.EmailPreviewBodyTextEdit = QtWidgets.QTextEdit(self.EmailPreviewFrame_)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.EmailPreviewBodyTextEdit.setFont(font)
        self.EmailPreviewBodyTextEdit.setStyleSheet("QTextEdit#EmailPreviewBodyTextEdit {\n"
"    background: rgba(0,0,0,0);\n"
"    color: #606060;\n"
"}")
        self.EmailPreviewBodyTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailPreviewBodyTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EmailPreviewBodyTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EmailPreviewBodyTextEdit.setReadOnly(True)
        self.EmailPreviewBodyTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.EmailPreviewBodyTextEdit.setObjectName("EmailPreviewBodyTextEdit")
        self.verticalLayout_3.addWidget(self.EmailPreviewBodyTextEdit)
        self.verticalLayout_4.addWidget(self.EmailPreviewFrame_)
        self.verticalLayout.addWidget(self.EmailPreviewFrame)

        self.retranslateUi(EmailPreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(EmailPreviewWidget)

    def retranslateUi(self, EmailPreviewWidget):
        _translate = QtCore.QCoreApplication.translate
        EmailPreviewWidget.setWindowTitle(_translate("EmailPreviewWidget", "Form"))
        self.EmailPreviewBodyTextEdit.setHtml(_translate("EmailPreviewWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
    
    def AddPreviewDetails(self):
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        
        Cursor = Db. cursor()
        Cursor.execute("SELECT * FROM Mails WHERE MailID=%s",(self.MailDetails[0],))
        Result = Cursor.fetchone()
        
        self.EmailPreviewBodyTextEdit.setPlainText(Result[2])
        self.EmailPreviewSubjectLabel.setText(Result[1])
        self.EmailPreviewFromLabel.setText(self.MailDetails[2])
        
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        
        Cursor = Db. cursor()
        Cursor.execute("SELECT * FROM UserDetails WHERE Email=%s",(self.MailDetails[1],))
        Result = Cursor.fetchone()
        
        File = open(f"UI/Backend/TempConfig/{self.MailDetails[2].strip()}.png", "ab")
        File.write(Result[3])
        File.close()
        
        ProfilePicture = QPixmap(f"Backend/TempConfig/{self.MailDetails[2].strip()}.png")
        self.EmailPreviewProfilePicLabel.setPixmap(ProfilePicture)

import Resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmailPreviewWidget = QtWidgets.QWidget()
    ui = Ui_EmailPreviewWidget()
    ui.setupUi(EmailPreviewWidget)
    EmailPreviewWidget.show()
    sys.exit(app.exec_())
