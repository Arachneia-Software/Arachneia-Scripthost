from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
import sys
import os

class TabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        self.setTabBar(self.TabBar(self))
        self.setTabPosition(QTabWidget.TabPosition.West)
        self.load_tabs_from_file('tabs.txt')

    def load_tabs_from_file(self, filename):
        if not os.path.exists(filename):
            return
        
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('<tab>'):
                    tab_name = line[5:].strip()
                    self.addTab(QWidget(), tab_name)

    class TabBar(QtWidgets.QTabBar):
        def tabSizeHint(self, index):
            s = QtWidgets.QTabBar.tabSizeHint(self, index)
            s.transpose()
            s.setHeight(int(s.height() * 1.3))  # We increase the height of each panel in which the tab name is placed
            return s

        def paintEvent(self, event):
            painter = QtWidgets.QStylePainter(self)
            opt = QtWidgets.QStyleOptionTab()

            for i in range(self.count()):
                self.initStyleOption(opt, i)
                painter.drawControl(QStyle.ControlElement.CE_TabBarTabShape, opt)
                painter.save()

                r = self.tabRect(i)
                r.moveLeft(r.left() + 20)  # Move the rectangle to the left to align to the left edge
                opt.rect = r

                painter.translate(r.topLeft())
                painter.drawText(QtCore.QRect(0, 0, r.width(), r.height()), QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, opt.text)
                painter.restore()

if __name__ == '__main__':
    app = QApplication([])
    tab = TabWidget()
    tab.setGeometry(0, 0, 1000, 1000)
    tab.show()

    sys.exit(app.exec())
