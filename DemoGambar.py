import sys

from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoGambar(QtWidget):
	def__init__(self):
		super()__init__()
		self.setupUi()

	def setupUI(self):
		self.resize(500,300)
		self.move(300,300)
		self.setWindowTitle('Menyisipkan Gambar')

		self.label1 = Qlabel()
		self.label1.setText('<b><font size=11>Demo Menampilkan Gambar dengan Qlabel</font></b>')

		self.label2 = Qlabel()
		self.label2.setText('<img src="ittp1.png">')

		layout = QVBoxLayout()
		layout.addWidget(self.label1)
		layout.addWidget(self.label2)
		self.setLayout(layout)

if__name__=='__main__':
	a = QApplication(sys.argv)

	form = DemoGambar()
	form.show()

	a.exec_()