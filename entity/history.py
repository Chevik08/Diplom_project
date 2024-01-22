

class History:
    def __init__(self,
                 name: str = None,
                 surname: str = None,
                 patronymic: str = None,
                 age: int = 0,
                 height: float = 0.0,
                 weight: float = 0.0,
                 date: str = None,
                 live_address: str = None,
                 job: str = None,
                 doctor_name: str = None,
                 doctor_surname: str = None,
                 doctor_patronymic: str = None,
                 address: str = None,
                 diagnosis: str = None,
                 info: str = None,
                 text: str = None):
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._age = age
        self._height = height
        self._weight = weight
        self._date = date
        self._live_address = live_address
        self._job = job
        self._doctor_name = doctor_name
        self._doctor_surname = doctor_surname
        self._doctor_patronymic = doctor_patronymic
        self._address = address
        self._diagnosis = diagnosis
        self._info = info
        self._text = text
        self._delim = [',', ';', ':', '/', '-']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value):
        self._patronymic = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def date(self):
        self._date_checker()
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def live_address(self):
        return self._live_address

    @live_address.setter
    def live_address(self, value):
        self._live_address = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value

    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value

    @property
    def doctor_surname(self):
        return self._doctor_surname

    @doctor_surname.setter
    def doctor_surname(self, value):
        self._doctor_surname = value

    @property
    def doctor_patronymic(self):
        return self._doctor_patronymic

    @doctor_patronymic.setter
    def doctor_patronymic(self, value):
        self._doctor_patronymic = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def _date_checker(self):
        """Метод проверки формата даты"""
        if self._date is None:
            return
        for delim in self._delim:
            if delim in self._date:
                self._date = self._date.replace(delim, '.')

    def __str__(self):
        return f"История болезни\n" \
               f"Пациент:\n" \
               f"- Имя: {self.name}\n" \
               f"- Фамилия: {self.surname}\n" \
               f"- Отчество: {self.patronymic}\n" \
               f"Дата приёма: {self.date}"


if __name__ == '__main__':
    h = History(date="22.22.2024", name="Никита")
    print(h)
