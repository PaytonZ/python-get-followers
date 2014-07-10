'''
Initializer for autogenerated GUItest.property
'''

from GuiGenerated import Ui_MainWindow
from PySide import QtCore, QtGui
import sys

def listenerSaveButton(stri):
	if stri != "":
		mySW.ui.saveBt.setEnabled(True)
	else:
		mySW.ui.saveBt.setEnabled(False)

class ControlMainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(ControlMainWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def customSetUp(self):
		QtCore.QObject.connect(self.ui.clientNameText, QtCore.SIGNAL("textEdited(QString)"), listenerSaveButton)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mySW = ControlMainWindow()
	mySW.customSetUp()
	mySW.show()
	sys.exit(app.exec_())