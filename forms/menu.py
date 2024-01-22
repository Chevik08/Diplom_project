from entity.container import Container
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMenu, QInputDialog


class TableMenu(QMenu):
    def __init__(self, main, cat: list[Container]):
        super().__init__()
        self.main = main
        self.cat = cat
        self.addAction("Создать папку", self.create_folder)
        self.addAction("Обновить", self.update_table)

    @QtCore.pyqtSlot()
    def create_folder(self):
        new_folder = self.main.generate_new_folder()
        if new_folder:
            self.cat.append(new_folder)
            self.main.update_()
            self.main.update_files()

    @QtCore.pyqtSlot()
    def update_table(self):
        self.main.update_()


class FolderMenu(QMenu):
    def __init__(self, main, cat: list[Container]):
        super().__init__()
        self.main = main
        self.cat = cat
        self.current = None

        self.addAction("Добавить файл", self.add_file)
        self.addAction("Переименовать", self.rename)
        self.addAction("Удалить", self.delete_folder)
        self.addAction("Анализ")

    @QtCore.pyqtSlot()
    def add_file(self):
        new_file = self.main.generate_new_file(auto=False)
        new_cont = Container(file=new_file,
                             folder=self.current)
        for cont in self.cat:
            if cont.folder == self.current:
                cont.folder.add_files(new_file)

        self.cat.append(new_cont)
        self.main.update_()
        self.main.update_files()

    @QtCore.pyqtSlot()
    def rename(self):
        text, ok = QInputDialog.getText(self, "", "Введите название директории")
        if ok:
            if len(text) > 1:
                self.current.name = text
                self.main.update_()
                self.main.update_files()

    @QtCore.pyqtSlot()
    def delete_folder(self):
        for_remove = []
        if self.current in [i.folder for i in self.cat]:
            for cont in self.cat:
                if cont.folder.id == self.current.id:
                    for_remove.append(cont)

            for item in for_remove:
                self.cat.remove(item)

            self.main.update_()
            self.main.update_files()


class FileMenu(QMenu):
    def __init__(self, main, cat: list[Container]):
        super().__init__()
        self.main = main
        self.cat = cat
        self.current = None

        self.addAction("Открыть")
        self.addAction("Переименовать", self.rename)
        self.addAction("Удалить", self.delete_file)
        self.addAction("Анализ")

    @QtCore.pyqtSlot()
    def rename(self):
        text, ok = QInputDialog.getText(self, "", "Введите новое название файла")
        if ok:
            if len(text) > 1:
                self.current.name = text
                self.main.update_()
                self.main.update_files()

    @QtCore.pyqtSlot()
    def delete_file(self):
        # Удалить этот файл из его папки
        for cont in self.cat:
            if self.current in cont.folder.get_files():
                cont.folder.remove_file(self.current)

        if self.current in [i.file for i in self.cat]:
            for cont in self.cat:
                if cont.file == self.current:
                    self.cat.remove(cont)
                    self.main.update_()
                    self.main.update_files()
