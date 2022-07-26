import pickle


class PrefixTreeNode:
    def __init__(self):
        self.edges = dict()
        self.isTerminate = False


class PrefixTree:
    __version = 'PT_V1'

    def __init__(self):
        self.head = PrefixTreeNode()

    def addWord(self, word):
        if len(word) == 0:
            return

        word = word.lower()
        curNode = self.head
        for i in range(len(word)):
            if word[i] not in curNode.edges:
                curNode.edges[word[i]] = PrefixTreeNode()
            curNode = curNode.edges[word[i]]
        curNode.isTerminate = True

    def checkWord(self, word) -> [bool, bool]:
        if len(word) == 0:
            return False, False

        curnode = self.head
        for i in range(len(word)):
            if word[i] not in curnode.edges:
                return False, False
            curnode = curnode.edges[word[i]]

        return curnode.isTerminate, True

    def loadFromTxt(self, filename: str, encoding='utf-8'):
        f = open(filename, 'r', encoding=encoding)
        for line in f:
            line = line.strip('\n')
            self.addWord(line)
        f.close()
        pass

    def loadFromBin(self, filename: str):
        f = open(filename, 'rb')
        unpkl = pickle.Unpickler(f)
        tmpver = unpkl.load()
        if tmpver != self.__version:
            f.close()
            raise Exception(f'Uncorrected version file {filename}')
        self.head = unpkl.load()
        f.close()
        pass

    def saveToTxt(self, filename: str):
        pass

    def saveToBin(self, filename: str):
        f = open(filename, 'wb')
        pkl = pickle.Pickler(f)
        pkl.dump(self.__version)
        pkl.dump(self.head)
        f.close()
        pass
