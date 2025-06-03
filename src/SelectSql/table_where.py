from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QLabel,
)
from PyQt6.QtCore import Qt
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QColor
from src.UtilsSql.connect_db import ConnectDb
from src.UtilsSql.clear_data import ClearDataSelect
from src.UtilsSql.create_model import create_model


class TableWhere(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_where()

    def current_textcolor_where(self, row, column, current_text):
        current_text.setForeground(QColor("green"))
        self.table_where.setItem(row, column, QTableWidgetItem(current_text))

    def create_table_where(self):
        self.table_where = QTableWidget(1, 8)
        self.table_where.setMaximumHeight(30)
        self.table_where.setColumnWidth(0, 120)
        self.table_where.horizontalHeader().setVisible(False)
        self.table_where.verticalHeader().setVisible(False)
        self.row_where = self.table_where.rowCount()
        self.create_combobox_where()

    def create_combobox_where(self):
        self.combo_where_option = QComboBox()
        self.combo_where_option.addItems(
            [
                "Select WHERE",
                "WHERE",
                "WHERE NOT",
                "WHERE EXISTS(SELECT ",
                "WHERE NOT EXISTS(SELECT ",
                "WHERE TRUE",
            ]
        )
        self.table_where.setCellWidget(0, 0, self.combo_where_option)
        self.combo_where_option.currentIndexChanged.connect(self.get_combobox_where)

    def get_combobox_where(self):
        current_text = self.combo_where_option.currentText()
        current_text_select_option = self.combobox_select_options.currentText()
        if current_text != "Select WHERE":
            self.combo_where_option.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text_select_option == "SELECT ALL":
                self.table_union.hide()
                self.table_and.hide()
                self.table_and_or.hide()
                self.table_group_by.hide()
                self.table_having.hide()
                self.table_order_by.hide()
            if current_text == "WHERE" or current_text == "WHERE NOT":
                self.table_where.setRowCount(1)
                self.table_where.removeRow(self.row_where)
                self.table_where.removeCellWidget(0, 1)
                self.table_where.removeCellWidget(0, 2)
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_join.show()
                self.table_and.show()
                self.table_and_or.show()
                self.table_group_by.show()
                self.table_having.show()
                self.table_order_by.show()
                self.create_combobox_where_fields1()
                ClearDataSelect.clear_column_combo_where_in(self)
            elif (
                current_text == "WHERE NOT EXISTS(SELECT "
                or current_text == "WHERE EXISTS(SELECT "
            ):
                ClearDataSelect.clear_column_combo_where_in(self)
                self.table_where.removeCellWidget(0, 1)
                self.table_where.removeCellWidget(0, 2)
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                self.table_where.removeCellWidget(0, 8)
                self.table_where.setColumnWidth(6, 50)
                self.table_where.setColumnWidth(7, 50)
                self.table_where.setColumnWidth(8, 50)
                self.table_join.show()
                self.table_and.show()
                self.table_and_or.show()
                self.table_group_by.show()
                self.table_having.show()
                self.table_order_by.show()
                self.create_combobox_where_exists_fields()
            else:
                ClearDataSelect.clear_column_combo_where_in(self)
                self.table_where.setRowCount(1)
                self.table_where.removeRow(self.row_where)
                self.table_where.setMaximumHeight(30)
                self.table_where.removeCellWidget(0, 1)
                self.table_where.removeCellWidget(0, 2)
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                self.table_where.removeCellWidget(0, 8)
                self.table_where.removeCellWidget(1, 4)
                self.table_where.removeCellWidget(1, 5)
                self.table_where.removeCellWidget(1, 6)
                self.table_where.setColumnWidth(6, 50)
                self.table_where.setColumnWidth(7, 50)
                self.table_where.setColumnWidth(8, 50)

        else:
            ClearDataSelect.clear_column_combo_where_in(self)
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.setMaximumHeight(30)
            self.table_where.removeCellWidget(0, 1)
            self.table_where.removeCellWidget(0, 2)
            self.table_where.removeCellWidget(0, 3)
            self.table_where.removeCellWidget(0, 4)
            self.table_where.removeCellWidget(0, 5)
            self.table_where.removeCellWidget(0, 6)
            self.table_where.removeCellWidget(0, 7)
            self.combo_where_option.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_exists_fields(self):
        self.combobox_where_exists_fields = QComboBox()
        self.combobox_where_exists_fields.addItem("Select field")
        self.combobox_where_exists_fields.addItem("*")
        for field in ConnectDb.get_list_all(self):
            field = field.split(",")[-1]
            self.combobox_where_exists_fields.addItem(field)
        self.combobox_where_exists_fields.currentTextChanged.connect(
            self.get_combobox_where_exists_fields
        )
        self.table_where.setCellWidget(0, 1, self.combobox_where_exists_fields)

    def get_combobox_where_exists_fields(self):
        current_text = self.combobox_where_exists_fields.currentText()
        if current_text != "Select field":
            self.combobox_where_exists_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_combobox_where_exists_from_tables1()
        else:
            self.combobox_where_exists_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_fields1(self):
        self.combobox_where_fields1 = QComboBox()
        self.combobox_where_fields1.addItems(["Select field", "*"])
        current_table = self.combo_tables.currentText()
        current_table = current_table.replace("FROM ", "")
        fields = ConnectDb.get_fields_table(self, current_table)
        self.combobox_where_fields1.addItems(fields)
        try:
            current_table = self.combo_join_tables1.currentText()
            if current_table != "Select table":
                fields = ConnectDb.get_fields_table(self, current_table)
                self.combobox_where_fields1.addItems(fields)
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combobox_where_fields1")
        self.table_where.setColumnWidth(1, 100)
        self.table_where.setCellWidget(0, 1, self.combobox_where_fields1)
        self.combobox_where_fields1.currentIndexChanged.connect(
            self.get_combo_where_fields1
        )

    def get_combo_where_fields1(self):
        current_text = self.combobox_where_fields1.currentText()
        if current_text != "Select field":
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.setMaximumHeight(30)
            self.combobox_where_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            current_text_where = self.combo_where_option.currentText()
            if current_text_where == "WHERE" or current_text_where == "WHERE NOT":
                self.create_combobox_operators()
        else:
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.setMaximumHeight(30)
            self.table_where.removeCellWidget(0, 2)
            self.table_where.removeCellWidget(0, 3)
            self.table_where.removeCellWidget(0, 4)
            self.table_where.removeCellWidget(0, 5)
            self.table_where.removeCellWidget(0, 6)
            self.combobox_where_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_operators(self):
        self.combo_where_operator = QComboBox()
        self.combo_where_operator.addItems(
            [
                "Operators",
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
                "IN(SELECT",
                "NOT IN(SELECT",
                "IS NULL",
                "IS NOT NULL",
            ]
        )
        self.table_where.setColumnWidth(2, 80)
        self.table_where.setCellWidget(0, 2, self.combo_where_operator)
        self.combo_where_operator.currentIndexChanged.connect(
            self.get_combo_where_operator
        )

    def get_combo_where_operator(self):
        current_text = self.combo_where_operator.currentText()
        if current_text != "Operators":
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.setMaximumHeight(30)
            self.combo_where_operator.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "BETWEEN" or current_text == "NOT BETWEEN":
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                ClearDataSelect.clear_column_combo_where_in(self)
                self.between1()
                self.between2()
            elif current_text == "LIKE" or current_text == "NOT LIKE":
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                ClearDataSelect.clear_column_combo_where_in(self)
                self.create_where_like_lineedit()
            elif current_text == "IN" or current_text == "NOT IN":
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                self.table_where.removeCellWidget(0, 8)
                self.table_where.setColumnWidth(4, 100)
                self.table_where.setColumnWidth(5, 200)
                self.table_where.setColumnWidth(6, 50)
                self.table_where.setColumnWidth(7, 50)
                self.table_where.setColumnWidth(8, 50)
                self.table_where.setColumnWidth(9, 50)
                ClearDataSelect.clear_column_combo_where_in(self)
                self.create_combo_where_in()
            elif current_text == "IS NULL" or current_text == "IS NOT NULL":
                ClearDataSelect.clear_column_combo_where_in(self)
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                self.table_where.removeCellWidget(0, 8)
                self.table_where.removeCellWidget(0, 9)
            elif current_text == "NOT IN(SELECT" or current_text == "IN(SELECT":
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                self.table_where.removeCellWidget(0, 8)
                self.table_where.removeCellWidget(0, 9)
                ClearDataSelect.clear_column_combo_where_in(self)
                self.create_combobox_where_in_select_fields()
            else:
                self.table_where.removeCellWidget(0, 3)
                self.table_where.removeCellWidget(0, 4)
                self.table_where.removeCellWidget(0, 5)
                self.table_where.removeCellWidget(0, 6)
                self.table_where.removeCellWidget(0, 7)
                self.table_where.removeCellWidget(0, 8)
                ClearDataSelect.clear_column_combo_where_in(self)
                self.get_operator()
        else:
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.setMaximumHeight(30)
            self.table_where.removeCellWidget(0, 3)
            self.table_where.removeCellWidget(0, 4)
            self.table_where.removeCellWidget(0, 5)
            self.table_where.removeCellWidget(0, 6)
            self.table_where.removeCellWidget(0, 7)
            self.table_where.removeCellWidget(0, 8)
            self.combo_where_operator.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_not_in_tables(self):
        self.combo_where_not_In_tables = QComboBox()
        self.combo_where_not_In_tables.addItem("FROM table")
        for table in ConnectDb.get_all_tables(self):
            self.combo_where_not_In_tables.addItem("FROM " + table)
        self.table_where.setCellWidget(0, 4, self.combo_where_not_In_tables)
        self.table_where.setColumnWidth(4, 120)
        self.combo_where_not_In_tables.currentIndexChanged.connect(
            self.get_combo_where_not_in_tables
        )

    def get_combo_where_not_in_tables(self):
        current_text = self.combo_where_not_In_tables.currentText()
        if current_text != "FROM table":
            self.create_combobox_where_select_where_field()
            self.combo_where_not_In_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_where_not_In_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_tables(self):
        self.combo_where_tables = QComboBox()
        self.combo_where_tables.addItem("FROM table)")
        for table in ConnectDb.get_all_tables(self):
            self.combo_where_tables.addItem("FROM " + table + ")")
        self.table_where.setCellWidget(0, 5, self.combo_where_tables)
        self.table_where.setColumnWidth(5, 120)
        self.combo_where_tables.currentIndexChanged.connect(self.get_combo_where_tables)

    def get_combo_where_tables(self):
        current_text = self.combo_where_tables.currentText()
        if current_text != "FROM table)":
            self.combo_where_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_where_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_fields_select_avg(self):
        self.combobox_fields_select_avg = QComboBox()
        self.combobox_fields_select_avg.addItem("Select field")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            for item in items:
                item = "(" + item + ") FROM"
                self.combobox_fields_select_avg.addItem(item)
        except AttributeError as e:
            print(f"{e} :create_combobox_fields_select_avg")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_tables)
        for item in items:
            item = "(" + item + ") FROM"
            self.combobox_fields_select_avg.addItem(item)
        self.table_where.setColumnWidth(4, 100)
        self.table_where.setCellWidget(0, 4, self.combobox_fields_select_avg)
        self.combobox_fields_select_avg.currentIndexChanged.connect(
            self.get_combobox_fields_select_avg
        )

    def get_combobox_fields_select_avg(self):
        current_text = self.combobox_fields_select_avg.currentText()
        if current_text != "Select field":
            self.create_combobox_select_avg_tables()
            self.combobox_fields_select_avg.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.removeCellWidget(0, 5)
            self.table_where.removeCellWidget(0, 6)
            self.combobox_fields_select_avg.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_select_avg_tables(self):
        self.combo_select_avg_tables = QComboBox()
        self.combo_select_avg_tables.addItem("Table")
        for table in ConnectDb.get_all_tables(self):
            self.combo_select_avg_tables.addItem(table + ")")
        self.table_where.setColumnWidth(5, 100)
        self.table_where.setCellWidget(0, 5, self.combo_select_avg_tables)
        self.combo_select_avg_tables.currentIndexChanged.connect(
            self.get_combo_select_avg_tables
        )

    def get_combo_select_avg_tables(self):
        current_text = self.combo_select_avg_tables.currentText()
        if current_text != "FROM table":
            self.combo_select_avg_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_select_avg_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_where_in(self):
        self.models_where = {}
        row = self.table_where.rowCount()
        self.combo_where_in = QtWidgets.QComboBox()
        try:
            current_text_column = self.combobox_where_fields1.currentText()
            current_text_tables = self.combo_tables.currentText()
            items = ConnectDb.get_data_column(
                self, current_text_tables, current_text_column
            )
            result_In_set = set(items)
            result_In_list = list(result_In_set)
            result_In_list.sort()
            model = create_model(result_In_list)
        except TypeError as e:
            print(f"{e} :combo_where_in")

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
                model = create_model(result)
        except (AttributeError, RuntimeError, TypeError) as e:
            print(f"{e} :combo_where_in")
        self.combo_where_in.setModel(model)
        model.itemChanged.connect(lambda _, row=row: self.on_item_changed_comboIn(row))
        self.models_where[row] = model
        self.table_where.setCellWidget(0, 3, self.combo_where_in)
        item = QTableWidgetItem()
        self.table_where.setItem(row, 3, item)
        first_item = QtGui.QStandardItem("Select field/s")
        model.setItem(0, first_item)

    def on_item_changed_comboIn(self, tableRow):
        model = self.models_where[tableRow]
        items = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == Qt.CheckState.Checked:
                first_string = model.item(row).text().split(",")[-1]
                items.append(first_string)
            for item in items:
                item = QTableWidgetItem(item)
                self.current_textcolor_where(0, 4, item)
        self.table_where.setColumnWidth(4, 200)
        self.items_where_combo_in = "(" + ", ".join(items) + ")"
        if not items:
            item = QTableWidgetItem()
            self.table_where.setItem(0, 4, item)
        else:
            self.table_where.item(0, 4).setText("(" + ", ".join(items) + ")")

    def create_where_like_lineedit(self):
        self.where_like_lineedit = QLineEdit()
        self.where_like_lineedit.setStyleSheet(self.style_qLine)
        self.where_like_lineedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.where_like_lineedit.textChanged.connect(self.get_Where_like_lineedit)
        self.table_where.setColumnWidth(3, 80)
        self.table_where.setCellWidget(0, 3, self.where_like_lineedit)

    def get_Where_like_lineedit(self):
        current_text = self.where_like_lineedit.text()
        if len(current_text) is not None:
            self.where_like_lineedit.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.where_like_lineedit.setStyleSheet(self.style_qLine1)

    def get_data_where(self):
        current_text_column = self.combobox_where_fields1.currentText()
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            if current_text_tables != "Select JOIN":
                current_text_tables = "FROM " + self.combo_join_tables1.currentText()
                self.items_where_join = ConnectDb.get_data_column(
                    self, current_text_tables, current_text_column
                )
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :get_data_where")
        current_text_tables = self.combo_tables.currentText()
        self.items_where_table = ConnectDb.get_data_column(
            self, current_text_tables, current_text_column
        )

    def between1(self):
        self.get_data_where()
        self.combo_result_between1 = QComboBox()
        try:
            self.combo_result_between1.addItems(self.items_where_table)
        except AttributeError as e:
            print(f"{e} :between1")
        try:
            self.combo_result_between1.addItems(self.items_where_join)
        except AttributeError as e:
            print(f"{e} :between1")
        self.table_where.setColumnWidth(3, 100)
        self.table_where.setCellWidget(0, 3, self.combo_result_between1)
        self.combo_result_between1.setStyleSheet(
            "QComboBox:editable{{ color: {} }}".format("green")
        )

    def between2(self):
        self.get_data_where()
        self.combo_result_between2 = QComboBox()
        try:
            for item in self.items_where_join:
                item = "AND " + item
                self.combo_result_between2.addItem(item)
        except (AttributeError, RuntimeError, TypeError) as e:
            print(f"{e} :between2")
        try:
            for item in self.items_where_table:
                item = "AND " + item
                self.combo_result_between2.addItem(item)
        except (AttributeError, RuntimeError, TypeError) as e:
            print(f"{e} :between2")
        self.table_where.setColumnWidth(4, 100)
        self.table_where.setCellWidget(0, 4, self.combo_result_between2)
        self.combo_result_between2.setStyleSheet(
            "QComboBox:editable{{ color: {} }}".format("green")
        )

    def get_operator(self):
        self.get_data_where()
        self.combo_result_query = QComboBox()
        self.combo_result_query.addItem("Select option")
        self.combo_result_query.addItem("(SELECT ")
        self.combo_result_query.addItem("(SELECT AVG")
        try:
            result = set(self.items_where_join)
            result = list(result)
            result.sort()
            self.combo_result_query.addItems(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :get_operator")
        try:
            result = set(self.items_where_table)
            result = list(result)
            result.sort()
            self.combo_result_query.addItems(result)
        except (AttributeError, TypeError) as e:
            print(f"{e} :get_operator")
        self.combo_result_query.currentIndexChanged.connect(self.get_operator_result)
        self.table_where.setColumnWidth(3, 100)
        self.table_where.setCellWidget(0, 3, self.combo_result_query)

    def get_operator_result(self):
        current_text = self.combo_result_query.currentText()
        if current_text != "Select option":
            self.combo_result_query.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "(SELECT AVG":
                self.create_combobox_fields_select_avg()
            elif current_text == "(SELECT ":
                self.create_combobox_where_select_where_fields2()
            else:
                self.table_where.setRowCount(1)
                self.table_where.removeRow(self.row_where)
                self.table_where.setMaximumHeight(30)
        else:
            self.combo_result_query.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_where.removeCellWidget(0, 4)
            self.table_where.removeCellWidget(0, 5)

    def create_combobox_where_in_select_fields(self):
        self.combobox_where_In_select_fields = QComboBox()
        self.combobox_where_In_select_fields.addItem("Select field")
        try:
            current_text_tables = self.combo_tables.currentText()
            current_text_tables = current_text_tables.replace("FROM ", "")
            items = ConnectDb.get_fields_table(self, current_text_tables)
            self.combobox_where_In_select_fields.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_in_select_fields")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            self.combobox_where_In_select_fields.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_in_select_fields")
        self.table_where.setColumnWidth(3, 100)
        self.table_where.setCellWidget(0, 3, self.combobox_where_In_select_fields)
        self.combobox_where_In_select_fields.currentIndexChanged.connect(
            self.get_combobox_where_in_select_fields
        )

    def get_combobox_where_in_select_fields(self):
        current_text = self.combobox_where_In_select_fields.currentText()
        if current_text != "Select field":
            self.create_combobox_where_in_select_tables()
            self.combobox_where_In_select_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.removeCellWidget(0, 4)
            self.table_where.removeCellWidget(0, 5)
            self.combobox_where_In_select_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_in_select_tables(self):
        self.combobox_where_in_select_tables = QComboBox()
        self.combobox_where_in_select_tables.addItem("FROM table")
        for table in ConnectDb.get_all_tables(self):
            self.combobox_where_in_select_tables.addItem("FROM " + table)
        self.table_where.setCellWidget(0, 4, self.combobox_where_in_select_tables)
        self.table_where.setColumnWidth(4, 120)
        self.combobox_where_in_select_tables.currentIndexChanged.connect(
            self.get_combobox_where_in_selct_tables
        )

    def get_combobox_where_in_selct_tables(self):
        current_text = self.combobox_where_in_select_tables.currentText()
        if current_text != "FROM table":
            self.table_where.setMaximumHeight(63)
            self.table_where.setRowCount(2)
            self.create_combobox_where_in_select_where_fields()
            self.combobox_where_in_select_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.removeCellWidget(0, 5)
            self.table_where.setMaximumHeight(30)
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.combobox_where_in_select_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_in_select_where_fields(self):
        self.combobox_where_in_select_where_fields = QComboBox()
        self.combobox_where_in_select_where_fields.addItem("Select WHERE")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            for item in items:
                item = "WHERE " + item
                self.combobox_where_in_select_where_fields.addItem(item)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_in_select_where_fields")

        current_text = self.combobox_where_in_select_tables.currentText()
        current_text = current_text.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text)
        for item in items:
            item = "WHERE " + item
            self.combobox_where_in_select_where_fields.addItem(item)
        self.table_where.setColumnWidth(4, 100)
        self.table_where.setCellWidget(1, 4, self.combobox_where_in_select_where_fields)
        self.combobox_where_in_select_where_fields.currentIndexChanged.connect(
            self.get_combobox_where_in_select_where_fields
        )
        self.create_where_label_prths()

    def get_combobox_where_in_select_where_fields(self):
        current_text = self.combobox_where_in_select_where_fields.currentText()
        if current_text != "Select WHERE":
            self.create_operator_select_where()
            self.table_where.removeCellWidget(0, 5)
            self.combobox_where_in_select_where_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.removeCellWidget(1, 5)
            self.table_where.removeCellWidget(1, 6)
            self.create_where_label_prths()
            self.combobox_where_in_select_where_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_where_label_prths(self):
        self.where_label_prths = QLabel(")")
        self.where_label_prths.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.where_label_prths.setStyleSheet("color: green")
        self.table_where.setColumnWidth(5, 50)
        self.table_where.setCellWidget(0, 5, self.where_label_prths)

    def create_combobox_where_exists_from_tables1(self):
        self.combobox_where_exists_from_tables1 = QComboBox()
        self.combobox_where_exists_from_tables1.addItem("FROM table")
        for table in ConnectDb.get_all_tables(self):
            self.combobox_where_exists_from_tables1.addItem("FROM " + table)
        self.table_where.setCellWidget(0, 2, self.combobox_where_exists_from_tables1)
        self.table_where.setColumnWidth(2, 120)
        self.combobox_where_exists_from_tables1.currentIndexChanged.connect(
            self.get_combobox_where_exists_from_tables1
        )

    def get_combobox_where_exists_from_tables1(self):
        current_text = self.combobox_where_exists_from_tables1.currentText()
        if current_text != "FROM table":
            self.create_combobox_where_exixts_where_tables1()
            self.combobox_where_exists_from_tables1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combobox_where_exists_from_tables1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_exixts_where_tables1(self):
        self.combo_where_exixts_where_tables1 = QComboBox()
        self.combo_where_exixts_where_tables1.addItem("WHERE table")
        for table in ConnectDb.get_all_tables(self):
            self.combo_where_exixts_where_tables1.addItem("WHERE " + table + ".")
        self.table_where.setCellWidget(0, 3, self.combo_where_exixts_where_tables1)
        self.table_where.setColumnWidth(3, 120)
        self.combo_where_exixts_where_tables1.currentIndexChanged.connect(
            self.get_combo_where_exixts_where_tables1
        )

    def get_combo_where_exixts_where_tables1(self):
        current_text = self.combo_where_exixts_where_tables1.currentText()
        if current_text != "WHERE table":
            self.create_combobox_where_exixts_where_fields1()
            self.combo_where_exixts_where_tables1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.removeCellWidget(0, 4)
            self.table_where.removeCellWidget(0, 5)
            self.table_where.removeCellWidget(0, 6)
            self.table_where.removeCellWidget(0, 7)
            self.combo_where_exixts_where_tables1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_exixts_where_fields1(self):
        self.combo_where_exixts_where_fields1 = QComboBox()
        self.combo_where_exixts_where_fields1.addItem("Select field")

        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            for item in items:
                item = item + " = "
                self.combo_where_exixts_where_fields1.addItem(item)
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combobox_where_exixts_where_fields1")
        try:
            current_text_tables = self.combo_tables.currentText()
            current_text_tables = current_text_tables.replace("FROM ", "")
            items = ConnectDb.get_fields_table(self, current_text_tables)
            for item in items:
                item = item + " = "
                self.combo_where_exixts_where_fields1.addItem(item)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_exixts_where_fields1")
        self.table_where.setColumnWidth(4, 120)
        self.table_where.setCellWidget(0, 4, self.combo_where_exixts_where_fields1)
        self.combo_where_exixts_where_fields1.currentIndexChanged.connect(
            self.get_combo_where_exixts_where_fields1
        )

    def get_combo_where_exixts_where_fields1(self):
        current_text = self.combo_where_exixts_where_fields1.currentText()
        if current_text != "Select field":
            self.create_combobox_where_exixts_where_tables2()
            self.combo_where_exixts_where_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.removeCellWidget(0, 5)
            self.table_where.removeCellWidget(0, 6)
            self.table_where.removeCellWidget(0, 7)
            self.combo_where_exixts_where_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_exixts_where_tables2(self):
        self.combo_where_exixts_where_tables2 = QComboBox()
        self.combo_where_exixts_where_tables2.addItem("Select table")
        for table in ConnectDb.get_all_tables(self):
            table = table + "."
            self.combo_where_exixts_where_tables2.addItem(table)
        self.table_where.setCellWidget(0, 5, self.combo_where_exixts_where_tables2)
        self.table_where.setColumnWidth(5, 120)
        self.combo_where_exixts_where_tables2.currentIndexChanged.connect(
            self.get_combo_where_exixts_where_tables2
        )

    def get_combo_where_exixts_where_tables2(self):
        current_text = self.combo_where_exixts_where_tables2.currentText()
        if current_text != "Select table":
            self.create_combobox_where_exixts_where_fields2()
            self.combo_where_exixts_where_tables2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.removeCellWidget(0, 6)
            self.table_where.removeCellWidget(0, 7)
            self.combo_where_exixts_where_tables2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_exixts_where_fields2(self):
        self.combobox_where_exixts_where_fields2 = QComboBox()
        self.combobox_where_exixts_where_fields2.addItem("Select field")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            self.combobox_where_exixts_where_fields2.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_exixts_where_fields2")
        try:
            current_text_tables = self.combo_tables.currentText()
            current_text_tables = current_text_tables.replace("FROM ", "")
            items = ConnectDb.get_fields_table(self, current_text_tables)
            self.combobox_where_exixts_where_fields2.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_exixts_where_fields2")
        self.table_where.setColumnWidth(6, 120)
        self.table_where.setCellWidget(0, 6, self.combobox_where_exixts_where_fields2)
        self.combobox_where_exixts_where_fields2.currentIndexChanged.connect(
            self.get_create_combobox_where_exixts_where_fields2
        )

    def get_create_combobox_where_exixts_where_fields2(self):
        current_text = self.combobox_where_exixts_where_fields2.currentText()
        if current_text != "Select field":
            self.create_where_exists_label_prths()
            self.table_where.setMaximumHeight(63)
            self.table_where.setRowCount(2)
            self.create_combobox_where_exixts_where_fields3()
            self.combobox_where_exixts_where_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.setMaximumHeight(30)
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.removeCellWidget(0, 7)
            self.combobox_where_exixts_where_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_where_exists_label_prths(self):
        self.where_exists_label_prths = QLabel(")")
        self.where_exists_label_prths.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.where_exists_label_prths.setStyleSheet("color: green")
        self.table_where.setColumnWidth(7, 50)
        self.table_where.setCellWidget(0, 7, self.where_exists_label_prths)

    def create_combobox_where_exixts_where_fields3(self):
        self.combo_where_exixts_where_fields3 = QComboBox()
        self.combo_where_exixts_where_fields3.addItem("AND field")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            for item in items:
                item = "AND " + item
                self.combo_where_exixts_where_fields3.addItem(item)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_exixts_where_fields3")
        current_text_tables = self.combobox_where_exists_from_tables1.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        for item in ConnectDb.get_fields_table(self, current_text_tables):
            item = "AND " + item
            self.combo_where_exixts_where_fields3.addItem(item)
        self.table_where.setColumnWidth(4, 120)
        self.table_where.setCellWidget(1, 4, self.combo_where_exixts_where_fields3)
        self.combo_where_exixts_where_fields3.currentIndexChanged.connect(
            self.get_combo_where_exixts_where_fields3
        )

    def get_combo_where_exixts_where_fields3(self):
        current_text = self.combo_where_exixts_where_fields3.currentText()
        if current_text != "AND field":
            self.table_where.removeCellWidget(0, 7)
            self.create_operator_select_where()
            self.combo_where_exixts_where_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.create_where_exists_label_prths()
            self.table_where.removeCellWidget(1, 5)
            self.table_where.removeCellWidget(1, 6)
            self.combo_where_exixts_where_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_fields2(self):
        self.combobox_where_fields2 = QComboBox()
        self.combobox_where_fields2.addItem("Select field")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            self.combobox_where_fields2.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_fields2")
        try:
            current_text_tables = self.combo_tables.currentText()
            current_text_tables = current_text_tables.replace("FROM ", "")
            items = ConnectDb.get_fields_table(self, current_text_tables)
            self.combobox_where_fields2.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_fields2")
        self.table_where.setColumnWidth(4, 100)
        self.table_where.setCellWidget(0, 4, self.combobox_where_fields2)
        self.combobox_where_fields2.currentIndexChanged.connect(
            self.get_combo_where_fields2
        )

    def get_combo_where_fields2(self):
        current_text = self.combobox_where_fields2.currentText()
        if current_text != "Select field":
            self.combobox_where_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            current_text_operator = self.combo_where_operator.currentText()
            if current_text_operator == "NOT IN(SELECT":
                self.create_combobox_where_not_in_tables()
            else:
                self.create_combobox_where_tables()
        else:
            self.table_where.removeCellWidget(0, 5)
            self.combobox_where_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_select_where_fields2(self):
        self.combo_where_select_where_fields2 = QComboBox()
        self.combo_where_select_where_fields2.addItem("Select field")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            self.combo_where_select_where_fields2.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_select_where_fields2")
        try:
            current_text_tables = self.combo_tables.currentText()
            current_text_tables = current_text_tables.replace("FROM ", "")
            items = ConnectDb.get_fields_table(self, current_text_tables)
            self.combo_where_select_where_fields2.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combobox_where_select_where_fields2")
        self.table_where.setColumnWidth(4, 120)
        self.table_where.setCellWidget(0, 4, self.combo_where_select_where_fields2)
        self.combo_where_select_where_fields2.currentIndexChanged.connect(
            self.get_combo_where_select_where_fields2
        )

    def get_combo_where_select_where_fields2(self):
        current_text = self.combo_where_select_where_fields2.currentText()
        if current_text != "Select field":
            self.create_combobox_where_select_tables()
            self.combo_where_select_where_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.table_where.removeCellWidget(0, 5)
            self.combo_where_select_where_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_select_tables(self):
        self.combo_where_select_tables = QComboBox()
        self.combo_where_select_tables.addItem("FROM table")
        for table in ConnectDb.get_all_tables(self):
            self.combo_where_select_tables.addItem("FROM " + table)
        self.table_where.setCellWidget(0, 5, self.combo_where_select_tables)
        self.table_where.setColumnWidth(5, 120)
        self.combo_where_select_tables.currentIndexChanged.connect(
            self.get_combo_where_select_tables
        )

    def get_combo_where_select_tables(self):
        current_text = self.combo_where_select_tables.currentText()
        if current_text != "FROM table":
            self.table_where.setMaximumHeight(63)
            self.table_where.setRowCount(2)
            self.create_combobox_where_select_where_field()
            self.create_where_select_label_prts()
            self.combo_where_select_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.setMaximumHeight(30)
            self.table_where.setRowCount(1)
            self.table_where.removeRow(self.row_where)
            self.combo_where_select_tables.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combobox_where_select_where_field(self):
        self.combo_where_select_where_field = QComboBox()
        self.combo_where_select_where_field.addItem("Select  WHERE")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table(self, current_text)
            for item in items:
                item = "WHERE " + item
                self.combo_where_select_where_field.addItem(item)
        except AttributeError as e:
            print(f"{e} :create_combobox_fields_select_avg")
        current_text_tables = self.combo_where_select_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_tables)
        for item in items:
            item = "WHERE " + item
            self.combo_where_select_where_field.addItem(item)
        self.table_where.setColumnWidth(4, 120)
        self.table_where.setCellWidget(1, 4, self.combo_where_select_where_field)
        self.combo_where_select_where_field.currentIndexChanged.connect(
            self.get_combo_where_select_where_field
        )

    def get_combo_where_select_where_field(self):
        current_text = self.combo_where_select_where_field.currentText()
        if current_text != "Select WHERE":
            self.table_where.removeCellWidget(0, 6)
            self.create_operator_select_where()
            self.combo_where_select_where_field.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.create_where_select_label_prts()
            self.table_where.removeCellWidget(1, 5)
            self.table_where.removeCellWidget(1, 6)
            self.combo_where_select_where_field.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_where_select_label_prts(self):
        self.where_select_label_prts = QLabel(")")
        self.where_select_label_prts.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_where.setCellWidget(0, 6, self.where_select_label_prts)
        self.where_select_label_prts.setStyleSheet("QLabel { color: green; }")

    def create_operator_select_where(self):
        self.combo_operator_select_where = QComboBox()
        self.combo_operator_select_where.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>"]
        )
        self.table_where.setCellWidget(1, 5, self.combo_operator_select_where)
        self.combo_operator_select_where.currentIndexChanged.connect(
            self.get_combo_operator_select_where
        )

    def get_combo_operator_select_where(self):
        current_text = self.combo_operator_select_where.currentText()
        if current_text != "Operator":
            self.create_combo_result_operator_select_where()
            self.combo_operator_select_where.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_where.removeCellWidget(1, 6)
            self.combo_operator_select_where.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_result_operator_select_where(self):
        self.combo_result_operator_select_where = QComboBox()
        current_text = self.combo_where_option.currentText()
        if (
            current_text == "WHERE NOT EXISTS(SELECT "
            or current_text == "WHERE EXISTS(SELECT "
        ):
            try:
                current_text_table = (
                    self.combobox_where_exists_from_tables1.currentText()
                )
                current_text_field = self.combo_where_exixts_where_fields3.currentText()
                current_text_field = current_text_field.replace("AND ", "")
                items = ConnectDb.get_data_column(
                    self, current_text_table, current_text_field
                )
                items_set = set(items)
                items_list = list(items_set)
                items_list.sort()
                for item in items_list:
                    item = item + ")"
                    self.combo_result_operator_select_where.addItem(item)
            except AttributeError as e:
                print(f"{e} :create_combo_result_operator_select_where")
        elif current_text == "WHERE NOT " or current_text == "WHERE":
            current_text = self.combo_where_operator.currentText()
            if current_text == "NOT IN(SELECT" or current_text == "IN(SELECT":
                try:
                    current_text_table = (
                        self.combobox_where_in_select_tables.currentText()
                    )
                    current_text_field = (
                        self.combobox_where_in_select_where_fields.currentText()
                    )
                    current_text_field = current_text_field.replace("WHERE ", "")
                    items = ConnectDb.get_data_column(
                        self, current_text_table, current_text_field
                    )
                    items_set = set(items)
                    items_list = list(items_set)
                    items_list.sort()
                    for item in items_list:
                        item = item + ")"
                        self.combo_result_operator_select_where.addItem(item)
                except AttributeError as e:
                    print(f"{e} :create_combo_result_operator_select_where")
            elif current_text in ["=", ">", "<", "<=", ">=", "<>"]:
                current_text = self.combo_result_query.currentText()
                if current_text == "(SELECT ":
                    try:
                        current_text_table = (
                            self.combo_where_select_tables.currentText()
                        )
                        current_text_field = (
                            self.combo_where_select_where_field.currentText()
                        )
                        current_text_field = current_text_field.replace("WHERE ", "")
                        items = ConnectDb.get_data_column(
                            self, current_text_table, current_text_field
                        )
                        items_set = set(items)
                        items_list = list(items_set)
                        items_list.sort()
                        for item in items_list:
                            item = item + ")"
                            self.combo_result_operator_select_where.addItem(item)
                    except AttributeError as e:
                        print(f"{e} :create_combo_result_operator_select_where")
        self.table_where.setCellWidget(1, 6, self.combo_result_operator_select_where)
        self.combo_result_operator_select_where.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
