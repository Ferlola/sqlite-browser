from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QColor
from src.UtilsSql.connect_db import ConnectDb
from src.UtilsSql.create_model import create_model


class TableFields2(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_fields2()

    def current_text_color_fields2(self, row, column, current_text):
        current_text.setForeground(QColor("green"))
        self.table_fields2.setItem(row, column, QTableWidgetItem(current_text))

    def create_table_fields2(self):
        self.table_fields2 = QTableWidget(1, 6)
        self.table_fields2.setMaximumHeight(30)
        self.table_fields2.setColumnWidth(0, 150)
        self.table_fields2.setColumnWidth(1, 370)
        self.table_fields2.setColumnWidth(2, 120)
        self.table_fields2.setColumnWidth(3, 120)
        self.table_fields2.setColumnWidth(4, 50)
        self.table_fields2.setColumnWidth(5, 50)
        self.table_fields2.horizontalHeader().setVisible(False)
        self.table_fields2.verticalHeader().setVisible(False)
        self.create_combobox_all2()

    def create_combobox_all2(self):
        self.models_fields2 = {}
        row = self.table_fields2.rowCount()
        self.combo_fields2 = QtWidgets.QComboBox()
        model = create_model(ConnectDb.get_list_all(self))
        self.combo_fields2.setModel(model)
        model.itemChanged.connect(lambda _, row=row: self.on_item_changed_all2(row))
        item = QTableWidgetItem()
        self.table_fields2.setItem(0, 1, item)
        self.models_fields2[row] = model
        self.table_fields2.setCellWidget(0, 0, self.combo_fields2)
        firstItem = QtGui.QStandardItem("Select field/s")
        model.setItem(0, firstItem)

    def on_item_changed_all2(self, tableRow):
        model = self.models_fields2[tableRow]
        self.items_checked2 = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == Qt.CheckState.Checked:
                first_string = model.item(row).text().split(",")[-1]
                self.items_checked2.append(first_string)
            for item in self.items_checked2:
                item = QTableWidgetItem(item)
                self.current_text_color_fields2(0, 1, item)
        self.itemsFieldsAll2 = ", ".join(self.items_checked2)
        if not self.items_checked2:
            item = QTableWidgetItem()
            self.table_fields2.setItem(0, 1, item)
            self.table_fields2.removeCellWidget(0, 2)
            self.table_fields2.removeCellWidget(0, 3)
            self.table_fields2.removeCellWidget(0, 4)
            self.table_fields2.removeCellWidget(0, 5)
            self.table_fields2.removeCellWidget(0, 6)
        else:
            self.create_combo_fields2_count()
            self.create_label_as2()
            self.create_lineedit_as2()
            self.table_fields2.item(0, 1).setText(", ".join(self.items_checked2))

    def create_combo_fields2_count(self):
        self.combo_fields2_count = QComboBox()
        self.combo_fields2_count.addItems(["count/avg/sum", ",COUNT", ",AVG", ",SUM"])
        self.table_fields2.setCellWidget(0, 2, self.combo_fields2_count)
        self.combo_fields2_count.currentIndexChanged.connect(
            self.get_combo_fields2_count
        )

    def get_combo_fields2_count(self):
        current_text = self.combo_fields2_count.currentText()
        if current_text != "count/avg/sum":
            self.table_fields2.setColumnWidth(2, 100)
            self.table_fields2.setColumnWidth(3, 140)
            self.create_combo_all2_fields2_count()
            self.combo_fields2_count.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_fields2.removeCellWidget(0, 3)
            self.table_fields2.setColumnWidth(2, 120)
            self.table_fields2.setColumnWidth(3, 120)
            self.combo_fields2_count.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_all2_fields2_count(self):
        self.combo_all2_fields2_count = QComboBox()
        self.combo_all2_fields2_count.addItem("(*)")
        self.combo_all2_fields2_count.addItems(self.get_list_count())  #
        self.combo_all2_fields2_count.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_fields2.setCellWidget(0, 3, self.combo_all2_fields2_count)

    def create_lineedit_as2(self):
        self.lineedit_as2 = QLineEdit()
        self.lineedit_as2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineedit_as2.textChanged.connect(self.changed_lineedit_fields2)
        self.lineedit_as2.setStyleSheet(self.style_qLine)
        self.table_fields2.setCellWidget(0, 5, self.lineedit_as2)

    def changed_lineedit_fields2(self):
        texto = self.lineedit_as2.text()
        if len(texto) is not None:
            self.label_as2.setStyleSheet("QLabel { color: black; }")
            self.lineedit_as2.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.label_as2.setStyleSheet("QLabel { color: green; }")
            self.lineedit_as2.setStyleSheet(self.style_qLine1)

    def create_label_as2(self):
        self.label_as2 = QLabel("AS")
        self.label_as2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_as2.setStyleSheet("QLabel { color: black; }")
        self.table_fields2.setCellWidget(0, 4, self.label_as2)
