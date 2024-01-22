import datetime
import enum
import os
import sys

from forms.menu import TableMenu, FileMenu, FolderMenu
from forms.main_window import Ui_MainWindow
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QAbstractItemView, \
    QInputDialog, QPlainTextEdit, QLineEdit, QSpinBox, \
    QDateEdit, QMessageBox
from PyQt6.QtGui import QStandardItem, QStandardItemModel, \
    QFont, QIcon
from json_converter import json_to_container, container_to_json
from exception_hook import excepthook
from entity.file import File
from entity.folder import Folder
from entity.container import Container
from entity.history import History

sys.excepthook = excepthook


class RES(enum.Enum):
    FOLDER = "folder"
    FILE = "file"
    IMAGE = "image"


class StandardItem(QStandardItem, QAbstractItemView):
    def __init__(self, text: str, style: RES, obj=None):
        super().__init__()

        self.get_text = text
        self._object = obj

        font = QFont("Times New Roman", 14)

        self.setEditable(False)
        self.setIcon(QIcon(f"icons/{style.value}.png"))
        self.setFont(font)
        self.setText(text)

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, value):
        self._object = value

    def __hash__(self):
        return hash(self.object)


class StandardText(QStandardItem, QAbstractItemView):
    def __init__(self, text: str):
        super().__init__()
        font = QFont("Times New Roman", 14)
        self.setEditable(False)
        self.setFont(font)
        self.setText(text)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.left_margin = 100
        self.font_correct = 12
        self.setWindowTitle("МедХелпер")

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Файл", "Тег", "Дата создания"])
        self.treeView.header().setVisible(True)
        self.treeView.customContextMenuRequested.connect(self.open_menu)
        self.root = self.model.invisibleRootItem()
        self.catalog = []
        self.storage_path = "./memory"
        self.actual_history = None

        self.table_menu = TableMenu(self, self.catalog)
        self.folder_menu = FolderMenu(self, self.catalog)
        self.file_menu = FileMenu(self, self.catalog)

        self.file_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tree_page))
        self.history_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.history_page))
        self.settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page))
        self.save_btn.clicked.connect(self.save_data)
        self.clear_btn.clicked.connect(self.clear_history)
        self.treeView.doubleClicked.connect(self.switch_and_fill_history)

        self.read_data(self.storage_path)

        self.folder = []
        self.tree = {}
        self.interface_tree = {}
        self.update_()

    def clear_history(self):
        for item in self.widget.children():
            if isinstance(item, QPlainTextEdit) or \
                    isinstance(item, QLineEdit) or \
                    isinstance(item, QSpinBox):
                item.clear()
            if isinstance(item, QDateEdit):
                date = datetime.date.today()
                year, month, day = date.strftime("%Y.%m.%d").split(".")
                item.setDate(QtCore.QDate(int(year), int(month), int(day)))

    def switch_and_fill_history(self, index: QtCore.QModelIndex):
        if self.model.itemFromIndex(index).text() is None:
            return
        if self.model.itemFromIndex(index).text() not in [i.file.name for i in self.catalog]:
            return

        if isinstance(self.model.itemFromIndex(index).object, File):
            self.stackedWidget.setCurrentWidget(self.history_page)
            file: File = self.model.itemFromIndex(index).object
            for cat in self.catalog:
                if cat.file and cat.file.id == file.id:
                    self.data_from_file_to_history(cat)
                    break

    def save_data(self):
        if self.patient_name_lnedit.text() == "" or \
                self.patient_surname_lnedit.text() == "":
            self.show_error("У пациента не указаны имя или фамилия")
            return
        elif self.actual_history is None:
            print("Создание новой истории в процессе")
            return
        else:
            for cond in self.catalog:
                if cond.file and cond.file.id == self.actual_history:
                    if self.data_from_history_to_file(cond):
                        self.stackedWidget.setCurrentWidget(self.tree_page)
                        self.actual_history = None

        self.update_()
        self.update_files()

    def data_from_file_to_history(self, cont: Container):
        hist = cont.history
        # Если в файле нет никакой истории болезни
        if not hist:
            self.actual_history = cont.file.id
            self.clear_history()
            return

        self.patient_name_lnedit.setText(hist.name)
        self.patient_surname_lnedit.setText(hist.surname)
        self.patient_patr_lnedit.setText(hist.patronymic)
        self.height_lnedit.setText(str(hist.height))
        self.weight_lnedit.setText(str(hist.weight))
        self.age_spinbox.setValue(hist.age)
        self.tag_lnedit.setText(cont.file.tag)
        self.doctor_name_lnedit.setText(hist.doctor_name)
        self.doctor_surname_lnedit.setText(hist.doctor_surname)
        self.doctoe_patr_lnedit.setText(hist.doctor_patronymic)
        date = hist.date.split(".")
        self.date_dateedit.setDate(QtCore.QDate(int(date[2]),
                                                int(date[1]),
                                                int(date[0])))

        self.patient_address_pltext.clear()
        self.patient_address_pltext.appendPlainText(hist.live_address)
        self.job_pltext.clear()
        self.job_pltext.appendPlainText(hist.job)
        self.diagnosis_pledit.clear()
        self.diagnosis_pledit.appendPlainText(hist.diagnosis)
        self.address_hospital_pltext.clear()
        self.address_hospital_pltext.appendPlainText(hist.address)
        self.info_pltext.clear()
        self.info_pltext.appendPlainText(hist.info)
        self.history_pltext.clear()
        self.history_pltext.appendPlainText(hist.text)
        self.actual_history = cont.file.id

    def data_from_history_to_file(self, cond: Container) -> bool:
        # Валидация полей
        try:
            float(self.height_lnedit.text())
            float(self.weight_lnedit.text())
        except ValueError:
            self.show_error("Неверный формат роста или веса")
            return False

        try:
            int(self.age_spinbox.value())
        except ValueError:
            self.show_error("Неверный формат возраста")
            return False

        hist = cond.history
        file = cond.file
        if not hist:
            hist = History()
        hist.name = self.patient_name_lnedit.text()
        hist.surname = self.patient_surname_lnedit.text()
        hist.patronymic = self.patient_patr_lnedit.text()
        hist.height = float(self.height_lnedit.text())
        hist.weight = float(self.weight_lnedit.text())
        hist.age = int(self.age_spinbox.value())
        hist.doctor_name = self.doctor_name_lnedit.text()
        hist.doctor_surname = self.doctor_surname_lnedit.text()
        hist.doctor_patronymic = self.doctoe_patr_lnedit.text()
        hist.date = self.date_dateedit.text()
        hist.diagnosis = self.diagnosis_pledit.toPlainText()
        hist.info = self.info_pltext.toPlainText()
        hist.text = self.history_pltext.toPlainText()
        hist.address = self.address_hospital_pltext.toPlainText()
        hist.job = self.job_pltext.toPlainText()
        hist.live_address = self.patient_address_pltext.toPlainText()
        file.tag = self.tag_lnedit.text()
        cond.history = hist
        return True

    def update_(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["Файл", "Тег", "Дата создания"])
        self.link_everything()
        self.create_tree_from_data()
        self.virtual_tree_to_interface_tree()
        self.update_file_manager()

    def update_file_manager(self):
        # Вставка объектов в файловый менеджер
        for fold_key in sorted(self.interface_tree.keys()):
            for file in self.interface_tree[fold_key]:
                if file is not None:
                    fold_key.appendRow([file,
                                        StandardText(str(file.object.tag)),
                                        StandardText(str(file.object.date))])
            self.model.appendRow(fold_key)

        self.treeView.setModel(self.model)

        big = 0
        for col in range(self.treeView.model().rowCount()):
            length = len(str(self.model.item(col, 0).get_text)) * self.font_correct
            if length > big:
                big = length

        self.treeView.header().resizeSection(0, big + self.left_margin)

    def virtual_tree_to_interface_tree(self):
        self.interface_tree.clear()
        for key in self.tree.keys():
            item = StandardItem(key.name, RES.FOLDER, key)
            for file in self.tree[key]:
                if file is None:
                    self.interface_tree[item] = [None]
                    continue
                f_item = StandardItem(file.name, RES.FILE, file)
                if item not in self.interface_tree.keys():
                    self.interface_tree[item] = [f_item]
                else:
                    self.interface_tree[item].append(f_item)

    def create_tree_from_data(self):
        self.tree.clear()
        self.folder.clear()
        for cont in self.catalog:
            if cont.folder.id not in [i.id for i in self.folder]:
                self.folder.append(cont.folder)

        for fold in self.folder:
            if fold not in self.tree.keys():
                self.tree[fold] = []
            for file in fold.get_files():
                self.tree[fold].append(file)
            if len(self.tree[fold]) == 0:
                self.tree[fold].append(None)

    def read_data(self, path):
        list_dir = os.listdir(path=path)
        for file in list_dir:
            j_cont = json_to_container(path + "/" + file)
            self.catalog.append(j_cont)

    def link_everything(self):
        for i in range(len(self.catalog)):
            for j in range(len(self.catalog)):
                # Связываем все файлы и папки между собой
                if self.catalog[j].file not in self.catalog[i].folder.get_files() and \
                        self.catalog[i].folder.id == self.catalog[j].folder.id:
                    self.catalog[i].folder.add_files(self.catalog[j].file)

                    if self.catalog[j].file:
                        self.catalog[j].file.set_folder(self.catalog[i].folder)

    def open_menu(self, pos):
        idx = self.treeView.indexAt(pos)
        item = self.model.itemFromIndex(idx)
        if isinstance(item, StandardText):
            return

        if item is None:
            self.table_menu.exec(self.treeView.mapToGlobal(pos))
        elif isinstance(item.object, File):
            self.file_menu.current = item.object
            self.file_menu.exec(self.treeView.mapToGlobal(pos))
        elif isinstance(item.object, Folder):
            self.folder_menu.current = item.object
            self.folder_menu.exec(self.treeView.mapToGlobal(pos))
        else:
            raise ValueError("Right click on unknown object!")

    def generate_new_folder(self):
        name, ok = QInputDialog.getText(self, "", "Имя новой папки")
        if not ok:
            return None
        if name != "" and len(name) > 1:
            new_folder = Folder(id=0, name=name)
        else:
            new_folder = Folder(id=0, name="Новая папка")
        new_folder.gen_id()
        new_file = self.generate_new_file(True)
        new_cont = Container(folder=new_folder,
                             file=new_file)
        return new_cont

    def generate_new_file(self, auto=True):
        if not auto:
            name, ok = QInputDialog.getText(self, "", "Имя нового файла")
        else:
            name = "Первое посещение"

        new_file = File(id=0,
                        name=name,
                        tag="",
                        date="20.12.2023")
        new_file.gen_id()
        return new_file

    def update_files(self):
        # FIXME: Добавить безопасность
        files = os.listdir(self.storage_path)
        for file in files:
            os.remove(self.storage_path + "/" + file)

        for cont in self.catalog:
            if cont.file:
                container_to_json(self.storage_path + f"/file_{cont.file.id}.json", cont)
            elif cont.folder:
                container_to_json(self.storage_path + f"/folder_{cont.folder.id}.json", cont)
            else:
                container_to_json(self.storage_path + f"/empty_{cont.get_id()}.json", cont)

    @staticmethod
    def show_error(message: str):
        """
        Метод порождения сообщения об ошибке;
        :param message: Содержание ошибки
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.icon(msg).Critical)
        msg.setText("Ошибка                                                    ")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec()
