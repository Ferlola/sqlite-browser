from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QCheckBox,
)
from PyQt6.QtCore import Qt
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QColor
from src.UtilsSql.connect_db import ConnectDb
from src.UtilsSql.create_model import create_model
from src.UtilsSql.clear_data import ClearDataSelect


class TableAnd(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_and()

    def current_text_color_and(self, row, column, currentText):
        currentText.setForeground(QColor("green"))
        self.table_and.setItem(row, column, QTableWidgetItem(currentText))

    def create_table_and(self):
        self.table_and = QTableWidget(1, 6)
        self.table_and.setMaximumHeight(30)
        self.table_and.setColumnWidth(0, 75)
        self.table_and.setColumnWidth(1, 50)
        self.table_and.setColumnWidth(2, 100)
        self.table_and.setColumnWidth(3, 80)
        self.table_and.horizontalHeader().setVisible(False)
        self.table_and.verticalHeader().setVisible(False)
        self.create_combo_and()

    def create_combo_and(self):
        self.combo_and = QComboBox()
        self.combo_and.addItems(["AND/OR", "AND ", "OR "])
        self.table_and.setCellWidget(0, 0, self.combo_and)
        self.combo_and.currentIndexChanged.connect(self.get_combo_and)

    def get_combo_and(self):
        current_text = self.combo_and.currentText()
        if current_text != "AND/OR":
            self.create_checkbox_parenthesis1()
            self.create_combo_and_fields1()
            self.combo_and.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.table_and.removeCellWidget(0, 1)
            self.table_and.removeCellWidget(0, 2)
            self.table_and.removeCellWidget(0, 3)
            self.table_and.removeCellWidget(0, 4)
            self.table_and.removeCellWidget(0, 5)
            self.table_and_or.removeCellWidget(0, 8)
            ClearDataSelect.clear_column_combobox_and_in(self)
            self.combo_and.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_checkbox_parenthesis1(self):
        self.checkbox_parenthesis1 = QCheckBox(text="(")
        self.checkbox_parenthesis1.setTristate(False)
        self.checkbox_parenthesis1.stateChanged.connect(
            self.on_state_changed_checkbox_parenthesis1
        )
        self.table_and.setColumnWidth(1, 50)
        self.table_and.setCellWidget(0, 1, self.checkbox_parenthesis1)

    def on_state_changed_checkbox_parenthesis1(self):
        state = self.checkbox_parenthesis1.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_parenthesis1.setStyleSheet("color: green")
            self.create_label_prh2()
        else:
            self.checkbox_parenthesis1.setStyleSheet("color: black")
            self.table_and_or.removeCellWidget(0, 6)

    def create_combo_and_fields1(self):
        self.combo_and_fields1 = QComboBox()
        self.combo_and_fields1.addItem("Select field")
        current_text_table = self.combo_tables.currentText()
        current_text_table = current_text_table.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_table)
        self.combo_and_fields1.addItems(items)
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            self.combo_and_fields1.addItems(items)
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combo_and_fields1")
        self.table_and.setCellWidget(0, 2, self.combo_and_fields1)
        self.combo_and_fields1.currentIndexChanged.connect(self.get_combo_and_fields1)

    def get_combo_and_fields1(self):
        current_text = self.combo_and_fields1.currentText()
        if current_text != "Select field":
            self.create_combo_and_optr()
            self.combo_and_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_and.removeCellWidget(0, 3)
            self.table_and.removeCellWidget(0, 4)
            self.table_and.removeCellWidget(0, 5)
            ClearDataSelect.clear_column_combobox_and_in(self)
            self.combo_and_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_and_fields3(self):
        self.combo_and_fields3 = QComboBox()
        self.combo_and_fields3.addItem("Select data")
        current_text_column = self.combo_and_fields1.currentText()
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            if current_text_tables != "Select JOIN":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_column
                )
                result = set(items)
                result = list(result)
                result.sort()
                self.combo_and_fields3.addItems(result)
        except (AttributeError, RuntimeError, TypeError) as e:
            print(f"{e} :create_combo_and_fields3")
        current_text_tables = self.combo_tables.currentText()
        items = ConnectDb.get_data_column(
            self, current_text_tables, current_text_column
        )
        try:
            result = set(items)
            result = list(result)
            result.sort()
            self.combo_and_fields3.addItems(result)
        except TypeError as e:
            print(f"{e} :create_combo_and_fields3")
        self.table_and.setCellWidget(0, 4, self.combo_and_fields3)
        self.table_and.setColumnWidth(4, 120)
        self.combo_and_fields3.currentIndexChanged.connect(self.get_combo_and_fields3)

    def get_combo_and_fields3(self):
        current_text = self.combo_and_fields3.currentText()
        if current_text != "Select data":
            self.combo_and_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_and_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_and_optr(self):
        self.combo_and_optr = QComboBox()
        self.combo_and_optr.addItems(
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
        self.table_and.setCellWidget(0, 3, self.combo_and_optr)
        self.combo_and_optr.currentIndexChanged.connect(self.get_combo_and_optr)

    def get_combo_and_optr(self):
        current_text = self.combo_and_optr.currentText()
        if current_text != "operator":
            self.combo_and_optr.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "LIKE" or current_text == "NOT LIKE":
                self.table_and.removeCellWidget(0, 4)
                self.table_and.removeCellWidget(0, 5)

                ClearDataSelect.clear_column_combobox_and_in(self)
                self.and_like()
            elif current_text == "IS NULL" or current_text == "IS NOT NULL":
                self.table_and.removeCellWidget(0, 4)
                self.table_and.removeCellWidget(0, 5)

                ClearDataSelect.clear_column_combobox_and_in(self)
            elif current_text == "IN" or current_text == "NOT IN":
                self.table_and.removeCellWidget(0, 4)
                self.table_and.removeCellWidget(0, 5)

                self.create_combobox_and_in()
            elif current_text == "BETWEEN" or current_text == "NOT BETWEEN":
                self.table_and.removeCellWidget(0, 4)
                self.table_and.removeCellWidget(0, 5)
                self.create_combo_and_between1()
                self.create_combo_and_between2()
                ClearDataSelect.clear_column_combobox_and_in(self)
            else:
                self.table_and.removeCellWidget(0, 5)
                ClearDataSelect.clear_column_combobox_and_in(self)
                self.create_combo_and_fields3()
        else:
            self.table_and.removeCellWidget(0, 4)
            self.table_and.removeCellWidget(0, 5)
            self.combo_and_optr.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_and_in(self):
        self.modelsAnd = {}
        row = self.table_and.rowCount()
        self.combobox_and_in = QtWidgets.QComboBox()
        try:
            current_text_table = self.combo_tables.currentText()
            current_text_field = self.combo_and_fields1.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_table, current_text_field
            )
            items_set = set(items)
            items_list = list(items_set)
            items_list.sort()
            model = create_model(items_list)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combobox_and_in")
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            current_text_field = self.combo_and_fields1.currentText()
            if current_text_tables != "Select JOIN":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_field
                )
                items_set = set(items)
            items_list = list(items_set)
            items_list.sort()
            model = create_model(items_list)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combobox_and_in")
        self.combobox_and_in.setModel(model)
        model.itemChanged.connect(lambda _, row=row: self.on_itemchanged_and_in(row))
        self.modelsAnd[row] = model
        self.table_and.setCellWidget(0, 4, self.combobox_and_in)
        self.table_and.setColumnWidth(4, 100)
        firstItem = QtGui.QStandardItem("Select field/s")
        model.setItem(0, firstItem)

    def on_itemchanged_and_in(self, tableRow):
        model = self.modelsAnd[tableRow]
        items = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == Qt.CheckState.Checked:
                first_string = model.item(row).text().split(",")[-1]
                items.append(first_string)
            for item in items:
                item = QTableWidgetItem(item)
                self.current_text_color_and(0, 5, item)
        self.table_and.setColumnWidth(5, 180)
        if len(items) == 0:
            item = QTableWidgetItem()
            self.table_and.setItem(0, 5, item)
            self.items_and_in = ""
        else:
            self.table_and.item(0, 5).setText("(" + ", ".join(items) + ")")
            self.items_and_in = "(" + ", ".join(items) + ")"

    def create_combo_and_between1(self):
        self.combo_and_between1 = QComboBox()
        current_text_column = self.combo_and_fields1.currentText()
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            if current_text_tables != "Select JOIN":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_column
                )
                self.combo_and_between1.addItems(items)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_between1")
        try:
            current_text_tables = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_tables, current_text_column
            )
            self.combo_and_between1.addItems(items)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_between1")
        self.table_and.setColumnWidth(4, 100)
        self.table_and.setCellWidget(0, 4, self.combo_and_between1)
        self.combo_and_between1.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )

    def create_combo_and_between2(self):
        self.combo_and_between2 = QComboBox()
        current_text_column = self.combo_and_fields1.currentText()
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            if current_text_tables != "Select JOIN":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                items = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_column
                )
                for item in items:
                    item = "AND" + item
                    self.combo_and_between2.addItem(item)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_between2")
        try:
            current_text_tables = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_tables, current_text_column
            )
            for item in items:
                item = "AND" + item
                self.combo_and_between2.addItem(item)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_combo_and_between2")
        self.table_and.setColumnWidth(5, 100)
        self.table_and.setCellWidget(0, 5, self.combo_and_between2)
        self.combo_and_between2.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )

    def and_like(self):
        self.and_like_line_edit = QLineEdit()
        self.and_like_line_edit.setStyleSheet(self.style_qLine)
        self.and_like_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.and_like_line_edit.textChanged.connect(self.get_and_like_lineedit)
        self.table_and.setColumnWidth(4, 80)
        self.table_and.setCellWidget(0, 4, self.and_like_line_edit)

    def get_and_like_lineedit(self):
        current_text = self.and_like_line_edit.text()
        if len(current_text) is not None:
            self.and_like_line_edit.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.and_like_line_edit.setStyleSheet(self.style_qLine1)
