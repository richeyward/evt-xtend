#!/usr/bin/env python3
from PyQt6 import QtWidgets
from windows.mainwindow import MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.move(1400, 300)
window.show() 
app.exec()
