class Folder:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._files = []

    def add_files(self, value):
        self._files.append(value)

    def clear_files(self):
        self._files.clear()

    def remove_file(self, value):
        if value in self._files:
            self._files.remove(value)

    def get_files(self):
        return self._files

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def gen_id(self):
        self._id = self.__hash__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
