
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

class Ui_EmailMainWidget(object):
    def setupUi(self, EmailMainWidget):
        EmailMainWidget.setObjectName("EmailMainWidget")
        EmailMainWidget.resize(700, 600)
        EmailMainWidget.setMinimumSize(QtCore.QSize(700, 600))
        EmailMainWidget.setStyleSheet("QWidget#EmailMainWidget {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(EmailMainWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._EmailListLayout = QtWidgets.QVBoxLayout()
        self._EmailListLayout.setObjectName("_EmailListLayout")
        self._EmailListBackgroundFrame_1 = QtWidgets.QFrame(EmailMainWidget)
        self._EmailListBackgroundFrame_1.setStyleSheet("QFrame#_EmailListBackgroundFrame_1 {\n"
"    background: #cccccc;\n"
"}")
        self._EmailListBackgroundFrame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._EmailListBackgroundFrame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self._EmailListBackgroundFrame_1.setObjectName("_EmailListBackgroundFrame_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self._EmailListBackgroundFrame_1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._EmailList_2Layout = QtWidgets.QHBoxLayout()
        self._EmailList_2Layout.setObjectName("_EmailList_2Layout")
        self._EmailListBackgroundFrame_2 = QtWidgets.QFrame(self._EmailListBackgroundFrame_1)
        self._EmailListBackgroundFrame_2.setStyleSheet("QFrame#_EmailListBackgroundFrame_2 {\n"
"    background: #e0e0e0;\n"
"    border-top-left-radius: 20;\n"
"    border-bottom-left-radius: 20;\n"
"}")
        self._EmailListBackgroundFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._EmailListBackgroundFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self._EmailListBackgroundFrame_2.setObjectName("_EmailListBackgroundFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self._EmailListBackgroundFrame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.EmailListBackgroundLayout = QtWidgets.QHBoxLayout()
        self.EmailListBackgroundLayout.setContentsMargins(-1, 5, -1, 5)
        self.EmailListBackgroundLayout.setObjectName("EmailListBackgroundLayout")
        self.EmailListFrame = QtWidgets.QFrame(self._EmailListBackgroundFrame_2)
        self.EmailListFrame.setStyleSheet("QFrame#EmailListFrame {\n"
"    background: rgba(0,0,0,0);\n"
"    border-right: 1px solid #a6a6a6;\n"
"}")
        self.EmailListFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailListFrame.setObjectName("EmailListFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.EmailListFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.EmailListLayout = QtWidgets.QVBoxLayout()
        self.EmailListLayout.setSpacing(10)
        self.EmailListLayout.setObjectName("EmailListLayout")
        self._EmailListSearchFrame = QtWidgets.QFrame(self.EmailListFrame)
        self._EmailListSearchFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._EmailListSearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._EmailListSearchFrame.setObjectName("_EmailListSearchFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self._EmailListSearchFrame)
        self.horizontalLayout_4.setContentsMargins(20, 12, 20, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.EmailListSearchFrame = QtWidgets.QFrame(self._EmailListSearchFrame)
        self.EmailListSearchFrame.setStyleSheet("QFrame#EmailListSearchFrame {\n"
"    background: #FFFFFF;\n"
"        border-radius: 5;\n"
"}")
        self.EmailListSearchFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.EmailListSearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmailListSearchFrame.setObjectName("EmailListSearchFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.EmailListSearchFrame)
        self.horizontalLayout_5.setContentsMargins(2, 2, 0, 2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.EmailListSearchIcon = QtWidgets.QLabel(self.EmailListSearchFrame)
        self.EmailListSearchIcon.setStyleSheet("")
        self.EmailListSearchIcon.setText("")
        self.EmailListSearchIcon.setPixmap(QtGui.QPixmap(":/Icons/SVGs/MagnifyingGlass.png"))
        self.EmailListSearchIcon.setScaledContents(False)
        self.EmailListSearchIcon.setObjectName("EmailListSearchIcon")
        self.horizontalLayout_5.addWidget(self.EmailListSearchIcon)
        self.EmailListSearch = QtWidgets.QLineEdit(self.EmailListSearchFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.EmailListSearch.setFont(font)
        self.EmailListSearch.setStyleSheet("QLineEdit#EmailListSearch {\n"
"    background: none;\n"
"    border: none;\n"
"    color: #393939;\n"
"}")
        self.EmailListSearch.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.EmailListSearch.setObjectName("EmailListSearch")
        self.horizontalLayout_5.addWidget(self.EmailListSearch)
        self.horizontalLayout_4.addWidget(self.EmailListSearchFrame)
        self.EmailListLayout.addWidget(self._EmailListSearchFrame)
        self._EmailListScrollArea = QtWidgets.QScrollArea(self.EmailListFrame)
        self._EmailListScrollArea.setStyleSheet("QScrollArea#_EmailListScrollArea {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self._EmailListScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self._EmailListScrollArea.setWidgetResizable(True)
        self._EmailListScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self._EmailListScrollArea.setObjectName("_EmailListScrollArea")
        self.EmailListScrollArea_ = QtWidgets.QWidget()
        self.EmailListScrollArea_.setGeometry(QtCore.QRect(0, 0, 225, 538))
        self.EmailListScrollArea_.setStyleSheet("QWidget#EmailListScrollArea_ {\n"
"    background: rgba(0, 0, 0, 0);\n"
"}")
        self.EmailListScrollArea_.setObjectName("EmailListScrollArea_")
        self.EmailPreviewScrollAreaWidgetLayout = QtWidgets.QVBoxLayout(self.EmailListScrollArea_)
        self.EmailPreviewScrollAreaWidgetLayout.setContentsMargins(30, 0, 20, 30)
        self.EmailPreviewScrollAreaWidgetLayout.setSpacing(0)
        self.EmailPreviewScrollAreaWidgetLayout.setObjectName("EmailPreviewScrollAreaWidgetLayout")
        self._EmailListScrollArea.setWidget(self.EmailListScrollArea_)
        self.EmailListLayout.addWidget(self._EmailListScrollArea)
        self.verticalLayout_4.addLayout(self.EmailListLayout)
        self.EmailListBackgroundLayout.addWidget(self.EmailListFrame)
        self.horizontalLayout_2.addLayout(self.EmailListBackgroundLayout)
        self._EmailList_2Layout.addWidget(self._EmailListBackgroundFrame_2)
        self.horizontalLayout_3.addLayout(self._EmailList_2Layout)
        self._EmailListLayout.addWidget(self._EmailListBackgroundFrame_1)
        self.horizontalLayout.addLayout(self._EmailListLayout)
        self.EmailBodyLayout = QtWidgets.QVBoxLayout()
        self.EmailBodyLayout.setObjectName("EmailBodyLayout")
        self.horizontalLayout.addLayout(self.EmailBodyLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 6)

        self.retranslateUi(EmailMainWidget)
        QtCore.QMetaObject.connectSlotsByName(EmailMainWidget)

    def retranslateUi(self, EmailMainWidget):
        _translate = QtCore.QCoreApplication.translate
        EmailMainWidget.setWindowTitle(_translate("EmailMainWidget", "Form"))
        self.EmailListSearch.setPlaceholderText(_translate("EmailMainWidget", "Search"))

import Resource_rc


if __name__ == "__main__":
    import sys
    EmailMainWidget = QtWidgets.QWidget()
    ui = Ui_EmailMainWidget()
    ui.setupUi(EmailMainWidget)
    EmailMainWidget.show()
    sys.exit(app.exec_())
