import sys

from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class MainForm(QtWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(400, 200)
		self.move(300, 300)
		self.setWindowTitle('Demo QTextEdit')

		self.label1 = Qlabel()
		self.label1.setText('No. HP')
		self.phoneEdit = QLineEdit()
		vbox1 = QVBoxLayout()
		vbox1.addWidget(self.label1)
		vbox1.addWidget(self.phoneEdit)

		self.label2 = Qlabel()
		self.label2 = setText('Pesan')
		self.messageEdit = QTextEdit()
		vbox2 = QVBoxLayout()
		vbox2.addWidget(self.label2)
		vbox2.addWidget(self.messageEdit)

		vbox3 = QVBoxLayout()
		vbox3.addLayout(vbox1)
		vbox3.addLayout(vbox2)

		self.sendButton = QPushButton('&Kirim SMS')
		self.cancelButton = QPushButton('&Batal')
		hbox = QHBoxLayout()
		hbox.addStrech()
		hbox.addWidget(self.sendButton)
		hbox.addWidget(self.cancelButton)

		layout = QVBoxLayout()
		layout.addLayout(vbox3)
		horizontalLine = QFrame();
		horizontalLine.setFrameShape(QFrame.HLine)       
		horizontalLine.setFrameShadow(QFrame.Sunken)       
		layout.addWidget(horizontalLine)       
		layout.addLayout(hbox)      
		self.setLayout(layout) 

if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()     

	a.exec_() 
 