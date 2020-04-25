# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame


class WebUI(object):
    def __init__(self, url='https://google.com'):
        w = 1280
        h = 960

        self.url = url
        self.app = QApplication([])
        self.app.setApplicationName('test')
        self.app.setWindowIcon(QIcon('../icon.svg'))
        self.view = QWebEngineView(self.app.activeModalWidget())
        self.view.window().resize(w, h)

    def run_gui(self):
        self.view.load(QUrl(self.url))

        change_setting = self.view.page().settings().setAttribute
        settings = QWebEngineSettings
        change_setting(settings.LocalStorageEnabled, True)
        change_setting(settings.PluginsEnabled, True)
        change_setting(settings.DnsPrefetchEnabled, True)

        self.view.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    WebUI().run_gui()
