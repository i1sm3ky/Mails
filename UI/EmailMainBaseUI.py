from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMessageBox
import sys
import mysql.connector as MyConn
import shutil
import os

import UI.EmailBodyUI as EmailBodyUI
import UI.SendMailUI as SendMailUI
import UI.StartingWelcomeUI as StartingWelcomeUI
import UI.SettingsUI as SettingsUI
import UI.EmailPreviewUI as EmailPreviewUI
import UI.EmailMainInnerBodyUI as EmailMainInnerBodyUI
import UI.EmailMainInnerEmptyBodyUI as EmailMainInnerEmptyBodyUI


app = QtWidgets.QApplication(sys.argv)

StartingWelcome = QtWidgets.QWidget()
StartingWelcome_UI = StartingWelcomeUI.Ui_StartingWelcomeWidget()
StartingWelcome_UI.setupUi(StartingWelcome)

SendMail = QtWidgets.QWidget()
SendMail_UI = SendMailUI.Ui_SendWidget()
SendMail_UI.setupUi(SendMail)
SendMail_UI.AddAttachmentsButton.setEnabled(False)

EmptyBody = QtWidgets.QWidget()
EmptyBody_UI = EmailMainInnerEmptyBodyUI.Ui_EmailMainInnerEmptyBodyWidget()
EmptyBody_UI.setupUi(EmptyBody)

EmailMainBodyWidget = QtWidgets.QWidget()
EmailMainBody_UI = EmailBodyUI.Ui_EmailMainWidget()
EmailMainBody_UI.setupUi(EmailMainBodyWidget)
EmailMainBody_UI.EmailBodyLayout.addWidget(EmptyBody)

EmailBodyWidget = QtWidgets.QWidget()
EmailBodyWidget_UI = EmailMainInnerBodyUI.Ui_EmailMainInnerBodyWidget()
EmailBodyWidget_UI.setupUi(EmailBodyWidget)

Settings = QtWidgets.QWidget()
Settings_UI = SettingsUI.Ui_EmailSettingsWidget()
Settings_UI.setupUi(Settings)


