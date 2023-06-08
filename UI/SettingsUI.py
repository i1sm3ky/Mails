from PyQt5 import QtCore, QtGui, QtWidgets

from UI.Backend.ClientFunctions import *


class Ui_EmailSettingsWidget(object):
    def setupUi(self, EmailSettingsWidget):
        EmailSettingsWidget.setObjectName("EmailSettingsWidget")
        EmailSettingsWidget.resize(700, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EmailSettingsWidget.sizePolicy().hasHeightForWidth())
        EmailSettingsWidget.setSizePolicy(sizePolicy)
        EmailSettingsWidget.setMinimumSize(QtCore.QSize(700, 600))
        EmailSettingsWidget.setStyleSheet("QWidget#EmailSettingsWidget {\n"
"    background: #cccccc;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(EmailSettingsWidget)
        self.verticalLayout.setContentsMargins(35, 0, 35, 35)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EmailSettingsTitleFrame = QtWidgets.QFrame(EmailSettingsWidget)
        self.EmailSettingsTitleFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailSettingsTitleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailSettingsTitleFrame.setObjectName("EmailSettingsTitleFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.EmailSettingsTitleFrame)
        self.verticalLayout_5.setContentsMargins(0, 15, 0, 15)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AccountSettingsLabel = QtWidgets.QLabel(self.EmailSettingsTitleFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AccountSettingsLabel.setFont(font)
        self.AccountSettingsLabel.setStyleSheet("QLabel#AccountSettingsLabel {\n"
"    color: #393939;\n"
"}")
        self.AccountSettingsLabel.setObjectName("AccountSettingsLabel")
        self.verticalLayout_5.addWidget(self.AccountSettingsLabel)
        self.AccountSettingsDescriptionLabel = QtWidgets.QLabel(self.EmailSettingsTitleFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsDescriptionLabel.setFont(font)
        self.AccountSettingsDescriptionLabel.setStyleSheet("QLabel#AccountSettingsDescriptionLabel {\n"
"    color: #7f7f7f;\n"
"}")
        self.AccountSettingsDescriptionLabel.setObjectName("AccountSettingsDescriptionLabel")
        self.verticalLayout_5.addWidget(self.AccountSettingsDescriptionLabel)
        self.verticalLayout.addWidget(self.EmailSettingsTitleFrame)
        self.EmailSettingsMainFrame = QtWidgets.QFrame(EmailSettingsWidget)
        self.EmailSettingsMainFrame.setStyleSheet("QFrame#EmailSettingsMainFrame {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.EmailSettingsMainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailSettingsMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailSettingsMainFrame.setObjectName("EmailSettingsMainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.EmailSettingsMainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._EmailSettingsLayout = QtWidgets.QVBoxLayout()
        self._EmailSettingsLayout.setObjectName("_EmailSettingsLayout")
        self._EmailSettingsBackgroundFrame_1 = QtWidgets.QFrame(self.EmailSettingsMainFrame)
        self._EmailSettingsBackgroundFrame_1.setStyleSheet("QFrame#_EmailSettingsBackgroundFrame_1 {\n"
"    background: #cccccc;\n"
"}")
        self._EmailSettingsBackgroundFrame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._EmailSettingsBackgroundFrame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self._EmailSettingsBackgroundFrame_1.setObjectName("_EmailSettingsBackgroundFrame_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self._EmailSettingsBackgroundFrame_1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._EmailSettings_2Layout = QtWidgets.QHBoxLayout()
        self._EmailSettings_2Layout.setObjectName("_EmailSettings_2Layout")
        self._EmailSettingsBackgroundFrame_2 = QtWidgets.QFrame(self._EmailSettingsBackgroundFrame_1)
        self._EmailSettingsBackgroundFrame_2.setStyleSheet("QFrame#_EmailSettingsBackgroundFrame_2 {\n"
"    background: #FFFFFF;\n"
"    border-top-left-radius: 20;\n"
"    border-bottom-left-radius: 20;\n"
"}")
        self._EmailSettingsBackgroundFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._EmailSettingsBackgroundFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self._EmailSettingsBackgroundFrame_2.setObjectName("_EmailSettingsBackgroundFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._EmailSettingsBackgroundFrame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.EmailSettingsBackgroundLayout = QtWidgets.QHBoxLayout()
        self.EmailSettingsBackgroundLayout.setContentsMargins(-1, 5, -1, 5)
        self.EmailSettingsBackgroundLayout.setObjectName("EmailSettingsBackgroundLayout")
        self.EmailSettingsLayout = QtWidgets.QFrame(self._EmailSettingsBackgroundFrame_2)
        self.EmailSettingsLayout.setStyleSheet("QFrame#EmailSettingsLayout {\n"
"    background: rgba(0,0,0,0);\n"
"    border-right: 1px solid #a6a6a6;\n"
"}")
        self.EmailSettingsLayout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailSettingsLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailSettingsLayout.setObjectName("EmailSettingsLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.EmailSettingsLayout)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.EmailSettingsFrame = QtWidgets.QFrame(self.EmailSettingsLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmailSettingsFrame.sizePolicy().hasHeightForWidth())
        self.EmailSettingsFrame.setSizePolicy(sizePolicy)
        self.EmailSettingsFrame.setMinimumSize(QtCore.QSize(0, 300))
        self.EmailSettingsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailSettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailSettingsFrame.setObjectName("EmailSettingsFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.EmailSettingsFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.AccountButton = QtWidgets.QPushButton(self.EmailSettingsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.AccountButton.setFont(font)
        self.AccountButton.setStyleSheet("QPushButton#AccountButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-right: 6;\n"
"}\n"
"\n"
"QPushButton#AccountButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#AccountButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Settings/SVGs/SettingsIcons/Account(Deactivated).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AccountButton.setIcon(icon)
        self.AccountButton.setIconSize(QtCore.QSize(32, 32))
        self.AccountButton.setObjectName("AccountButton")
        self.AccountButton.clicked.connect(self.AccountButtonClicked)
        self.verticalLayout_2.addWidget(self.AccountButton)
        self.PersonalizationButton = QtWidgets.QPushButton(self.EmailSettingsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.PersonalizationButton.setFont(font)
        self.PersonalizationButton.setStyleSheet("QPushButton#PersonalizationButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-left: 35;\n"
"    padding-bottom:8;\n"
"}\n"
"\n"
"QPushButton#PersonalizationButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#PersonalizationButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Settings/SVGs/SettingsIcons/Personalization(Deactivacted).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PersonalizationButton.setIcon(icon1)
        self.PersonalizationButton.setIconSize(QtCore.QSize(22, 22))
        self.PersonalizationButton.setCheckable(False)
        self.PersonalizationButton.setObjectName("PersonalizationButton")
        self.PersonalizationButton.setEnabled(False)
        self.verticalLayout_2.addWidget(self.PersonalizationButton)
        self.SecurityButton = QtWidgets.QPushButton(self.EmailSettingsFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.SecurityButton.setFont(font)
        self.SecurityButton.setStyleSheet("QPushButton#SecurityButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #a6a6a6;\n"
"    padding-right: 10;\n"
"}\n"
"\n"
"QPushButton#SecurityButton:hover {\n"
"    color: #7f7f7f;\n"
"}\n"
"\n"
"QPushButton#SecurityButton:pressed {\n"
"    color: #393939;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Settings/SVGs/SettingsIcons/Security(Deactivated).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SecurityButton.setIcon(icon2)
        self.SecurityButton.setIconSize(QtCore.QSize(18, 18))
        self.SecurityButton.setObjectName("SecurityButton")
        self.SecurityButton.clicked.connect(self.SecurityButtonClicked)
        self.verticalLayout_2.addWidget(self.SecurityButton)
        self.verticalLayout_3.addWidget(self.EmailSettingsFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 3)
        self.EmailSettingsBackgroundLayout.addWidget(self.EmailSettingsLayout)
        self.horizontalLayout_2.addLayout(self.EmailSettingsBackgroundLayout)
        self._EmailSettings_2Layout.addWidget(self._EmailSettingsBackgroundFrame_2)
        self.horizontalLayout_3.addLayout(self._EmailSettings_2Layout)
        self._EmailSettingsLayout.addWidget(self._EmailSettingsBackgroundFrame_1)
        self.horizontalLayout.addLayout(self._EmailSettingsLayout)
        self.EmailSettingsMainLayout = QtWidgets.QVBoxLayout()
        self.EmailSettingsMainLayout.setSpacing(0)
        self.EmailSettingsMainLayout.setObjectName("EmailSettingsMainLayout")
        self.EmailSettingsStackedWidget = QtWidgets.QStackedWidget(self.EmailSettingsMainFrame)
        self.EmailSettingsStackedWidget.setStyleSheet("QStackedWidget#EmailBodyStackedWidget {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.EmailSettingsStackedWidget.setObjectName("EmailSettingsStackedWidget")
        self.AccountPage = QtWidgets.QWidget()
        self.AccountPage.setStyleSheet("QWidget#AccountPage {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-top-right-radius: 20;\n"
"}")
        self.AccountPage.setObjectName("AccountPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.AccountPage)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.AccountPageFrame = QtWidgets.QFrame(self.AccountPage)
        self.AccountPageFrame.setMaximumSize(QtCore.QSize(650, 550))
        self.AccountPageFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AccountPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AccountPageFrame.setObjectName("AccountPageFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.AccountPageFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.AccountPageLayout = QtWidgets.QFrame(self.AccountPageFrame)
        self.AccountPageLayout.setObjectName("AccountPageLayout")
        self.gridLayout = QtWidgets.QGridLayout(self.AccountPageLayout)
        self.gridLayout.setContentsMargins(25, 0, 25, 165)
        self.gridLayout.setHorizontalSpacing(27)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.AccountSettingsLastNameLineEdit = QtWidgets.QLineEdit(self.AccountPageLayout)
        self.AccountSettingsLastNameLineEdit.setStyleSheet("QLineEdit#AccountSettingsLastNameLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 4;\n"
"}")
        self.AccountSettingsLastNameLineEdit.setObjectName("AccountSettingsLastNameLineEdit")
        self.AccountSettingsLastNameLineEdit.textChanged.connect(self.ShowSaveChanges)
        self.gridLayout.addWidget(self.AccountSettingsLastNameLineEdit, 3, 1, 1, 1)
        self.AccountSettingsEmailLabel = QtWidgets.QLabel(self.AccountPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsEmailLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsEmailLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsEmailLabel.setFont(font)
        self.AccountSettingsEmailLabel.setStyleSheet("QLabel#AccountSettingsEmailLabel {\n"
"    color: #a6a6a6;\n"
"    padding-top: 20;\n"
"    padding-bottom: 2;\n"
"}")
        self.AccountSettingsEmailLabel.setObjectName("AccountSettingsEmailLabel")
        self.gridLayout.addWidget(self.AccountSettingsEmailLabel, 4, 0, 1, 1)
        self.AccountSettingsLastNameLabel = QtWidgets.QLabel(self.AccountPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsLastNameLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsLastNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsLastNameLabel.setFont(font)
        self.AccountSettingsLastNameLabel.setStyleSheet("QLabel#AccountSettingsLastNameLabel {\n"
"    color: #a6a6a6;\n"
"    padding-top: 20;\n"
"    padding-bottom: 2;\n"
"}")
        self.AccountSettingsLastNameLabel.setObjectName("AccountSettingsLastNameLabel")
        self.gridLayout.addWidget(self.AccountSettingsLastNameLabel, 2, 1, 1, 1)
        self.AccountSettingsFirstNameLineEdit = QtWidgets.QLineEdit(self.AccountPageLayout)
        self.AccountSettingsFirstNameLineEdit.setStyleSheet("QLineEdit#AccountSettingsFirstNameLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 4;\n"
"}")
        self.AccountSettingsFirstNameLineEdit.setObjectName("AccountSettingsFirstNameLineEdit")
        self.AccountSettingsFirstNameLineEdit.textChanged.connect(self.ShowSaveChanges)
        self.gridLayout.addWidget(self.AccountSettingsFirstNameLineEdit, 3, 0, 1, 1)
        self.AccountSettingsEmailLineEdit = QtWidgets.QLineEdit(self.AccountPageLayout)
        self.AccountSettingsEmailLineEdit.setStyleSheet("QLineEdit#AccountSettingsEmailLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 4;\n"
"}")
        self.AccountSettingsEmailLineEdit.setObjectName("AccountSettingsEmailLineEdit")
        self.AccountSettingsEmailLineEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.AccountSettingsEmailLineEdit, 5, 0, 1, 1)
        self.AccountSettingsPhoneNumberLineEdit = QtWidgets.QLineEdit(self.AccountPageLayout)
        self.AccountSettingsPhoneNumberLineEdit.setStyleSheet("QLineEdit#AccountSettingsPhoneNumberLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 4;\n"
"}")
        self.AccountSettingsPhoneNumberLineEdit.setObjectName("AccountSettingsPhoneNumberLineEdit")
        self.AccountSettingsPhoneNumberLineEdit.textChanged.connect(self.ShowSaveChanges)
        self.gridLayout.addWidget(self.AccountSettingsPhoneNumberLineEdit, 5, 1, 1, 1)
        self.AccountSettingsPhoneNumberLabel = QtWidgets.QLabel(self.AccountPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsPhoneNumberLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsPhoneNumberLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsPhoneNumberLabel.setFont(font)
        self.AccountSettingsPhoneNumberLabel.setStyleSheet("QLabel#AccountSettingsPhoneNumberLabel {\n"
"    color: #a6a6a6;\n"
"    padding-top:     20;\n"
"    padding-bottom: 2;\n"
"}")
        self.AccountSettingsPhoneNumberLabel.setObjectName("AccountSettingsPhoneNumberLabel")
        self.gridLayout.addWidget(self.AccountSettingsPhoneNumberLabel, 4, 1, 1, 1)
        self.GeneralInfoLabel = QtWidgets.QLabel(self.AccountPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GeneralInfoLabel.sizePolicy().hasHeightForWidth())
        self.GeneralInfoLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.GeneralInfoLabel.setFont(font)
        self.GeneralInfoLabel.setStyleSheet("QLabel#GeneralInfoLabel {\n"
"    color: #393939;\n"
"    padding-top: 20;\n"
"    padding-bottom: 20;\n"
"}")
        self.GeneralInfoLabel.setObjectName("GeneralInfoLabel")
        self.gridLayout.addWidget(self.GeneralInfoLabel, 0, 0, 1, 1)
        self.AccountSettingsFirstNameLabel = QtWidgets.QLabel(self.AccountPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsFirstNameLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsFirstNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsFirstNameLabel.setFont(font)
        self.AccountSettingsFirstNameLabel.setStyleSheet("QLabel#AccountSettingsFirstNameLabel {\n"
"    color: #a6a6a6;\n"
"    padding-top: 20;\n"
"    padding-bottom: 2;\n"
"}")
        self.AccountSettingsFirstNameLabel.setObjectName("AccountSettingsFirstNameLabel")
        self.gridLayout.addWidget(self.AccountSettingsFirstNameLabel, 2, 0, 1, 1)
        self.AccountSettingsProfilePictureFrame = QtWidgets.QFrame(self.AccountPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsProfilePictureFrame.sizePolicy().hasHeightForWidth())
        self.AccountSettingsProfilePictureFrame.setSizePolicy(sizePolicy)
        self.AccountSettingsProfilePictureFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AccountSettingsProfilePictureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AccountSettingsProfilePictureFrame.setObjectName("AccountSettingsProfilePictureFrame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.AccountSettingsProfilePictureFrame)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.AccountSettingsProfilePictureFrame_ = QtWidgets.QFrame(self.AccountSettingsProfilePictureFrame)
        self.AccountSettingsProfilePictureFrame_.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AccountSettingsProfilePictureFrame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AccountSettingsProfilePictureFrame_.setObjectName("AccountSettingsProfilePictureFrame_")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.AccountSettingsProfilePictureFrame_)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.AccountSettingsProfilePictureLabel = QtWidgets.QLabel(self.AccountSettingsProfilePictureFrame_)
        self.AccountSettingsProfilePictureLabel.setText("")
        self.AccountSettingsProfilePictureLabel.setObjectName("AccountSettingsProfilePictureLabel")
        self.horizontalLayout_5.addWidget(self.AccountSettingsProfilePictureLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_13.addWidget(self.AccountSettingsProfilePictureFrame_)
        self.AccountSettingsProfilePictureChangeButton = QtWidgets.QPushButton(self.AccountSettingsProfilePictureFrame)
        self.AccountSettingsProfilePictureChangeButton.setStyleSheet("QPushButton#AccountSettingsProfilePictureChangeButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #0077ff;\n"
"    text-align: center;\n"
"    padding-bottom: 4;\n"
"}\n"
"\n"
"QPushButton#AccountSettingsProfilePictureChangeButton:hover {\n"
"    color: #4da0ff;\n"
"}\n"
"\n"
"QPushButton#AccountSettingsProfilePictureChangeButton:pressed {\n"
"    color: #004cff;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/SVGs/EditIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AccountSettingsProfilePictureChangeButton.setIcon(icon3)
        self.AccountSettingsProfilePictureChangeButton.setObjectName("AccountSettingsProfilePictureChangeButton")
        self.verticalLayout_13.addWidget(self.AccountSettingsProfilePictureChangeButton)
        self.gridLayout.addWidget(self.AccountSettingsProfilePictureFrame, 1, 0, 1, 2)
        self.verticalLayout_7.addWidget(self.AccountPageLayout)
        self.verticalLayout_4.addWidget(self.AccountPageFrame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.EmailSettingsStackedWidget.addWidget(self.AccountPage)
        self.PersonalizationPage = QtWidgets.QWidget()
        self.PersonalizationPage.setStyleSheet("QWidget#PersonalizationPage {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-top-right-radius: 20;\n"
"}")
        self.PersonalizationPage.setObjectName("PersonalizationPage")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.PersonalizationPage)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.PersionalizationPageFrame = QtWidgets.QFrame(self.PersonalizationPage)
        self.PersionalizationPageFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PersionalizationPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PersionalizationPageFrame.setObjectName("PersionalizationPageFrame")
        self.horizontalLayout_6.addWidget(self.PersionalizationPageFrame)
        self.EmailSettingsStackedWidget.addWidget(self.PersonalizationPage)
        self.SecurityPage = QtWidgets.QWidget()
        self.SecurityPage.setStyleSheet("QWidget#SecurityPage {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #FFFFFF;\n"
"    border-top-right-radius: 20;\n"
"}")
        self.SecurityPage.setObjectName("SecurityPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SecurityPage)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SecurityPageFrame = QtWidgets.QFrame(self.SecurityPage)
        self.SecurityPageFrame.setMaximumSize(QtCore.QSize(650, 550))
        self.SecurityPageFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SecurityPageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SecurityPageFrame.setObjectName("SecurityPageFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.SecurityPageFrame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.SecurityPageLayout = QtWidgets.QFrame(self.SecurityPageFrame)
        self.SecurityPageLayout.setObjectName("SecurityPageLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.SecurityPageLayout)
        self.verticalLayout_9.setContentsMargins(25, 0, 25, 25)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SecurityandPasswordLabel = QtWidgets.QLabel(self.SecurityPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SecurityandPasswordLabel.sizePolicy().hasHeightForWidth())
        self.SecurityandPasswordLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SecurityandPasswordLabel.setFont(font)
        self.SecurityandPasswordLabel.setStyleSheet("QLabel#SecurityandPasswordLabel {\n"
"    color: #393939;\n"
"    padding-top: 20;\n"
"    padding-bottom: 20;\n"
"}")
        self.SecurityandPasswordLabel.setObjectName("SecurityandPasswordLabel")
        self.verticalLayout_9.addWidget(self.SecurityandPasswordLabel)
        self.AccountSettingsPasswordLabel = QtWidgets.QLabel(self.SecurityPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsPasswordLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsPasswordLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsPasswordLabel.setFont(font)
        self.AccountSettingsPasswordLabel.setStyleSheet("QLabel#AccountSettingsPasswordLabel {\n"
"    color: #606060;\n"
"}")
        self.AccountSettingsPasswordLabel.setObjectName("AccountSettingsPasswordLabel")
        self.verticalLayout_9.addWidget(self.AccountSettingsPasswordLabel)
        self.AccountSettingsPasswordLineEdit = QtWidgets.QLineEdit(self.SecurityPageLayout)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AccountSettingsPasswordLineEdit.setFont(font)
        self.AccountSettingsPasswordLineEdit.setStyleSheet("QLineEdit#AccountSettingsPasswordLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 5;\n"
"    padding-left: 3;\n"
"}")
        self.AccountSettingsPasswordLineEdit.setInputMask("")
        self.AccountSettingsPasswordLineEdit.setText("")
        self.AccountSettingsPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.AccountSettingsPasswordLineEdit.setReadOnly(True)
        self.AccountSettingsPasswordLineEdit.setObjectName("AccountSettingsPasswordLineEdit")
        self.verticalLayout_9.addWidget(self.AccountSettingsPasswordLineEdit)
        self.ChangePasswordButton = QtWidgets.QPushButton(self.SecurityPageLayout)
        self.ChangePasswordButton.setStyleSheet("QPushButton#ChangePasswordButton {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"    color: #1884ff;\n"
"    padding-bottom: 2;\n"
"    text-align: right;\n"
"}\n"
"\n"
"QPushButton#ChangePasswordButton:hover {\n"
"    color: #419aff;\n"
"}\n"
"\n"
"QPushButton#ChangePasswordButton:pressed {\n"
"    color: #004cff;\n"
"}")
        self.ChangePasswordButton.setObjectName("ChangePasswordButton")
        self.verticalLayout_9.addWidget(self.ChangePasswordButton)
        self.AccountSettingsSecurityQuestionLabel = QtWidgets.QLabel(self.SecurityPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsSecurityQuestionLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsSecurityQuestionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsSecurityQuestionLabel.setFont(font)
        self.AccountSettingsSecurityQuestionLabel.setStyleSheet("QLabel#AccountSettingsSecurityQuestionLabel {\n"
"    color: #606060;\n"
"}")
        self.AccountSettingsSecurityQuestionLabel.setObjectName("AccountSettingsSecurityQuestionLabel")
        self.verticalLayout_9.addWidget(self.AccountSettingsSecurityQuestionLabel)
        self.AccountSettingsSecurityQuestionLineEdit = QtWidgets.QLineEdit(self.SecurityPageLayout)
        self.AccountSettingsSecurityQuestionLineEdit.setStyleSheet("QLineEdit#AccountSettingsSecurityQuestionLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 5;\n"
"    padding-left: 3;\n"
"}")
        self.AccountSettingsSecurityQuestionLineEdit.setObjectName("AccountSettingsSecurityQuestionLineEdit")
        self.verticalLayout_9.addWidget(self.AccountSettingsSecurityQuestionLineEdit)
        self.AccountSettingsSecurityQuestionAnswerLabel = QtWidgets.QLabel(self.SecurityPageLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccountSettingsSecurityQuestionAnswerLabel.sizePolicy().hasHeightForWidth())
        self.AccountSettingsSecurityQuestionAnswerLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.AccountSettingsSecurityQuestionAnswerLabel.setFont(font)
        self.AccountSettingsSecurityQuestionAnswerLabel.setStyleSheet("QLabel#AccountSettingsSecurityQuestionAnswerLabel {\n"
"    color: #606060;\n"
"}")
        self.AccountSettingsSecurityQuestionAnswerLabel.setObjectName("AccountSettingsSecurityQuestionAnswerLabel")
        self.verticalLayout_9.addWidget(self.AccountSettingsSecurityQuestionAnswerLabel)
        self.AccountSettingsSecurityQuestionAnswerLineEdit = QtWidgets.QLineEdit(self.SecurityPageLayout)
        self.AccountSettingsSecurityQuestionAnswerLineEdit.setStyleSheet("QLineEdit#AccountSettingsSecurityQuestionAnswerLineEdit {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    color: #393939;\n"
"    border: 1px solid #a6a6a6;\n"
"    border-radius: 5;\n"
"    padding-left: 3;\n"
"}")
        self.AccountSettingsSecurityQuestionAnswerLineEdit.setObjectName("AccountSettingsSecurityQuestionAnswerLineEdit")
        self.verticalLayout_9.addWidget(self.AccountSettingsSecurityQuestionAnswerLineEdit)
        self.verticalLayout_8.addWidget(self.SecurityPageLayout)
        self.verticalLayout_6.addWidget(self.SecurityPageFrame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 2)
        self.EmailSettingsStackedWidget.addWidget(self.SecurityPage)
        self.EmailSettingsMainLayout.addWidget(self.EmailSettingsStackedWidget)
        self.SaveChangesFrame = QtWidgets.QFrame(self.EmailSettingsMainFrame)
        self.SaveChangesFrame.setStyleSheet("QFrame#SaveChangesFrame {\n"
"    background: #FFFFFF;\n"
"    border-bottom-right-radius: 20;\n"
"}")
        self.SaveChangesFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SaveChangesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SaveChangesFrame.setObjectName("SaveChangesFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SaveChangesFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 18, 18)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.SaveChangesButton = QtWidgets.QPushButton(self.SaveChangesFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveChangesButton.sizePolicy().hasHeightForWidth())
        self.SaveChangesButton.setSizePolicy(sizePolicy)
        self.SaveChangesButton.setMinimumSize(QtCore.QSize(105, 25))
        self.SaveChangesButton.setStyleSheet("QPushButton#SaveChangesButton {\n"
"    background: #0077ff;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #0077ff;\n"
"    border-radius: 7;\n"
"}\n"
"\n"
"QPushButton#SaveChangesButton:hover {\n"
"    background: #1884ff;\n"
"    border: 1px solid #1884ff;\n"
"}\n"
"\n"
"QPushButton#SaveChangesButton:pressed {\n"
"    background: #65adff;\n"
"    border: 1px solid #65adff;\n"
"}\n"
"")
        self.SaveChangesButton.setObjectName("SaveChangesButton")
        self.SaveChangesButton.clicked.connect(self.SaveChanges)
        self.horizontalLayout_4.addWidget(self.SaveChangesButton)
        self.EmailSettingsMainLayout.addWidget(self.SaveChangesFrame)
        self.horizontalLayout.addLayout(self.EmailSettingsMainLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addWidget(self.EmailSettingsMainFrame)

        self.retranslateUi(EmailSettingsWidget)
        self.EmailSettingsStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EmailSettingsWidget)

    def retranslateUi(self, EmailSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        EmailSettingsWidget.setWindowTitle(_translate("EmailSettingsWidget", "Form"))
        self.AccountSettingsLabel.setText(_translate("EmailSettingsWidget", "Account Settings"))
        self.AccountSettingsDescriptionLabel.setText(_translate("EmailSettingsWidget", "Change your profile and account settings"))
        self.AccountButton.setText(_translate("EmailSettingsWidget", "Account"))
        self.PersonalizationButton.setText(_translate("EmailSettingsWidget", "Personalization"))
        self.SecurityButton.setText(_translate("EmailSettingsWidget", "Security"))
        self.AccountSettingsEmailLabel.setText(_translate("EmailSettingsWidget", "Email"))
        self.AccountSettingsLastNameLabel.setText(_translate("EmailSettingsWidget", "Last Name"))
        self.AccountSettingsPhoneNumberLabel.setText(_translate("EmailSettingsWidget", "Phone Number"))
        self.GeneralInfoLabel.setText(_translate("EmailSettingsWidget", "General Info"))
        self.AccountSettingsFirstNameLabel.setText(_translate("EmailSettingsWidget", "First Name"))
        self.AccountSettingsProfilePictureChangeButton.setText(_translate("EmailSettingsWidget", "Change Profile Picture"))
        self.SecurityandPasswordLabel.setText(_translate("EmailSettingsWidget", "Security and Password"))
        self.AccountSettingsPasswordLabel.setText(_translate("EmailSettingsWidget", "Password"))
        self.ChangePasswordButton.setText(_translate("EmailSettingsWidget", "Change Password"))
        self.AccountSettingsSecurityQuestionLabel.setText(_translate("EmailSettingsWidget", "Security Question"))
        self.AccountSettingsSecurityQuestionAnswerLabel.setText(_translate("EmailSettingsWidget", "Answer"))
        self.SaveChangesButton.setText(_translate("EmailSettingsWidget", "Save Changes"))
        
        self.SaveChangesButton.hide()
        
    def AccountButtonClicked(self):
        self.EmailSettingsStackedWidget.setCurrentIndex(0)
        
    def SecurityButtonClicked(self):
        self.EmailSettingsStackedWidget.setCurrentIndex(2)
        
    def SaveChanges(self):
        CommitChanges(self.AccountSettingsFirstNameLineEdit.text(), self.AccountSettingsLastNameLineEdit.text(), self.AccountSettingsPhoneNumberLineEdit.text(), self.AccountSettingsSecurityQuestionLineEdit.text(), self.AccountSettingsSecurityQuestionAnswerLineEdit.text())

    def ShowSaveChanges(self):
        self.SaveChangesButton.show()

import Resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmailSettingsWidget = QtWidgets.QWidget()
    ui = Ui_EmailSettingsWidget()
    ui.setupUi(EmailSettingsWidget)
    EmailSettingsWidget.show()
    sys.exit(app.exec_())
