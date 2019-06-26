import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Tugas5(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle(' ')

        self.showTitle = QCheckBox()
        self.showTitle.setText('Show Title')
        self.showTitle.stateChanged.connect(self.cek)

        layout = QVBoxLayout()
        layout.addWidget(self.showTitle)

        self.setLayout(layout)

    def cek(self):
        if self.showTitle.isChecked():
            self.setWindowTitle('Contoh QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = Tugas5()
    form.show()

    a.exec_()