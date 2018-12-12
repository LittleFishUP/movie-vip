import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWebEngineWidgets import *

def _fullScreenRequested( request ):
    request.accept()
    w.showFullScreen()

argvs = sys.argv
# 支援flash
argvs.append('--ppapi-flash-path=./pepflashplayer.dll')

app = QtWidgets.QApplication(argvs)
w = QWebEngineView()
w.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
w.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
w.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

w.page().fullScreenRequested.connect(_fullScreenRequested)

w.load(QtCore.QUrl('https://www.bilibili.com/video/av22192941/'))


w.show()
app.exec_()