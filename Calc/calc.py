from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__() #calls the init methods of base classes qmain window and ui calc
        self.setupUi(self)
        self.show()
