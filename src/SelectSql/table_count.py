from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from src.UtilsSql.connect_db import ConnectDb


class TableCount(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_count()

    def create_table_count(self):
        self.table_count = QTableWidget(1, 4)
        self.table_count.setMaximumHeight(30)
        self.table_count.setColumnWidth(0, 150)
        self.table_count.setColumnWidth(1, 50)
        self.table_count.setColumnWidth(2, 100)
        self.table_count.setColumnWidth(3, 120)
        self.table_count.horizontalHeader().setVisible(False)
        self.table_count.verticalHeader().setVisible(False)
        self.create_combo_count()

    def create_combo_count(self):
        row = self.table_count.rowCount()
        self.comboCount = QComboBox()
        self.comboCount.addItem("Select field")
        self.comboCount.addItem("(*)")
        for item in self.get_list_fields():
            item = "(" + item + ")"
            self.comboCount.addItem(item)
        self.table_count.setCellWidget(0, 0, self.comboCount)
        self.comboCount.currentIndexChanged.connect(self.get_combo_count)
        first_item = QtGui.QStandardItem(row)
        first_item.setSelectable(False)

    def get_combo_count(self):
        current_text = self.comboCount.currentText()
        if current_text != "Select field":
            self.create_count_label_as()
            self.create_count_lineedit_as()
            self.create_combo_count_fields()
            self.comboCount.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.table_count.removeCellWidget(0, 1)
            self.table_count.removeCellWidget(0, 2)
            self.table_count.removeCellWidget(0, 3)
            self.comboCount.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_count_label_as(self):
        self.count_label_as = QLabel("AS")
        self.count_label_as.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.count_label_as.setStyleSheet("QLabel { color: black; }")
        self.table_count.setCellWidget(0, 1, self.count_label_as)

    def create_count_lineedit_as(self):
        self.count_lineedit_as = QLineEdit()
        self.count_lineedit_as.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.count_lineedit_as.textChanged.connect(self.changed_count_lineedit_as)
        self.count_lineedit_as.setStyleSheet(self.style_qLine)
        self.table_count.setCellWidget(0, 2, self.count_lineedit_as)

    def changed_count_lineedit_as(self):
        texto = self.count_lineedit_as.text()
        if len(texto) is not None:
            self.count_label_as.setStyleSheet("QLabel { color: black; }")
            self.count_lineedit_as.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.count_label_as.setStyleSheet("QLabel { color: green; }")
            self.count_lineedit_as.setStyleSheet(self.style_qLine1)

    def create_combo_count_fields(self):
        self.combo_count_fields = QComboBox()
        self.combo_count_fields.addItem("Select field")
        for item in ConnectDb.get_list_fields(self):
            item = "," + item
            self.combo_count_fields.addItem(item)
        self.table_count.setCellWidget(0, 3, self.combo_count_fields)
        self.combo_count_fields.currentIndexChanged.connect(self.get_combo_count_fields)

    def get_combo_count_fields(self):
        current_text = self.combo_count_fields.currentText()
        if current_text != "Select field":
            self.combo_count_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_count_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
