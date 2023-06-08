import pickle
import os
from PyQt5 import QtWidgets
import sys

from UI import ChooseServerUI, EmailMainBaseUI

try:
    ChooseServerUI.Run()
except:
    pass
finally:
    with open("UI/Backend/TempConfig/Results.dat", "rb") as File:
        Result = pickle.load(File)
    os.remove("UI/Backend/TempConfig/Results.dat")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    MainWindow_UI = EmailMainBaseUI.Ui_EmailBaseWidget(Result[0], Result[1], Result[2])
    MainWindow_UI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())