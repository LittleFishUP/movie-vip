# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

from PyQt5.QtWidgets import QMainWindow

from Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.pushButton5.clicked.connect(self.movieurl)
        
    def movieurl(self):
        b = self.textEdit222.toPlainText()
        a = "http://app.baiyug.cn:2019/vip/index.php?url="
        webbrowser.open(a+b)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
   
    ui = MainWindow()
    
    ui.show()
    sys.exit(app.exec_())