class Ui_EmailBaseWidget(object):
    def __init__(self, MySqlDetails, PhoneNumber, Email):
        self.MySqlDetails = MySqlDetails
        self.PhoneNumber = PhoneNumber
        self.Email = Email

    def setupUi(self, EmailBaseWidget):
        EmailBaseWidget.setObjectName("EmailBaseWidget")
        EmailBaseWidget.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EmailBaseWidget.sizePolicy().hasHeightForWidth())
        EmailBaseWidget.setSizePolicy(sizePolicy)
        EmailBaseWidget.setMinimumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        EmailBaseWidget.setFont(font)
        EmailBaseWidget.setStyleSheet("QWidget#EmailBaseWidget {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(EmailBaseWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OptionListLayout = QtWidgets.QVBoxLayout()
        self.OptionListLayout.setObjectName("OptionListLayout")
        self.OptionListBackgroundFrame = QtWidgets.QFrame(EmailBaseWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionListBackgroundFrame.sizePolicy().hasHeightForWidth())
        self.OptionListBackgroundFrame.setSizePolicy(sizePolicy)
        self.OptionListBackgroundFrame.setMinimumSize(QtCore.QSize(50, 0))
        self.OptionListBackgroundFrame.setStyleSheet("QFrame#OptionListBackgroundFrame {\n"
"    background: #cccccc;\n"
"    border-top-left-radius: 20;\n"
"    border-bottom-left-radius: 20;\n"
"}")
        self.OptionListBackgroundFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OptionListBackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OptionListBackgroundFrame.setObjectName("OptionListBackgroundFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.OptionListBackgroundFrame)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LoggedInAsFrame = QtWidgets.QFrame(self.OptionListBackgroundFrame)
        self.LoggedInAsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LoggedInAsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoggedInAsFrame.setObjectName("LoggedInAsFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LoggedInAsFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LoggedInAsLabel = QtWidgets.QLabel(self.LoggedInAsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.LoggedInAsLabel.setFont(font)
        self.LoggedInAsLabel.setStyleSheet("QFrame#LoggedInAsLabel {\n"
"    color: #7f7f7f;\n"
"    padding-left: 7;\n"
"}")
        self.LoggedInAsLabel.setObjectName("LoggedInAsLabel")
        self.verticalLayout_2.addWidget(self.LoggedInAsLabel)
        self.LoggedInAsFrame_ = QtWidgets.QFrame(self.LoggedInAsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoggedInAsFrame_.sizePolicy().hasHeightForWidth())
        self.LoggedInAsFrame_.setSizePolicy(sizePolicy)
        self.LoggedInAsFrame_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LoggedInAsFrame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoggedInAsFrame_.setObjectName("LoggedInAsFrame_")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LoggedInAsFrame_)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LoggedInAsProfilePic = QtWidgets.QPushButton(self.LoggedInAsFrame_)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoggedInAsProfilePic.sizePolicy().hasHeightForWidth())
        self.LoggedInAsProfilePic.setSizePolicy(sizePolicy)
        self.LoggedInAsProfilePic.setStyleSheet("QPushButton#LoggedInAsProfilePic {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    text-align: right;\n"
"    padding-bottom: 6;\n"
"}")
        self.LoggedInAsProfilePic.setText("")
        self.LoggedInAsProfilePic.setIconSize(QtCore.QSize(32, 32))
        self.LoggedInAsProfilePic.setObjectName("LoggedInAsProfilePic")
        self.horizontalLayout_2.addWidget(self.LoggedInAsProfilePic)
        self._LoggedInAsFrame = QtWidgets.QFrame(self.LoggedInAsFrame_)
        self._LoggedInAsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._LoggedInAsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._LoggedInAsFrame.setObjectName("_LoggedInAsFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._LoggedInAsFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LoggedInAsName = QtWidgets.QPushButton(self._LoggedInAsFrame)
        self.LoggedInAsName.setStyleSheet("QPushButton#LoggedInAsName {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    text-align: left;\n"
"    padding-bottom: 4;\n"
"}\n"
"\n"
"QPushButton#LoggedInAsName:hover {\n"
"    color: #1884ff;\n"
"}\n"
"\n"
"QPushButton#LoggedInAsName:pressed {\n"
"    color: #004cff;\n"
"}")
        self.LoggedInAsName.setText("")
        self.LoggedInAsName.setObjectName("LoggedInAsName")
        self.verticalLayout.addWidget(self.LoggedInAsName)
        self.LoggedInAsEmail = QtWidgets.QPushButton(self._LoggedInAsFrame)
        self.LoggedInAsEmail.setStyleSheet("QPushButton#LoggedInAsEmail {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #7f7f7f;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton#LoggedInAsEmail:hover {\n"
"    color: #1884ff;\n"
"}\n"
"\n"
"QPushButton#LoggedInAsEmail:pressed {\n"
"    color: #004cff;\n"
"}")
        self.LoggedInAsEmail.setText("")
        self.LoggedInAsEmail.setObjectName("LoggedInAsEmail")
        self.verticalLayout.addWidget(self.LoggedInAsEmail)
        self.horizontalLayout_2.addWidget(self._LoggedInAsFrame)
        self.verticalLayout_2.addWidget(self.LoggedInAsFrame_)
        self.verticalLayout_3.addWidget(self.LoggedInAsFrame)
        self.NewMailButtonFrame = QtWidgets.QFrame(self.OptionListBackgroundFrame)
        self.NewMailButtonFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NewMailButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NewMailButtonFrame.setObjectName("NewMailButtonFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.NewMailButtonFrame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NewMailButton = QtWidgets.QPushButton(self.NewMailButtonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewMailButton.sizePolicy().hasHeightForWidth())
        self.NewMailButton.setSizePolicy(sizePolicy)
        self.NewMailButton.setMinimumSize(QtCore.QSize(0, 25))
        self.NewMailButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.NewMailButton.setFont(font)
        self.NewMailButton.setStyleSheet("QPushButton#NewMailButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 7;\n"
"}\n"
"\n"
"QPushButton#NewMailButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#NewMailButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.NewMailButton.setObjectName("NewMailButton")
        self.NewMailButton.clicked.connect(self.NewMailClicked)
        self.horizontalLayout_3.addWidget(self.NewMailButton)
        self.verticalLayout_3.addWidget(self.NewMailButtonFrame)
        self.OptionListFrame = QtWidgets.QFrame(self.OptionListBackgroundFrame)
        self.OptionListFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OptionListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OptionListFrame.setObjectName("OptionListFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.OptionListFrame)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.OptionListLayout_ = QtWidgets.QGridLayout()
        self.OptionListLayout_.setObjectName("OptionListLayout_")
        self.InboxMailCount = QtWidgets.QPushButton(self.OptionListFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InboxMailCount.sizePolicy().hasHeightForWidth())
        self.InboxMailCount.setSizePolicy(sizePolicy)
        self.InboxMailCount.setMaximumSize(QtCore.QSize(16, 16))
        self.InboxMailCount.setStyleSheet("QPushButton#InboxMailCount {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid rgba(0, 0, 0, 0);\n"
"    border-radius: 8;\n"
"}")
        self.InboxMailCount.setText("")
        self.InboxMailCount.setObjectName("InboxMailCount")
        self.OptionListLayout_.addWidget(self.InboxMailCount, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.OptionListLayout_.addItem(spacerItem1, 1, 0, 1, 1)
        self.StarredMailButton = QtWidgets.QPushButton(self.OptionListFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.StarredMailButton.setFont(font)
        self.StarredMailButton.setStyleSheet("QPushButton#StarredMailButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-left: 5;\n"
"    padding-bottom: 7;\n"
"}\n"
"\n"
"QPushButton#StarredMailButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#StarredMailButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Disabled Icons/SVGs/Disabled/StarredMailicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StarredMailButton.setIcon(icon3)
        self.StarredMailButton.setIconSize(QtCore.QSize(36, 36))
        self.StarredMailButton.setObjectName("StarredMailButton")
        self.StarredMailButton.clicked.connect(self.StarredMailClicked)
        self.OptionListLayout_.addWidget(self.StarredMailButton, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem2, 4, 1, 1, 1)
        self.SettingsButton = QtWidgets.QPushButton(self.OptionListFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setStyleSheet("QPushButton#SettingsButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-left: 11;\n"
"    padding-top: 7;\n"
"    padding-bottom: 12;\n"
"}\n"
"\n"
"QPushButton#SettingsButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#SettingsButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Disabled Icons/SVGs/Disabled/SettingsIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsButton.setIcon(icon4)
        self.SettingsButton.setIconSize(QtCore.QSize(24, 24))
        self.SettingsButton.setObjectName("SettingsButton")
        self.SettingsButton.clicked.connect(self.SettingsClicked)
        self.OptionListLayout_.addWidget(self.SettingsButton, 11, 1, 1, 1)
        self.TrashMailButton = QtWidgets.QPushButton(self.OptionListFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.TrashMailButton.setFont(font)
        self.TrashMailButton.setStyleSheet("QPushButton#TrashMailButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-right: 8;\n"
"    padding-top: 8;\n"
"    padding-bottom: 10;\n"
"}\n"
"\n"
"QPushButton#TrashMailButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#TrashMailButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Disabled Icons/SVGs/Disabled/TrashIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TrashMailButton.setIcon(icon5)
        self.TrashMailButton.setIconSize(QtCore.QSize(24, 24))
        self.TrashMailButton.setObjectName("TrashMailButton")
        self.TrashMailButton.clicked.connect(self.TrashMailClicked)
        self.OptionListLayout_.addWidget(self.TrashMailButton, 9, 1, 1, 1)
        self.DraftsMailCount = QtWidgets.QPushButton(self.OptionListFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DraftsMailCount.sizePolicy().hasHeightForWidth())
        self.DraftsMailCount.setSizePolicy(sizePolicy)
        self.DraftsMailCount.setMaximumSize(QtCore.QSize(16, 16))
        self.DraftsMailCount.setStyleSheet("QPushButton#DraftsMailCount {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid rgba(0, 0, 0, 0);\n"
"    border-radius: 8;\n"
"}")
        self.DraftsMailCount.setText("")
        self.DraftsMailCount.setObjectName("DraftsMailCount")
        self.OptionListLayout_.addWidget(self.DraftsMailCount, 7, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem3, 0, 1, 1, 1)
        self.InboxMailButton = QtWidgets.QPushButton(self.OptionListFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.InboxMailButton.setFont(font)
        self.InboxMailButton.setStyleSheet("QPushButton#InboxMailButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-right: 5;\n"
"    padding-top: 2;\n"
"    padding-bottom: 7;\n"
"}\n"
"\n"
"QPushButton#InboxMailButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#InboxMailButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Disabled Icons/SVGs/Disabled/InboxIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InboxMailButton.setIcon(icon6)
        self.InboxMailButton.setIconSize(QtCore.QSize(32, 32))
        self.InboxMailButton.setObjectName("InboxMailButton")
        self.InboxMailButton.clicked.connect(self.InboxMailClicked)
        self.OptionListLayout_.addWidget(self.InboxMailButton, 1, 1, 1, 1)
        self.SentMailButton = QtWidgets.QPushButton(self.OptionListFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.SentMailButton.setFont(font)
        self.SentMailButton.setStyleSheet("QPushButton#SentMailButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-right: 9;\n"
"    padding-top: 1;\n"
"    padding-bottom: 7;\n"
"}\n"
"\n"
"QPushButton#SentMailButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#SentMailButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Disabled Icons/SVGs/Disabled/SentIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SentMailButton.setIcon(icon7)
        self.SentMailButton.setIconSize(QtCore.QSize(24, 24))
        self.SentMailButton.setObjectName("SentMailButton")
        self.SentMailButton.clicked.connect(self.SentMailClicked)
        self.OptionListLayout_.addWidget(self.SentMailButton, 5, 1, 1, 1)
        self.DraftsMailButton = QtWidgets.QPushButton(self.OptionListFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.DraftsMailButton.setFont(font)
        self.DraftsMailButton.setStyleSheet("QPushButton#DraftsMailButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-top: 8;\n"
"    padding-bottom: 12;\n"
"}\n"
"\n"
"QPushButton#DraftsMailButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#DraftsMailButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Disabled Icons/SVGs/Disabled/DraftIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DraftsMailButton.setIcon(icon8)
        self.DraftsMailButton.setIconSize(QtCore.QSize(24, 24))
        self.DraftsMailButton.setObjectName("DraftsMailButton")
        self.DraftsMailButton.clicked.connect(self.DraftMailClicked)
        self.OptionListLayout_.addWidget(self.DraftsMailButton, 7, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.OptionListLayout_.addItem(spacerItem4, 1, 3, 1, 1)
        self.SettingsAlertIndicator = QtWidgets.QPushButton(self.OptionListFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SettingsAlertIndicator.sizePolicy().hasHeightForWidth())
        self.SettingsAlertIndicator.setSizePolicy(sizePolicy)
        self.SettingsAlertIndicator.setMaximumSize(QtCore.QSize(16, 16))
        self.SettingsAlertIndicator.setStyleSheet("QPushButton#SettingsAlertIndicator {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: 1px solid rgba(0, 0, 0, 0);\n"
"    border-radius: 8;\n"
"}")
        self.SettingsAlertIndicator.setText("")
        self.SettingsAlertIndicator.setObjectName("SettingsAlertIndicator")
        self.OptionListLayout_.addWidget(self.SettingsAlertIndicator, 11, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem5, 8, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem6, 10, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem7, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.OptionListLayout_.addItem(spacerItem9, 12, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.OptionListLayout_)
        self.verticalLayout_3.addWidget(self.OptionListFrame)
        self.GroupScrollArea = QtWidgets.QScrollArea(self.OptionListBackgroundFrame)
        self.GroupScrollArea.setStyleSheet("QScrollArea#GroupScrollArea {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.GroupScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GroupScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GroupScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GroupScrollArea.setWidgetResizable(True)
        self.GroupScrollArea.setObjectName("GroupScrollArea")
        self.GroupScrollArea.setEnabled(False)
        self.GroupScrollAreaWidget = QtWidgets.QWidget()
        self.GroupScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 174, 216))
        self.GroupScrollAreaWidget.setStyleSheet("QWidget#GroupScrollAreaWidget {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.GroupScrollAreaWidget.setObjectName("GroupScrollAreaWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.GroupScrollAreaWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.GroupScrollFrame_ = QtWidgets.QFrame(self.GroupScrollAreaWidget)
        self.GroupScrollFrame_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GroupScrollFrame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GroupScrollFrame_.setObjectName("GroupScrollFrame_")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.GroupScrollFrame_)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.frame = QtWidgets.QFrame(self.GroupScrollFrame_)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AllGroupButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AllGroupButton.setFont(font)
        self.AllGroupButton.setStyleSheet("QPushButton#AllGroupButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton#AllGroupButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#AllGroupButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Images/AllIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AllGroupButton.setIcon(icon9)
        self.AllGroupButton.setObjectName("AllGroupButton")
        self.verticalLayout_6.addWidget(self.AllGroupButton)
        self.FamilyGroupButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.FamilyGroupButton.setFont(font)
        self.FamilyGroupButton.setStyleSheet("QPushButton#FamilyGroupButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    text-align: left;\n"
"    padding-top: 20;\n"
"}\n"
"\n"
"QPushButton#FamilyGroupButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#FamilyGroupButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Images/Family.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FamilyGroupButton.setIcon(icon10)
        self.FamilyGroupButton.setObjectName("FamilyGroupButton")
        self.verticalLayout_6.addWidget(self.FamilyGroupButton)
        self.FriendsGroupButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.FriendsGroupButton.setFont(font)
        self.FriendsGroupButton.setStyleSheet("QPushButton#FriendsGroupButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    text-align: left;\n"
"    padding-top: 20;\n"
"}\n"
"\n"
"QPushButton#FriendsGroupButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#FriendsGroupButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Images/Work.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FriendsGroupButton.setIcon(icon11)
        self.FriendsGroupButton.setObjectName("FriendsGroupButton")
        self.verticalLayout_6.addWidget(self.FriendsGroupButton)
        self.ClientsGroupButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.ClientsGroupButton.setFont(font)
        self.ClientsGroupButton.setStyleSheet("QPushButton#ClientsGroupButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    text-align: left;\n"
"    padding-top: 20;\n"
"}\n"
"\n"
"QPushButton#ClientsGroupButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#ClientsGroupButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Images/Client.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClientsGroupButton.setIcon(icon12)
        self.ClientsGroupButton.setObjectName("ClientsGroupButton")
        self.verticalLayout_6.addWidget(self.ClientsGroupButton)
        self.horizontalLayout_4.addWidget(self.frame)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout_5.addWidget(self.GroupScrollFrame_)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.GroupScrollArea.setWidget(self.GroupScrollAreaWidget)
        self.verticalLayout_3.addWidget(self.GroupScrollArea)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 4)
        self.OptionListLayout.addWidget(self.OptionListBackgroundFrame)
        self.horizontalLayout.addLayout(self.OptionListLayout)
        self.EmailMainBodyLayout = QtWidgets.QVBoxLayout()
        self.EmailMainBodyLayout.setObjectName("EmailMainBodyLayout")
        self.horizontalLayout.addLayout(self.EmailMainBodyLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 7)
        self.EmailMainBodyLayout.addWidget(StartingWelcome)

        self.retranslateUi(EmailBaseWidget)
        QtCore.QMetaObject.connectSlotsByName(EmailBaseWidget)

    def retranslateUi(self, EmailBaseWidget):
        _translate = QtCore.QCoreApplication.translate
        EmailBaseWidget.setWindowTitle(_translate("EmailBaseWidget", "Form"))
        self.LoggedInAsLabel.setText(_translate("EmailBaseWidget", "Logged in as:"))
        self.NewMailButton.setText(_translate("EmailBaseWidget", "New Mail"))
        self.StarredMailButton.setText(_translate("EmailBaseWidget", "Starred"))
        self.SettingsButton.setText(_translate("EmailBaseWidget", "  Settings"))
        self.TrashMailButton.setText(_translate("EmailBaseWidget", "  Trash"))
        self.InboxMailButton.setText(_translate("EmailBaseWidget", "  Inbox"))
        self.SentMailButton.setText(_translate("EmailBaseWidget", "  Sent"))
        self.DraftsMailButton.setText(_translate("EmailBaseWidget", "  Drafts"))
        self.AllGroupButton.setText(_translate("EmailBaseWidget", "  All"))
        self.FamilyGroupButton.setText(_translate("EmailBaseWidget", "  Family"))
        self.FriendsGroupButton.setText(_translate("EmailBaseWidget", "  Work"))
        self.ClientsGroupButton.setText(_translate("EmailBaseWidget", "  Clients"))
        
    def DeleteMail(self, MailID):
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        from UI.Backend.ClientFunctions import ChangeToAlpha
        
        Cursor = Db. cursor()
        Cursor.execute(f"UPDATE {ChangeToAlpha(self.PhoneNumber)} SET Status='Trash' WHERE MailID={MailID}")
        Db.commit()
        self.TrashMailClicked()
        
    def StarMail(self, MailID):
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        from UI.Backend.ClientFunctions import ChangeToAlpha
        
        Cursor = Db. cursor()
        Cursor.execute(f"UPDATE {ChangeToAlpha(self.PhoneNumber)} SET Status='Starred' WHERE MailID={MailID}")
        Db.commit()
        self.StarredMailClicked()
        
    def ReplyMail(self, MailID):
        self.NewMailClicked()
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        from UI.Backend.ClientFunctions import ChangeToAlpha, GetNameFromEmail, GetNumberIfEmail
        from UI.Backend.MessageBox import ShowMessageBox
        
        Cursor = Db. cursor(buffered=True)
        Cursor.execute("SELECT * FROM Mails WHERE MailID=%s",(MailID,))
        Result = Cursor.fetchone()
        SendMail_UI.SendSubjectInput.setText()
        SendMail_UI.SendToInput.setText()
    
    def ForwardMail(self, MailID):
        RecieverEmail, Ok = QInputDialog.getText(None, "Enter email!", "Please enter email to forward mail:")
        if Ok and RecieverEmail:
            Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
            from UI.Backend.ClientFunctions import ChangeToAlpha, GetNameFromEmail, GetNumberIfEmail
            from UI.Backend.MessageBox import ShowMessageBox
            
            Cursor = Db. cursor(buffered=True)
            Cursor.execute("SELECT * FROM Mails WHERE MailID=%s",(MailID,))
            Result = Cursor.fetchone()
        
            Cursor = Db.cursor(buffered=True)
            Cursor.execute("INSERT INTO Mails (Subject,Body) VALUES(%s,%s)",(Result[1], Result[2]))
            Cursor.execute("SELECT MailID from Mails ORDER BY MailID DESC")
            MailID = Cursor.fetchone()[0]
            Cursor.execute(f'''INSERT INTO {ChangeToAlpha(self.PhoneNumber)} VALUES({int(MailID)},{"'" + self.Email + "'"},{"'" + GetNameFromEmail(self.Email) + "'"},{"'" + "Sent" + "'"})''')
            Cursor.execute(f'''INSERT INTO {ChangeToAlpha(GetNumberIfEmail(SendMail_UI.SendToInput.text()))} VALUES({int(MailID)},{"'" + self.Email + "'"},{"'" + GetNameFromEmail(self.Email) + "'"},{"'" + "Inbox" + "'"})''')
            Db.commit()
            ShowMessageBox(QMessageBox.Information, "Mail Forwarded!", "Mail forwarded successfully!", QMessageBox.Ok)
        
    def OpenMail(self, MailDetails):
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        
        Cursor = Db. cursor(buffered=True)
        Cursor.execute("SELECT * FROM Mails WHERE MailID=%s",(MailDetails[0],))
        Result = Cursor.fetchone()
        
        EmailBodyWidget_UI.EmailBodyLabel.setText(Result[2])
        EmailBodyWidget_UI.EmailSubjectLabel.setText(Result[1])
        EmailBodyWidget_UI.EmailFromEmailLabel.setText(MailDetails[1])
        
        EmailMainBody_UI.EmailBodyLayout.removeWidget(EmptyBody)
        EmailMainBody_UI.EmailBodyLayout.addWidget(EmailBodyWidget)
        
        EmailBodyWidget_UI.DeleteMailButton.clicked.connect(lambda : self.DeleteMail(MailDetails[0]))
        EmailBodyWidget_UI.FavouriteMailButton.clicked.connect(lambda : self.StarMail(MailDetails[0]))
        EmailBodyWidget_UI.ForwardMailButton.clicked.connect(lambda : self.ForwardMail(MailDetails[0]))
        EmailBodyWidget_UI.ReplyMailButton.clicked.connect(lambda : self.ReplyMail(MailDetails[0]))
        
    def AddEmailPreviews(self, Status):
        for _ in reversed(range(EmailMainBody_UI.EmailPreviewScrollAreaWidgetLayout.count())): 
            EmailMainBody_UI.EmailPreviewScrollAreaWidgetLayout.itemAt(_).widget().setParent(None)
        
        Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
        
        from UI.Backend.ClientFunctions import ChangeToAlpha
        Cursor = Db. cursor()
        Cursor.execute(f'''SELECT * FROM {ChangeToAlpha(self.PhoneNumber)} WHERE Status={"'" + Status + "'"} ORDER BY MailID DESC''')
        
        Result = Cursor.fetchall()
        for Result_ in Result:
            EmailPreviewWidget = QtWidgets.QWidget()
            EmailPreview_UI = EmailPreviewUI.Ui_EmailPreviewWidget(Result_, self.MySqlDetails)
            EmailPreview_UI.setupUi(EmailPreviewWidget)
            EmailPreview_UI.AddPreviewDetails()
            EmailPreviewWidget.mouseReleaseEvent = lambda event, arg=Result_ : self.OpenMail(arg)
            EmailMainBody_UI.EmailPreviewScrollAreaWidgetLayout.addWidget(EmailPreviewWidget)
            
    def SendMailClicked(self):
        from UI.Backend.ClientFunctions import CheckEmailValidity, CheckEmailPhoneNumberPresence
        from UI.Backend.MessageBox import ShowMessageBox
        if SendMail_UI.SendEmailBody.toPlainText() != '' and SendMail_UI.SendToInput.text() != '' and SendMail_UI.SendSubjectInput.text() != '' and CheckEmailValidity(SendMail_UI.SendToInput.text()) and CheckEmailPhoneNumberPresence(SendMail_UI.SendToInput.text()):
            Db = MyConn.connect(host=self.MySqlDetails[0], user=self.MySqlDetails[1], passwd=self.MySqlDetails[2], db=self.MySqlDetails[3])
            from UI.Backend.ClientFunctions import ChangeToAlpha, GetNameFromEmail, GetNumberIfEmail
            
            Cursor = Db.cursor(buffered=True)
            Cursor.execute("INSERT INTO Mails (Subject,Body) VALUES(%s,%s)",(SendMail_UI.SendSubjectInput.text(), SendMail_UI.SendEmailBody.toPlainText()))
            Cursor.execute("SELECT MailID from Mails ORDER BY MailID DESC")
            MailID = Cursor.fetchone()[0]
            Cursor.execute(f'''INSERT INTO {ChangeToAlpha(self.PhoneNumber)} VALUES({int(MailID)},{"'" + self.Email + "'"},{"'" + GetNameFromEmail(self.Email) + "'"},{"'" + "Sent" + "'"})''')
            Cursor.execute(f'''INSERT INTO {ChangeToAlpha(GetNumberIfEmail(SendMail_UI.SendToInput.text()))} VALUES({int(MailID)},{"'" + self.Email + "'"},{"'" + GetNameFromEmail(self.Email) + "'"},{"'" + "Inbox" + "'"})''')
            Db.commit()
            ShowMessageBox(QMessageBox.Information, "Mail Sent!", "Mail sent successfully!", QMessageBox.Ok)
            SendMail_UI.SendEmailBody.clear()
            SendMail_UI.SendToInput.clear()
            SendMail_UI.SendSubjectInput.clear()
        elif CheckEmailValidity(SendMail_UI.SendToInput.text()) == False:
            ShowMessageBox(QMessageBox.Critical, "Incorrect Email!", "Please Enter a correct email address!", QMessageBox.Ok)
        elif CheckEmailPhoneNumberPresence(SendMail_UI.SendToInput.text()) == False:
            ShowMessageBox(QMessageBox.Critical, "Incorrect Email!", "The email you entered doesn't belong to any user!", QMessageBox.Ok)
        elif SendMail_UI.SendToInput.text() == '':
            ShowMessageBox(QMessageBox.Critical, "Empty Field!", "Please enter the email address where you want to send the mail!", QMessageBox.Ok)
        elif SendMail_UI.SendSubjectInput.text() == '':
            ShowMessageBox(QMessageBox.Critical, "Empty Field!", "Please enter a subject to send mail!", QMessageBox.Ok)
        elif SendMail_UI.SendEmailBody.toPlainText() == '':
            ShowMessageBox(QMessageBox.Critical, "Empty Field!", "Please enter the body of email to send!", QMessageBox.Ok)
        
    def NewMailClicked(self):
        StartingWelcome.setParent(None)
        EmailMainBodyWidget.setParent(None)
        Settings.setParent(None)
        self.EmailMainBodyLayout.addWidget(SendMail)
        SendMail_UI.SendButton.clicked.connect(self.SendMailClicked)
        
    def InboxMailClicked(self):
        StartingWelcome.setParent(None)
        SendMail.setParent(None)
        Settings.setParent(None)
        EmailMainBodyWidget.setParent(None)
        self.AddEmailPreviews("Inbox")
        self.EmailMainBodyLayout.addWidget(EmailMainBodyWidget)
        
    def StarredMailClicked(self):
        StartingWelcome.setParent(None)
        SendMail.setParent(None)
        Settings.setParent(None)
        EmailMainBodyWidget.setParent(None)
        self.AddEmailPreviews("Starred")
        self.EmailMainBodyLayout.addWidget(EmailMainBodyWidget)
        
    def SentMailClicked(self):
        StartingWelcome.setParent(None)
        SendMail.setParent(None)
        Settings.setParent(None)
        EmailMainBodyWidget.setParent(None)
        self.AddEmailPreviews("Sent")
        self.EmailMainBodyLayout.addWidget(EmailMainBodyWidget)
        
    def DraftMailClicked(self):
        StartingWelcome.setParent(None)
        SendMail.setParent(None)
        Settings.setParent(None)
        EmailMainBodyWidget.setParent(None)
        self.AddEmailPreviews("Draft")
        self.EmailMainBodyLayout.addWidget(EmailMainBodyWidget)
        
    def TrashMailClicked(self):
        StartingWelcome.setParent(None)
        SendMail.setParent(None)
        Settings.setParent(None)
        EmailMainBodyWidget.setParent(None)
        self.AddEmailPreviews("Trash")
        self.EmailMainBodyLayout.addWidget(EmailMainBodyWidget)
        
    def SettingsClicked(self):
        StartingWelcome.setParent(None)
        SendMail.setParent(None)
        EmailMainBodyWidget.setParent(None)
        self.EmailMainBodyLayout.addWidget(Settings)
    
import Resource_rc

def QuitApp():
    try:
        shutil.rmtree("UI/Backend/TempConfig")
        os.makedirs("UI/Backend/TempConfig")
    except:
        pass
    app.exec_()

def RunMainUI():
    EmailBaseWidget = QtWidgets.QWidget()
    ui = Ui_EmailBaseWidget()
    ui.setupUi(EmailBaseWidget)
    EmailBaseWidget.show()
    sys.exit(QuitApp())
    
if __name__ == "__main__":
    RunMainUI()
