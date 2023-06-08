from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

def ShowMessageBox(Type, Title, Message, Buttons, DefaultButton=None, SubMessage=''):
    MessageBox = QMessageBox()
    MessageBox.setIcon(Type)
    MessageBox.setWindowTitle(Title)
    MessageBox.setText(Message)
    MessageBox.setInformativeText(SubMessage)
    MessageBox.setStandardButtons(Buttons)
    MessageBox.setDefaultButton(DefaultButton)
    MessageBox.buttonClicked.connect(MessageButtonClicked)
    MessageBox.exec_()
def MessageButtonClicked(Return):
    return Return.text()

#Icons- Critical, Warning, Information, Question
#Buttons- Ok, Open, Save, Cancel, Close, Yes, No, Abrot, Retry, Ignore