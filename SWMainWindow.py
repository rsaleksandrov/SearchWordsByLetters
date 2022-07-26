"""
Поиск слов по буквам
SWMainWindow.py
(C) RSAleksandrov 2022
https://github.com/rsaleksandrov/SearchWordsByLetters
"""
from PyQt5 import QtWidgets, QtCore, QtGui
import prefixtree
from collections import deque


class SWMainWindow(QtWidgets.QWidget):
    __rusAlphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                     'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                     'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    def __init__(self, parent=None):
        # Initializate main window
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(622, 435)
        self.setMinimumSize(QtCore.QSize(622, 435))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Поиск слов по буквам')
        self.__vbox = QtWidgets.QVBoxLayout(self)
        self.__gpbParam = QtWidgets.QGroupBox(self)
        self.__gpbParam.setMinimumSize(QtCore.QSize(601, 104))
        self.__gpbParam.setMaximumSize(QtCore.QSize(16777215, 104))

        self.__gridLayout = QtWidgets.QGridLayout(self.__gpbParam)
        self.__lbChars = QtWidgets.QLabel(self.__gpbParam)
        self.__lbChars.setMinimumSize(QtCore.QSize(99, 30))
        self.__lbChars.setAlignment(QtCore.Qt.AlignRight |
                                    QtCore.Qt.AlignTrailing |
                                    QtCore.Qt.AlignVCenter)
        self.__gridLayout.addWidget(self.__lbChars, 0, 0, 1, 1)
        self.__leChars = QtWidgets.QLineEdit(self.__gpbParam)
        self.__leChars.setMinimumSize(QtCore.QSize(364, 27))
        self.__gridLayout.addWidget(self.__leChars, 0, 1, 1, 1)
        self.__pbFindWords = QtWidgets.QPushButton(self.__gpbParam)
        self.__pbFindWords.setMinimumSize(QtCore.QSize(106, 29))
        self.__pbFindWords.setObjectName("pushButton")
        self.__gridLayout.addWidget(self.__pbFindWords, 0, 2, 1, 1)
        self.__lbWordLen = QtWidgets.QLabel(self.__gpbParam)
        self.__lbWordLen.setMinimumSize(QtCore.QSize(99, 30))
        self.__lbWordLen.setAlignment(QtCore.Qt.AlignRight |
                                      QtCore.Qt.AlignTrailing |
                                      QtCore.Qt.AlignVCenter)
        self.__gridLayout.addWidget(self.__lbWordLen, 1, 0, 1, 1)
        self.__spbWordLen = QtWidgets.QSpinBox(self.__gpbParam)
        self.__spbWordLen.setMinimumSize(QtCore.QSize(364, 27))
        self.__spbWordLen.setMaximum(20)
        self.__spbWordLen.setProperty("value", 3)
        self.__gridLayout.addWidget(self.__spbWordLen, 1, 1, 1, 1)
        self.__vbox.addWidget(self.__gpbParam)
        self.__gpbResult = QtWidgets.QGroupBox(self)
        self.__gpbResult.setMinimumSize(QtCore.QSize(601, 291))
        self.__vbox2 = QtWidgets.QVBoxLayout(self.__gpbResult)
        self.__lvResult = QtWidgets.QListWidget(self.__gpbResult)
        self.__lvResult.setMinimumSize(QtCore.QSize(584, 266))
        self.__vbox2.addWidget(self.__lvResult)
        self.__vbox.addWidget(self.__gpbResult)

        self.__gpbParam.setTitle('Исходные данные')
        self.__lbChars.setText('Буквы слова')
        self.__lbWordLen.setText('Длина слова')
        self.__pbFindWords.setText('Найти слова')
        self.__gpbResult.setTitle('Результаты')

        self.__pbFindWords.clicked.connect(self.__findWord)

        # Load words
        self.__pt = prefixtree.PrefixTree()
        self.__pt.loadFromTxt('data.txt')

    def __defDupChar(self, word, chars) -> []:
        res = []
        tmpword = list(word)
        for ch in chars:
            if ch not in tmpword:
                res.append(ch)
            else:
                tmpword.remove(ch)

        return res

    def __findWord(self, e):
        chars = []
        resword = []
        for ch in self.__leChars.text():
            if ch in self.__rusAlphabet:
                chars.append(ch)
        stack = deque(set(chars))
        wordLen = self.__spbWordLen.value()
        while len(stack) > 0:
            curword = stack.popleft()
            tmpchars = self.__defDupChar(curword, chars)
            for ch in tmpchars:
                tmpword = curword + ch
                corr, pcorr = self.__pt.checkWord(tmpword)
                if len(tmpword) == wordLen and corr:
                    resword.append(tmpword)
                elif len(tmpword) < wordLen and pcorr:
                    stack.append(tmpword)
        self.__lvResult.clear()
        self.__lvResult.addItems(set(resword))
        pass
