"""
Поиск слов по буквам
main.py
(C) RSAleksandrov 2022
https://github.com/rsaleksandrov/SearchWordsByLetters
"""
import sys
from PyQt5 import QtWidgets, QtGui
import SWMainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icon.png"),
                   QtGui.QIcon.Normal,
                   QtGui.QIcon.Off)
    app.setWindowIcon(icon)

    win = SWMainWindow.SWMainWindow()
    win.show()
    sys.exit(app.exec_())
