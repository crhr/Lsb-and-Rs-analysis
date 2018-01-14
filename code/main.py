# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
import sys
import ui

reload(sys)
app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
win = ui.Ui_MainWindow()
win.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())