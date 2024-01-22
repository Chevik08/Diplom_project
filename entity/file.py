class File:
    def __init__(self, id, name, tag, date):
        self.__id = id
        self._name = name
        self._tag = tag
        self._date = date
        self._folder = None

    def set_folder(self, folder):
        self._folder = folder

    def get_folder(self):
        return self._folder

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def gen_id(self):
        self.__id = self.__hash__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value