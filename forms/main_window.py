# Form implementation generated from reading ui file 'ui/main_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 683)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.main_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.main_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.tree_page = QtWidgets.QWidget()
        self.tree_page.setObjectName("tree_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tree_page)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.treeView = QtWidgets.QTreeView(parent=self.tree_page)
        self.treeView.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeView.setAcceptDrops(False)
        self.treeView.setObjectName("treeView")
        self.gridLayout_5.addWidget(self.treeView, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.tree_page)
        self.history_page = QtWidgets.QWidget()
        self.history_page.setObjectName("history_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.history_page)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget = QtWidgets.QWidget(parent=self.history_page)
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 6, 0, 1, 1)
        self.doctor_name_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.doctor_name_lnedit.setObjectName("doctor_name_lnedit")
        self.gridLayout_8.addWidget(self.doctor_name_lnedit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 2, 1, 1, 1)
        self.patient_name_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_name_lnedit.sizePolicy().hasHeightForWidth())
        self.patient_name_lnedit.setSizePolicy(sizePolicy)
        self.patient_name_lnedit.setObjectName("patient_name_lnedit")
        self.gridLayout_8.addWidget(self.patient_name_lnedit, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 12, 1, 1, 1)
        self.height_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.height_lnedit.setObjectName("height_lnedit")
        self.gridLayout_8.addWidget(self.height_lnedit, 9, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 8, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 8, 0, 1, 1)
        self.address_hospital_pltext = QtWidgets.QPlainTextEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address_hospital_pltext.sizePolicy().hasHeightForWidth())
        self.address_hospital_pltext.setSizePolicy(sizePolicy)
        self.address_hospital_pltext.setObjectName("address_hospital_pltext")
        self.gridLayout_8.addWidget(self.address_hospital_pltext, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.info_pltext = QtWidgets.QPlainTextEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_pltext.sizePolicy().hasHeightForWidth())
        self.info_pltext.setSizePolicy(sizePolicy)
        self.info_pltext.setObjectName("info_pltext")
        self.gridLayout_8.addWidget(self.info_pltext, 13, 1, 4, 1)
        self.age_spinbox = QtWidgets.QSpinBox(parent=self.widget)
        self.age_spinbox.setObjectName("age_spinbox")
        self.gridLayout_8.addWidget(self.age_spinbox, 7, 0, 1, 1)
        self.date_dateedit = QtWidgets.QDateEdit(parent=self.widget)
        self.date_dateedit.setObjectName("date_dateedit")
        self.gridLayout_8.addWidget(self.date_dateedit, 7, 1, 1, 1)
        self.patient_surname_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.patient_surname_lnedit.setObjectName("patient_surname_lnedit")
        self.gridLayout_8.addWidget(self.patient_surname_lnedit, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 4, 0, 1, 1)
        self.doctor_surname_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.doctor_surname_lnedit.setObjectName("doctor_surname_lnedit")
        self.gridLayout_8.addWidget(self.doctor_surname_lnedit, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 4, 1, 1, 1)
        self.patient_patr_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.patient_patr_lnedit.setObjectName("patient_patr_lnedit")
        self.gridLayout_8.addWidget(self.patient_patr_lnedit, 5, 0, 1, 1)
        self.doctoe_patr_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.doctoe_patr_lnedit.setObjectName("doctoe_patr_lnedit")
        self.gridLayout_8.addWidget(self.doctoe_patr_lnedit, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 1, 1, 1)
        self.tag_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.tag_lnedit.setObjectName("tag_lnedit")
        self.gridLayout_8.addWidget(self.tag_lnedit, 11, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 2, 1, 1)
        self.history_pltext = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.history_pltext.setObjectName("history_pltext")
        self.gridLayout_8.addWidget(self.history_pltext, 1, 2, 19, 1)
        self.job_pltext = QtWidgets.QPlainTextEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_pltext.sizePolicy().hasHeightForWidth())
        self.job_pltext.setSizePolicy(sizePolicy)
        self.job_pltext.setObjectName("job_pltext")
        self.gridLayout_8.addWidget(self.job_pltext, 13, 0, 4, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 18, 1, 1, 1)
        self.weight_lnedit = QtWidgets.QLineEdit(parent=self.widget)
        self.weight_lnedit.setObjectName("weight_lnedit")
        self.gridLayout_8.addWidget(self.weight_lnedit, 11, 0, 1, 1)
        self.patient_address_pltext = QtWidgets.QPlainTextEdit(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_address_pltext.sizePolicy().hasHeightForWidth())
        self.patient_address_pltext.setSizePolicy(sizePolicy)
        self.patient_address_pltext.setObjectName("patient_address_pltext")
        self.gridLayout_8.addWidget(self.patient_address_pltext, 19, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 18, 0, 1, 1)
        self.diagnosis_pledit = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.diagnosis_pledit.setObjectName("diagnosis_pledit")
        self.gridLayout_8.addWidget(self.diagnosis_pledit, 19, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 10, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 10, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 12, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_btn = QtWidgets.QPushButton(parent=self.widget)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_2.addWidget(self.clear_btn)
        self.save_btn = QtWidgets.QPushButton(parent=self.widget)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 20, 0, 1, 3)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.history_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.settings_page)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_16 = QtWidgets.QLabel(parent=self.settings_page)
        self.label_16.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.settings_page)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 1, 0, 1, 1)
        self.header_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.header_widget.setObjectName("header_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.header_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_btn = QtWidgets.QPushButton(parent=self.header_widget)
        self.file_btn.setObjectName("file_btn")
        self.horizontalLayout.addWidget(self.file_btn)
        self.history_btn = QtWidgets.QPushButton(parent=self.header_widget)
        self.history_btn.setObjectName("history_btn")
        self.horizontalLayout.addWidget(self.history_btn)
        self.settings_btn = QtWidgets.QPushButton(parent=self.header_widget)
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout.addWidget(self.settings_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.header_widget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Дата приёма"))
        self.label_10.setText(_translate("MainWindow", "Возраст"))
        self.label_4.setText(_translate("MainWindow", "Фамилия пациента"))
        self.label_5.setText(_translate("MainWindow", "Фамилия врача"))
        self.label_13.setText(_translate("MainWindow", "Дополнительные заметки"))
        self.label_14.setText(_translate("MainWindow", "Адрес больницы"))
        self.label_8.setText(_translate("MainWindow", "Рост"))
        self.label.setText(_translate("MainWindow", "Имя пациента"))
        self.label_6.setText(_translate("MainWindow", "Отчество пациента"))
        self.label_7.setText(_translate("MainWindow", "Отчество врача"))
        self.label_2.setText(_translate("MainWindow", "Имя врача"))
        self.label_3.setText(_translate("MainWindow", "История болезни"))
        self.label_17.setText(_translate("MainWindow", "Предположения о диагнозе"))
        self.label_15.setText(_translate("MainWindow", "Адрес проживания"))
        self.label_18.setText(_translate("MainWindow", "Тег"))
        self.label_12.setText(_translate("MainWindow", "Вес"))
        self.label_11.setText(_translate("MainWindow", "Должность"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))
        self.label_16.setText(_translate("MainWindow", "В разработке"))
        self.file_btn.setText(_translate("MainWindow", "Файлы"))
        self.history_btn.setText(_translate("MainWindow", "История болезни"))
        self.settings_btn.setText(_translate("MainWindow", "Настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
