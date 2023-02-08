import sys
from PySide6 import QtWidgets

from MainWindow import Ui_MainWindow
from ..modulos.ui_mainwindow import Ui_MainWindow as segunda


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()