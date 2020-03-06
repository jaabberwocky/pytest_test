from tobiasPackage.prettyFunctions import *

class TobiasClass:
    def __init__(self, name):
        self.name = name
        self._num_chars = len(self.name)
        self._chars = [s for s in self.name]

    def getChars(self):
        return self._chars

    def getNumChars(self):
        return self._num_chars


    