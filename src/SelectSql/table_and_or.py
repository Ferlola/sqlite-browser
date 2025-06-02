from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox, QLineEdit, QLabel
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from src.UtilsSql.create_model import create_model
from src.UtilsSql.clear_data import ClearDataSelect
from src.UtilsSql.connect_db import ConnectDb


class TableAndOr(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_and_or()

    def current_text_color_and_or(self, row, column, current_text):
        current_text.setForeground(QColor("green"))
        self.table_and_or.setItem(row, column, QTableWidgetItem(current_text))

    def create_table_and_or(self):
        self.table_and_or = QTableWidget(1, 7)
        self.table_and_or.setMaximumHeight(30)
        self.table_and_or.setColumnWidth(0, 50)
        self.table_and_or.setColumnWidth(1, 100)
        self.table_and_or.setColumnWidth(2, 120)
        self.table_and_or.setColumnWidth(3, 80)
        self.table_and_or.setColumnWidth(6, 50)
        self.table_and_or.horizontalHeader().setVisible(False)
        self.table_and_or.verticalHeader().setVisible(False)
        self.create_combo_and_or()

    def create_combo_and_or(self):
        self.combo_and_or = QComboBox()
        self.combo_and_or.addItems(["AND/OR", "AND", "OR"])
        self.table_and_or.setCellWidget(0, 1, self.combo_and_or)
        self.combo_and_or.currentIndexChanged.connect(self.get_combo_and_or)

    def get_combo_and_or(self):
        current_text = self.combo_and_or.currentText()
        if current_text != "AND/OR":
            self.combo_and_or.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            self.create_combo_and_or_fields1()
        else:
            self.table_and_or.removeCellWidget(0, 2)
            self.table_and_or.removeCellWidget(0, 3)
            self.table_and_or.removeCellWidget(0, 4)
            self.table_and_or.removeCellWidget(0, 5)
            ClearDataSelect.clear_column_comboitems_and_or_in(self)
            self.combo_and_or.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_and_or_fields1(self):
        self.combo_and_or_fields1 = QComboBox()
        self.combo_and_or_fields1.addItem("Select field")
        current_text = self.combo_tables.currentText()
        current_text = current_text.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text)
        self.combo_and_or_fields1.addItems(items)
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            self.combo_and_or_fields1.addItems(items)
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combo_and_or_fields1")
        self.table_and_or.setCellWidget(0, 2, self.combo_and_or_fields1)
        self.combo_and_or_fields1.currentIndexChanged.connect(
            self.get_combo_and_or_fields1
        )

    def get_combo_and_or_fields1(self):
        current_text = self.combo_and_or_fields1.currentText()
        if current_text != "Select field":
            self.create_combo_and_or_optr1()
            self.combo_and_or_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_and_or.removeCellWidget(0, 3)
            self.table_and_or.removeCellWidget(0, 4)
            self.combo_and_or_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_and_or_optr1(self):
        self.combo_and_or_optr1 = QComboBox()
        self.combo_and_or_optr1.addItems(
            [
                "operator",
                "=",
                ">",
                "<",
                ">=",
                "<=",
                "<>",
                "BETWEEN",
                "NOT BETWEEN",
                "LIKE",
                "NOT LIKE",
                "IN",
                "NOT IN",
                "IS NULL",
                "IS NOT NULL",
            ]
        )
        self.table_and_or.setCellWidget(0, 3, self.combo_and_or_optr1)
        self.combo_and_or_optr1.currentIndexChanged.connect(self.get_combo_and_or_optr1)

    def get_combo_and_or_optr1(self):
        current_text = self.combo_and_or_optr1.currentText()
        if current_text != "operator":
            self.combo_and_or_optr1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "LIKE" or current_text == "NOT LIKE":
                self.table_and_or.removeCellWidget(0, 5)
                ClearDataSelect.clear_column_comboitems_and_or_in(self)
                self.and_or_like()
            elif current_text == "IS NULL" or current_text == "IS NOT NULL":
                self.table_and_or.removeCellWidget(0, 4)
                self.table_and_or.removeCellWidget(0, 5)
                ClearDataSelect.clear_column_comboitems_and_or_in(self)
            elif current_text == "IN" or current_text == "NOT IN":
                self.table_and_or.removeCellWidget(0, 4)
                self.table_and_or.removeCellWidget(0, 5)
                self.create_combobox_and_or_in()
            elif current_text == "BETWEEN" or current_text == "NOT BETWEEN":
                self.table_and_or.removeCellWidget(0, 4)
                self.table_and_or.removeCellWidget(0, 5)
                ClearDataSelect.clear_column_comboitems_and_or_in(self)
                self.create_combo_and_or_between1()
                self.create_combo_and_or_between2()
            else:
                self.table_and_or.removeCellWidget(0, 4)
                self.table_and_or.removeCellWidget(0, 5)
                ClearDataSelect.clear_column_comboitems_and_or_in(self)
                self.create_combo_and_or_fields2()
        else:
            self.table_and_or.removeCellWidget(0, 4)
            self.table_and_or.removeCellWidget(0, 5)
            ClearDataSelect.clear_column_comboitems_and_or_in(self)
            self.combo_and_or_optr1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_and_or_fields2(self):
        self.combo_and_or_fields2 = QComboBox()
        current_text_column = self.combo_and_or_fields1.currentText()
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            if current_text_tables != "Select table":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_column
                )
                result = set(items)
                result = list(result)
                result.sort()
                self.combo_and_or_fields2.addItems(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_fields2")
        try:
            current_text_tables = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_tables, current_text_column
            )
            result = set(items)
            result = list(result)
            result.sort()
            self.combo_and_or_fields2.addItems(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_fields2")
        self.table_and_or.setCellWidget(0, 4, self.combo_and_or_fields2)
        self.table_and_or.setColumnWidth(4, 100)
        self.combo_and_or_fields2.currentIndexChanged.connect(
            self.get_combo_and_or_fields2
        )
        self.combo_and_or_fields2.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )

    def get_combo_and_or_fields2(self):
        current_text = self.combo_and_or_fields2.currentText()
        if current_text != "Select field":
            self.combo_and_or_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_and_or_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_and_or_fields3(self):
        self.combo_and_or_fields3 = QComboBox()
        current_text_column = self.combo_and_or_fields1.currentText()
        try:
            current_text_table = self.combo_join_tables1.currentText()
            if current_text_table != "Select table":
                current_text_table = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_table, current_text_column
                )
                result = set(items)
                result = list(result)
                result.sort()
                self.combo_and_or_fields3.addItems(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_fields3")
        try:
            current_text_table = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_table, current_text_column
            )
            result = set(items)
            result = list(result)
            result.sort()
            self.combo_and_or_fields3.addItems(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_fields3")
        self.table_and_or.setCellWidget(0, 4, self.combo_and_or_fields3)
        self.table_and_or.setColumnWidth(4, 120)
        self.combo_and_or_fields3.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )

    def create_combobox_and_or_in(self):
        self.models_and_or = {}
        row = self.table_and_or.rowCount()
        self.combobox_and_or_in = QtWidgets.QComboBox()
        current_text_column = self.combo_and_or_fields1.currentText()
        try:
            current_text_table = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_table, current_text_column
            )
            itemsSet = set(items)
            itemslist = list(itemsSet)
            itemslist.sort()
            model = create_model(itemslist)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combobox_and_or_in")
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            if current_text_tables != "Select table":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_column
                )
                result = set(items)
                result = list(result)
                result.sort()
                model = create_model(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_fields2")
        self.combobox_and_or_in.setModel(model)
        model.itemChanged.connect(lambda _, row=row: self.on_itemchanged_and_or_in(row))
        self.models_and_or[row] = model
        self.table_and_or.setCellWidget(0, 4, self.combobox_and_or_in)
        self.table_and_or.setColumnWidth(4, 100)
        first_item = QtGui.QStandardItem("Select field/s")
        model.setItem(0, first_item)

    def on_itemchanged_and_or_in(self, tableRow):
        model = self.models_and_or[tableRow]
        items = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == Qt.CheckState.Checked:
                first_string = model.item(row).text().split(",")[-1]
                items.append(first_string)
            for item in items:
                item = QTableWidgetItem(item)
                self.current_text_color_and_or(0, 5, item)
        self.table_and_or.setColumnWidth(5, 180)
        if len(items) == 0:
            item = QTableWidgetItem()
            self.table_and_or.setItem(0, 5, item)
            self.items_and_or_in = ""
        else:
            self.table_and_or.item(0, 5).setText("(" + ", ".join(items) + ")")
            self.items_and_or_in = "(" + ", ".join(items) + ")"

    def create_combo_and_or_between1(self):
        self.combo_and_or_between1 = QComboBox()
        current_text_column = self.combo_and_or_fields1.currentText()
        try:
            current_text_table = self.combo_join_tables1.currentText()
            if current_text_table != "Select JOIN":
                current_text_table = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_table, current_text_column
                )
                self.combo_and_or_between1.addItems(items)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_between1")
        try:
            current_text_table = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_table, current_text_column
            )
            self.combo_and_or_between1.addItems(items)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_between1")
        self.table_and_or.setColumnWidth(4, 100)
        self.table_and_or.setCellWidget(0, 4, self.combo_and_or_between1)
        self.combo_and_or_between1.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )

    def create_combo_and_or_between2(self):
        self.combo_and_or_between2 = QComboBox()
        current_text_column = self.combo_and_or_fields1.currentText()
        try:
            current_text_table = self.combo_join_tables1.currentText()
            if current_text_table != "Select JOIN":
                current_text_table = "FROM " + self.combo_join_tables1.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_table, current_text_column
            )
            for item in items:
                item = "AND" + item
                self.combo_and_or_between2.addItem(item)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_between2")
        try:
            current_text_table = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_table, current_text_column
            )
            for item in items:
                item = "AND" + item
                self.combo_and_or_between2.addItem(item)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_or_between2")
        self.table_and_or.setColumnWidth(5, 100)
        self.table_and_or.setCellWidget(0, 5, self.combo_and_or_between2)
        self.combo_and_or_between2.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )

    def and_or_like(self):
        self.and_or_likeLineedit = QLineEdit()
        self.and_or_likeLineedit.setStyleSheet(self.style_qLine)
        self.and_or_likeLineedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.and_or_likeLineedit.textChanged.connect(self.get_and_or_like_lineedit)
        self.table_and_or.setColumnWidth(4, 80)
        self.table_and_or.setCellWidget(0, 4, self.and_or_likeLineedit)

    def get_and_or_like_lineedit(self):
        texto = self.and_or_likeLineedit.text()
        if len(texto) is not None:
            self.and_or_likeLineedit.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.and_or_likeLineedit.setStyleSheet(self.style_qLine1)

    def create_label_prh2(self):
        self.label_prh2 = QLabel(")")
        self.label_prh2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_and_or.setCellWidget(0, 6, self.label_prh2)
        self.label_prh2.setStyleSheet("QLabel { color: green; }")
