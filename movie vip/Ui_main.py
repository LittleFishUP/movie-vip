# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\movie vip\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit222 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit222.setGeometry(QtCore.QRect(140, 230, 541, 31))
        self.textEdit222.setObjectName("textEdit222")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 230, 71, 21))
        self.label.setObjectName("label")
        self.pushButton5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton5.setGeometry(QtCore.QRect(330, 360, 93, 28))
        self.pushButton5.setObjectName("pushButton5")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 561, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe 仿宋 Std R")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "vip视频破解软件 by.向"))
        self.label.setText(_translate("MainWindow", "视频地址："))
        self.pushButton5.setText(_translate("MainWindow", "播放视频"))
        self.label_2.setText(_translate("MainWindow", "娱乐用，想不充vip的可以用用。\n"
" ps：懒不想做界面不渲染了"))

    
        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

