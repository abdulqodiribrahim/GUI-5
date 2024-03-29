import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Tugas3(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(400,200)
		self.move(300,300)
		self.setWindowTitle('Demo QTextEdit')
		
		self.label1 = QLabel()
		self.label1.setText('Dari')
		self.phoneEdit = QLineEdit()
		vbox1 = QVBoxLayout()
		vbox1.addWidget(self.label1)
		vbox1.addWidget(self.phoneEdit)
		
		self.label1 = QLabel()
		self.label1.setText('Untuk')
		self.phoneEdit = QLineEdit()
		vbox2 = QVBoxLayout()
		vbox2.addWidget(self.label1)
		vbox2.addWidget(self.phoneEdit)
		
		self.label2 = QLabel()
		self.label2.setText('')
		self.massageEdit = QTextEdit()
		vbox3 = QVBoxLayout()
		vbox3.addWidget(self.label2)
		vbox3.addWidget(self.massageEdit)
		
		vbox4 = QVBoxLayout()
		vbox4.addLayout(vbox1)
		vbox4.addLayout(vbox2)
		vbox4.addLayout(vbox3)
		
		self.sendButton = QPushButton('&Kirim SMS')
		self.cancelButton = QPushButton('&Batal')
		hbox = QHBoxLayout()
		hbox.addStretch()
		hbox.addWidget(self.sendButton)
		hbox.addWidget(self.cancelButton)

		layout = QVBoxLayout()
		layout.addLayout(vbox4)
		horizontalLine = QFrame();
		horizontalLine.setFrameShape(QFrame.HLine)
		horizontalLine.setFrameShadow(QFrame.Sunken)
		layout.addWidget(horizontalLine)
		layout.addLayout(hbox)
		self.setLayout(layout)

if __name__ == '__main__':
	a = QApplication(sys.argv)

	form = Tugas3()
	form.show()

	a.exec_()