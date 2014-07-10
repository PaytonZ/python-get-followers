'''
Initializer for autogenerated GUItest.property
'''

from GuiGenerated import Ui_MainWindow
from PySide import QtCore, QtGui
import sys

class ControlMainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(ControlMainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mySW = ControlMainWindow()
	mySW.show()
	sys.exit(app.exec_())