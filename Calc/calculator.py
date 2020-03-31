from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    
    firstNum = None
    userIsTypingSecondNumber = False


    def __init__(self):
        super().__init__() #calls the init methods of base classes qmain window and ui calc
        self.setupUi(self)
        self.show()
        self.pushButton_0.clicked.connect(self.digit_pressed) #connects a slot to the event button 0 press
        self.pushButton_01.clicked.connect(self.digit_pressed)
        self.pushButton_02.clicked.connect(self.digit_pressed)
        self.pushButton_03.clicked.connect(self.digit_pressed)
        self.pushButton_04.clicked.connect(self.digit_pressed)
        self.pushButton_05.clicked.connect(self.digit_pressed)
        self.pushButton_06.clicked.connect(self.digit_pressed)
        self.pushButton_07.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_09.clicked.connect(self.digit_pressed)

        self.pushButton_dot.clicked.connect(self.decimal_pressed)

        self.pushButton_plus_minus.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percentage.clicked.connect(self.unary_operation_pressed)
        self.pushButton_plus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_plus.setCheckable(True)
        self.pushButton_minus.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)        
        self.pushButton_divide.setCheckable(True)

        self.pushButton_equals.clicked.connect(self.equals_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)

    def digit_pressed(self): #slot
        button = self.sender()

        if ((self.pushButton_plus.isChecked() or self.pushButton_minus.isChecked() or
            self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked()) and (not self.userIsTypingSecondNumber)):
            newLabel = format(float(button.text()),'.15g')
            self.userIsTypingSecondNumber = True
        else: 
            if (("." in self.label.text()) and (button.text() == '0')):
                newLabel = format(self.label.text() + button.text(), '.15')
            else:
                newLabel = format(float(self.label.text() + button.text()),'.15g')

        self.label.setText(newLabel) #displays button pressed in label widget

    def decimal_pressed(self):
        self.label.setText(self.label.text() + '.') #concantenates decimal at end

    def unary_operation_pressed(self):
        button = self.sender()

        labelNumber = float(self.label.text())
        if button.text() == '+/-':
            labelNumber = labelNumber * -1
        else: #button == '%'
            labelNumber = labelNumber * .01
        newLabel = format(labelNumber,'.15g')
        self.label.setText(newLabel)

    def binary_operation_pressed(self):
        button = self.sender()
        self.firstNum = float(self.label.text())
        #qt attribute for button
        button.setChecked(True)
        
    def equals_pressed(self):

        secondNum = float(self.label.text())

        if self.pushButton_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_plus.setChecked(False)

        elif self.pushButton_minus.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_minus.setChecked(False)
        elif self.pushButton_multiply.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_multiply.setChecked(False)
        elif self.pushButton_divide.isChecked():
            labelNumber = self.firstNum / secondNum
            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)
            self.pushButton_divide.setChecked(False)
        
        self.userIsTypingSecondNumber = False

    def clear_pressed(self):
        self.pushButton_plus.setChecked(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.label.setText('0')