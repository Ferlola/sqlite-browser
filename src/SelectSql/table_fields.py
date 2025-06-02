from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtGui import QColor
from src.UtilsSql.create_model import create_model
from src.UtilsSql.connect_db import ConnectDb


class TableFields(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_fields()

    def current_text_color_fields(self, row, column, current_text):
        current_text.setForeground(QColor("green"))
        self.table_fields.setItem(row, column, QTableWidgetItem(current_text))

    def create_table_fields(self):
        self.table_fields = QTableWidget(1, 6)
        self.table_fields.setMaximumHeight(30)
        self.table_fields.setColumnWidth(0, 150)
        self.table_fields.setColumnWidth(1, 370)
        self.table_fields.setColumnWidth(2, 120)
        self.table_fields.setColumnWidth(3, 120)
        self.table_fields.setColumnWidth(4, 50)
        self.table_fields.setColumnWidth(5, 50)
        self.table_fields.horizontalHeader().setVisible(False)
        self.table_fields.verticalHeader().setVisible(False)
        self.create_combobox_all()

    def create_combobox_all(self):
        self.models_fields1 = {}
        row = self.table_fields.rowCount()
        self.combo_fields1 = QtWidgets.QComboBox()
        model = create_model(self.get_list_all())
        self.combo_fields1.setModel(model)
        model.itemChanged.connect(lambda _, row=row: self.on_item_changed(row))
        self.models_fields1[row] = model
        self.table_fields.setCellWidget(0, 0, self.combo_fields1)
        item = QTableWidgetItem()
        self.table_fields.setItem(row, 1, item)
        first_item = QtGui.QStandardItem("Select field/s")
        model.setItem(0, first_item)

    def on_item_changed(self, tableRow):
        model = self.models_fields1[tableRow]
        self.items_checked = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == Qt.CheckState.Checked:
                first_string = model.item(row).text().split(",")[-1]
                self.items_checked.append(first_string)
            for item in self.items_checked:
                item = QTableWidgetItem(item)
                self.current_text_color_fields(0, 1, item)
        self.itemsFields = ", ".join(self.items_checked)
        if not self.items_checked:
            item = QTableWidgetItem()
            self.table_fields.setItem(0, 1, item)
            self.table_fields.removeCellWidget(0, 2)
            self.table_fields.removeCellWidget(0, 3)
            self.table_fields.removeCellWidget(0, 4)
            self.table_fields.removeCellWidget(0, 5)
        else:
            self.create_combo_fields1_count()
            self.create_label_as()
            self.create_lineedit_as()
            self.table_fields.item(0, 1).setText(", ".join(self.items_checked))

    def create_combo_fields1_count(self):
        self.combo_fields1_count = QComboBox()
        self.combo_fields1_count.addItems(["count/avg/sum", ",COUNT", ",AVG", ",SUM"])
        self.table_fields.setCellWidget(0, 2, self.combo_fields1_count)
        self.combo_fields1_count.currentIndexChanged.connect(
            self.get_combo_fields1_count
        )

    def get_combo_fields1_count(self):
        current_text = self.combo_fields1_count.currentText()
        if current_text != "count/avg/sum":
            self.table_fields.setColumnWidth(2, 100)
            self.table_fields.setColumnWidth(3, 140)
            self.create_combo_all_fields2_count()
            self.combo_fields1_count.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_fields.removeCellWidget(0, 3)
            self.table_fields.setColumnWidth(2, 120)
            self.table_fields.setColumnWidth(3, 120)
            self.combo_fields1_count.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_all_fields2_count(self):
        self.combo_all_fields2_count = QComboBox()
        self.combo_all_fields2_count.addItem("(*)")
        self.combo_all_fields2_count.addItems(self.get_list_count())
        self.combo_all_fields2_count.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_fields.setCellWidget(0, 3, self.combo_all_fields2_count)

    def create_lineedit_as(self):
        self.lineedit_as = QLineEdit()
        self.lineedit_as.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineedit_as.textChanged.connect(self.changed_lineedit_fields)
        self.lineedit_as.setStyleSheet(self.style_qLine)
        self.table_fields.setCellWidget(0, 5, self.lineedit_as)

    def changed_lineedit_fields(self):
        texto = self.lineedit_as.text()
        if len(texto) is not None:
            self.label_as.setStyleSheet("QLabel { color: black; }")
            self.lineedit_as.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.label_as.setStyleSheet("QLabel { color: green; }")
            self.lineedit_as.setStyleSheet(self.style_qLine1)

    def create_label_as(self):
        self.label_as = QLabel("AS")
        self.label_as.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_as.setStyleSheet("QLabel { color: black; }")
        self.table_fields.setCellWidget(0, 4, self.label_as)
