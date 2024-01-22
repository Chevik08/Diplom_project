from entity.folder import Folder
from entity.history import History
from entity.file import File


class Container:
    def __init__(self,
                 folder: Folder,
                 file: File = None,
                 hist: History = None):

        self._folder = folder
        self._file = file
        self._history = hist

    @property
    def folder(self):
        return self._folder

    @folder.setter
    def folder(self, value):
        self._folder = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value

    def get_id(self):
        return self.__hash__()
