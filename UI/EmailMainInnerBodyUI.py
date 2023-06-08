from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmailMainInnerBodyWidget(object):
    def setupUi(self, EmailMainInnerBodyWidget):
        EmailMainInnerBodyWidget.setObjectName("EmailMainInnerBodyWidget")
        EmailMainInnerBodyWidget.resize(465, 598)
        EmailMainInnerBodyWidget.setMinimumSize(QtCore.QSize(465, 598))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EmailMainInnerBodyWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EmailBodyLayout = QtWidgets.QVBoxLayout()
        self.EmailBodyLayout.setObjectName("EmailBodyLayout")
        self.EmailBodyScrollArea = QtWidgets.QScrollArea(EmailMainInnerBodyWidget)
        self.EmailBodyScrollArea.setStyleSheet("QScrollArea#EmailBodyScrollArea {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.EmailBodyScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailBodyScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EmailBodyScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.EmailBodyScrollArea.setWidgetResizable(True)
        self.EmailBodyScrollArea.setObjectName("EmailBodyScrollArea")
        self.EmailBodyArea = QtWidgets.QWidget()
        self.EmailBodyArea.setGeometry(QtCore.QRect(0, 0, 463, 596))
        self.EmailBodyArea.setStyleSheet("QWidget#EmailBodyArea {\n"
"    background: #FFFFFF;\n"
"}")
        self.EmailBodyArea.setObjectName("EmailBodyArea")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.EmailBodyArea)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.EmailHeaderFrame = QtWidgets.QFrame(self.EmailBodyArea)
        self.EmailHeaderFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailHeaderFrame.setObjectName("EmailHeaderFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.EmailHeaderFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EmailSubjectLabel = QtWidgets.QLabel(self.EmailHeaderFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.EmailSubjectLabel.setFont(font)
        self.EmailSubjectLabel.setStyleSheet("QLabel#EmailSubjectLabel {\n"
"    color: #393939;\n"
"}")
        self.EmailSubjectLabel.setText("")
        self.EmailSubjectLabel.setObjectName("EmailSubjectLabel")
        self.verticalLayout.addWidget(self.EmailSubjectLabel)
        self.EmailFromFrame = QtWidgets.QFrame(self.EmailHeaderFrame)
        self.EmailFromFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailFromFrame.setObjectName("EmailFromFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.EmailFromFrame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.EmailFromLabel = QtWidgets.QLabel(self.EmailFromFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmailFromLabel.sizePolicy().hasHeightForWidth())
        self.EmailFromLabel.setSizePolicy(sizePolicy)
        self.EmailFromLabel.setStyleSheet("QLabel#EmailFromLabel {\n"
"    color: #a6a6a6;\n"
"}")
        self.EmailFromLabel.setObjectName("EmailFromLabel")
        self.horizontalLayout_6.addWidget(self.EmailFromLabel)
        self.EmailFromEmailLabel = QtWidgets.QLabel(self.EmailFromFrame)
        self.EmailFromEmailLabel.setStyleSheet("QLabel#EmailFromEmailLabel {\n"
"    color: #393939;\n"
"}")
        self.EmailFromEmailLabel.setText("")
        self.EmailFromEmailLabel.setObjectName("EmailFromEmailLabel")
        self.horizontalLayout_6.addWidget(self.EmailFromEmailLabel)
        self.verticalLayout.addWidget(self.EmailFromFrame)
        self.verticalLayout_8.addWidget(self.EmailHeaderFrame)
        self.EmailBodyFrame = QtWidgets.QFrame(self.EmailBodyArea)
        self.EmailBodyFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailBodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailBodyFrame.setObjectName("EmailBodyFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.EmailBodyFrame)
        self.horizontalLayout_7.setContentsMargins(0, 30, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.EmailBodyLabel = QtWidgets.QLabel(self.EmailBodyFrame)
        self.EmailBodyLabel.setText("")
        self.EmailBodyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.EmailBodyLabel.setWordWrap(True)
        self.EmailBodyLabel.setObjectName("EmailBodyLabel")
        self.horizontalLayout_7.addWidget(self.EmailBodyLabel)
        self.verticalLayout_8.addWidget(self.EmailBodyFrame)
        self.MediaFrame = QtWidgets.QFrame(self.EmailBodyArea)
        self.MediaFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MediaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MediaFrame.setObjectName("MediaFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.MediaFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8.addWidget(self.MediaFrame)
        self.AttatchedFileFrame_ = QtWidgets.QFrame(self.EmailBodyArea)
        self.AttatchedFileFrame_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AttatchedFileFrame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AttatchedFileFrame_.setObjectName("AttatchedFileFrame_")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AttatchedFileFrame_)
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AttatchedFileFrame = QtWidgets.QFrame(self.AttatchedFileFrame_)
        self.AttatchedFileFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AttatchedFileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AttatchedFileFrame.setObjectName("AttatchedFileFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.AttatchedFileFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6.addWidget(self.AttatchedFileFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_8.addWidget(self.AttatchedFileFrame_)
        self.EmailOptionsFrame = QtWidgets.QFrame(self.EmailBodyArea)
        self.EmailOptionsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailOptionsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailOptionsFrame.setObjectName("EmailOptionsFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.EmailOptionsFrame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.FavouriteMailButton = QtWidgets.QPushButton(self.EmailOptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FavouriteMailButton.sizePolicy().hasHeightForWidth())
        self.FavouriteMailButton.setSizePolicy(sizePolicy)
        self.FavouriteMailButton.setStyleSheet("QPushButton#FavouriteMailButton {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton#FavouriteMailButton:hover {\n"
"    background: #efefef;\n"
"    border: 1px solid #efefef;\n"
"}\n"
"\n"
"QPushButton#FavouriteMailButton:pressed {\n"
"    background: #cfcfcf;\n"
"    border: 1px solid #cfcfcf;\n"
"}")
        self.FavouriteMailButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/SVGs/FavouriteMailicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FavouriteMailButton.setIcon(icon)
        self.FavouriteMailButton.setIconSize(QtCore.QSize(28, 28))
        self.FavouriteMailButton.setObjectName("FavouriteMailButton")
        self.horizontalLayout_10.addWidget(self.FavouriteMailButton)
        self.DeleteMailButton = QtWidgets.QPushButton(self.EmailOptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteMailButton.sizePolicy().hasHeightForWidth())
        self.DeleteMailButton.setSizePolicy(sizePolicy)
        self.DeleteMailButton.setStyleSheet("QPushButton#DeleteMailButton {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton#DeleteMailButton:hover {\n"
"    background: #efefef;\n"
"    border: 1px solid #efefef;\n"
"}\n"
"\n"
"QPushButton#DeleteMailButton:pressed {\n"
"    background: #cfcfcf;\n"
"    border: 1px solid #cfcfcf;\n"
"}")
        self.DeleteMailButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/SVGs/DeleteMailIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteMailButton.setIcon(icon1)
        self.DeleteMailButton.setIconSize(QtCore.QSize(28, 28))
        self.DeleteMailButton.setObjectName("DeleteMailButton")
        self.horizontalLayout_10.addWidget(self.DeleteMailButton)
        self.ReplyMailButton = QtWidgets.QPushButton(self.EmailOptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReplyMailButton.sizePolicy().hasHeightForWidth())
        self.ReplyMailButton.setSizePolicy(sizePolicy)
        self.ReplyMailButton.setStyleSheet("QPushButton#ReplyMailButton {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton#ReplyMailButton:hover {\n"
"    background: #efefef;\n"
"    border: 1px solid #efefef;\n"
"}\n"
"\n"
"QPushButton#ReplyMailButton:pressed {\n"
"    background: #cfcfcf;\n"
"    border: 1px solid #cfcfcf;\n"
"}")
        self.ReplyMailButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/SVGs/ReplyMailIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReplyMailButton.setIcon(icon2)
        self.ReplyMailButton.setIconSize(QtCore.QSize(28, 28))
        self.ReplyMailButton.setObjectName("ReplyMailButton")
        self.horizontalLayout_10.addWidget(self.ReplyMailButton)
        self.ForwardMailButton = QtWidgets.QPushButton(self.EmailOptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ForwardMailButton.sizePolicy().hasHeightForWidth())
        self.ForwardMailButton.setSizePolicy(sizePolicy)
        self.ForwardMailButton.setStyleSheet("QPushButton#ForwardMailButton {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton#ForwardMailButton:hover {\n"
"    background: #efefef;\n"
"    border: 1px solid #efefef;\n"
"}\n"
"\n"
"QPushButton#ForwardMailButton:pressed {\n"
"    background: #cfcfcf;\n"
"    border: 1px solid #cfcfcf;\n"
"}")
        self.ForwardMailButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/SVGs/ForwardMailIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ForwardMailButton.setIcon(icon3)
        self.ForwardMailButton.setIconSize(QtCore.QSize(28, 28))
        self.ForwardMailButton.setObjectName("ForwardMailButton")
        self.horizontalLayout_10.addWidget(self.ForwardMailButton)
        self.verticalLayout_8.addWidget(self.EmailOptionsFrame)
        self.EmailBodyScrollArea.setWidget(self.EmailBodyArea)
        self.EmailBodyLayout.addWidget(self.EmailBodyScrollArea)
        self.verticalLayout_2.addLayout(self.EmailBodyLayout)

        self.retranslateUi(EmailMainInnerBodyWidget)
        QtCore.QMetaObject.connectSlotsByName(EmailMainInnerBodyWidget)

    def retranslateUi(self, EmailMainInnerBodyWidget):
        _translate = QtCore.QCoreApplication.translate
        EmailMainInnerBodyWidget.setWindowTitle(_translate("EmailMainInnerBodyWidget", "Form"))
        self.EmailFromLabel.setText(_translate("EmailMainInnerBodyWidget", "From: "))

import Resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmailMainInnerBodyWidget = QtWidgets.QWidget()
    ui = Ui_EmailMainInnerBodyWidget()
    ui.setupUi(EmailMainInnerBodyWidget)
    EmailMainInnerBodyWidget.show()
    sys.exit(app.exec_())
