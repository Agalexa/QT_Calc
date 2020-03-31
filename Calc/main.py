import sys
from PyQt5 import QtWidgets
from calculator import CalculatorWindow 

app = QtWidgets.QApplication(sys.argv)
calculator = CalculatorWindow()

sys.exit(app.exec_())
