import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QMessageBox, QWidget,QPushButton,QLabel,QShortcut
from PyQt5.QtGui import QFont, QIcon,QKeySequence
from PyQt5.QtCore import Qt

from random import randint
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Guess the Num')
        self.setWindowIcon(QIcon('number.png'))
        self.layout = QFormLayout()

        global font
        font = QFont()
        font.setFamily('IRFerdosi')
        font.setPointSize(18)
        self.setFont(font)
        
        self.input_num = QLineEdit()
        self.input_num.setStyleSheet("""
        QWidget {
            border: 3px solid #b9936c;
            background-color: #e6e2d3;
            font: 18pt "IRFerdosi";
        }
        """)
        self.input_num.setPlaceholderText('Enter the Number')
        self.layout.addRow(self.input_num)

        self.push_btn = QPushButton()
        self.push_btn.setStyleSheet("""
        QWidget {
            border: 2px solid green;
            background-color: #e3eaa7;
            font: 18pt "IRFerdosi";}
        """)

        self.msgSc = QShortcut(QKeySequence('Return'),self)

        self.push_btn.setText('Enter')
        self.push_btn.setShortcut('Enter')

        self.layout.addRow(self.push_btn)

        self.big_or_small = QLabel()
        self.big_or_small.setAlignment(Qt.AlignCenter)
        self.layout.addRow(self.big_or_small)

        self.resize(315,100)
        self.setMaximumSize(315,100)
        self.setLayout(self.layout)

        self.random_num = randint(0,1000)
        print(self.random_num)
        self.win = False

        self.info = False
        self.attemps = 1
        self.times = 0

        self.info_label = QLabel()
        self.info_label.setStyleSheet("""
        QWidget {
            border: 3px solid brown;
            background-color: #e6e2d3;
            font: 18pt "IRFerdosi";
        }
        """)

        def pushed():
            if self.times%2==0:
                self.push_btn.setStyleSheet("""
                QWidget {
                    border: 2px solid green;
                    background-color: #fefbd8;
                    font: 18pt "IRFerdosi";
                }
                """)
            else:
                self.push_btn.setStyleSheet("""
                    QWidget {
                        border: 2px solid green;
                        background-color: #e3eaa7;
                        font: 18pt "IRFerdosi";}
                    """)
            self.times+=1

            if self.win:
                self.info_label.setParent(None)

                self.input_num = QLineEdit()
                self.input_num.setText('')
                self.input_num.setStyleSheet("""
                QWidget {
                    border: 2px solid #b9936c;
                    background-color: #e6e2d3;
                    font: 18pt "IRFerdosi";
                        }
                    """)
                self.input_num.setPlaceholderText('Enter the Number')
                self.layout.insertRow(0,self.input_num)
                self.input_num.setFocus()

                self.push_btn.setText('Enter')
                self.win = False

            else:
                is_float = True
                num = self.input_num.text()
                try:
                    num = float(num)
                except ValueError:
                    is_float = False

                if is_float:
                    if float(num)==self.random_num:
                        self.big_or_small.setParent(None)
                        self.random_num = randint(0, 1000)
                        print(self.random_num)

                        self.win = True
                        
                        self.input_num.setParent(None)
                        self.info_label.setText(f'You have attempted {self.attemps} times')
                        self.layout.insertRow(0,self.info_label)
                        self.attemps = 0
                        self.info = True

                        self.push_btn.setText('Play Again!')
                    else:
                        if num>self.random_num:
                            self.big_or_small.setText('The Number is smaller')
                        else:
                            self.big_or_small.setText('The Number is bigger')

                        self.big_or_small.setStyleSheet("""
                        QWidget {
                            border : 3px solid #feb236;
                            background-color: #fefbd8;
                            font : 18pt "IRFerdosi";
                        }
                        """)
                        self.layout.addRow(self.big_or_small)

                else:
                    self.Error()
                
                self.attemps+=1

            
        self.push_btn.clicked.connect(pushed)
        self.msgSc.activated.connect(pushed)


    def Error(self):
        font = QFont()
        font.setFamily('Franklin Gothic Book')
        font.setPointSize(15)

        msg = QMessageBox()
        msg.setFont(font)
        msg.setWindowTitle('Type Error')
        msg.setWindowIcon(QIcon('error_pic.png'))
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Invalid Input')
        msg.exec_()

    def closeEvent(self, event):
        info = QMessageBox()
        info.setWindowTitle('Confirmation')
        info.setWindowIcon(QIcon('info.jpg'))
        info.setFont(font)
        info.setIcon(QMessageBox.Information)
        info.setText('Stop playing?')
        info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        info.setDefaultButton(QMessageBox.Cancel)

        returnValue = info.exec()
        if returnValue == QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()

    


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
