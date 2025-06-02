from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableUpdate(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_update()

    def create_table_update(self):
        self.table_update = QTableWidget(3, 5)
        self.table_update.setMaximumHeight(93)
        self.table_update.setColumnWidth(0, 100)
        self.table_update.setColumnWidth(1, 130)
        self.table_update.setColumnWidth(2, 140)
        self.table_update.setColumnWidth(3, 130)
        self.table_update.setColumnWidth(4, 140)
        self.table_update.horizontalHeader().setVisible(False)
        self.table_update.verticalHeader().setVisible(False)
        self.create_label_update()

    def create_label_update(self):
        self.label_update = QLabel("UPDATE")
        self.table_update.setCellWidget(0, 0, self.label_update)
        self.label_update.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_update.setStyleSheet("QLabel { color: green; }")
        self.create_combo_update_table()

    def create_combo_update_table(self):
        self.combo_update_table = QComboBox()
        self.combo_update_table.addItem("Select table")
        self.combo_update_table.addItems(ConnectDb.get_all_tables(self))
        self.table_update.setCellWidget(0, 1, self.combo_update_table)
        self.combo_update_table.currentIndexChanged.connect(self.get_combo_update_table)

    def get_combo_update_table(self):
        current_text = self.combo_update_table.currentText()
        if current_text != "Select table":
            self.items_update = ConnectDb.get_fields_table(self, current_text)
            self.items_update = list(self.items_update)
            self.create_label_set()
            self.create_combo_update_fields1()
            self.combo_update_table.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_update.removeCellWidget(1, 0)
            self.table_update.removeCellWidget(1, 1)
            self.table_update.removeCellWidget(1, 2)
            self.table_update.removeCellWidget(1, 3)
            self.table_update.removeCellWidget(1, 4)
            self.table_update.removeCellWidget(2, 0)
            self.table_update.removeCellWidget(2, 1)
            self.table_update.removeCellWidget(2, 2)
            self.combo_update_table.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_label_set(self):
        self.label_set = QLabel("SET")
        self.table_update.setCellWidget(1, 0, self.label_set)
        self.label_set.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_set.setStyleSheet("QLabel { color: green; }")

    def create_combo_update_fields1(self):
        self.combo_update_fields1 = QComboBox()
        newList = []
        newList.append("Select field")
        for item in self.items_update:
            newList.append(item + " =")
        self.combo_update_fields1.addItems(newList)
        self.table_update.setColumnWidth(1, 120)
        self.table_update.setCellWidget(1, 1, self.combo_update_fields1)
        self.combo_update_fields1.currentIndexChanged.connect(
            self.get_result_combo_update_fields1
        )

    def get_result_combo_update_fields1(self):
        current_text = self.combo_update_fields1.currentText()
        if current_text != "Select field":
            self.combo_update_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_lineedit_update1()
        else:
            self.combo_update_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_update.removeCellWidget(1, 2)
            self.table_update.removeCellWidget(1, 3)
            self.table_update.removeCellWidget(1, 4)
            self.table_update.removeCellWidget(2, 0)
            self.table_update.removeCellWidget(2, 1)
            self.table_update.removeCellWidget(2, 2)

    def create_lineedit_update1(self):
        self.line_edit_update1 = QLineEdit()
        self.line_edit_update1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_edit_update1.setStyleSheet(self.style_qLine)
        self.line_edit_update1.textChanged.connect(self.change_lineedit_update1)
        self.table_update.setColumnWidth(2, 100)
        self.table_update.setCellWidget(1, 2, self.line_edit_update1)

    def create_combo_update_fields2(self):
        newList = []
        newList.append("Select field")
        for item in self.items_update:
            newList.append("," + item + "=")
        self.combo_update_fields2 = QComboBox()
        self.combo_update_fields2.addItems(newList)
        self.table_update.setColumnWidth(3, 120)
        self.table_update.setCellWidget(1, 3, self.combo_update_fields2)
        self.combo_update_fields2.currentIndexChanged.connect(
            self.get_combo_update_fields2
        )

    def get_combo_update_fields2(self):
        current_text = self.combo_update_fields2.currentText()
        if current_text != "Select field":
            self.combo_update_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_lineedit_update2()
        else:
            self.table_update.removeCellWidget(1, 4)
            self.combo_update_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_lineedit_update2(self):
        self.line_edit_update2 = QLineEdit()
        self.line_edit_update2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_edit_update2.setStyleSheet(self.style_qLine)
        self.line_edit_update2.textChanged.connect(self.change_lineedit_update2)
        self.table_update.setCellWidget(1, 4, self.line_edit_update2)

    def create_label_where(self):
        self.label_where = QLabel("WHERE")
        self.table_update.setCellWidget(2, 0, self.label_where)
        self.label_where.setStyleSheet("QLabel { color: green; }")
        self.label_where.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def create_combo_update_fields3(self):
        self.combo_update_fields3 = QComboBox()
        self.combo_update_fields3.addItem("Select field")
        for item in self.items_update:
            item = item + " ="
            self.combo_update_fields3.addItem(item)
        self.table_update.setCellWidget(2, 1, self.combo_update_fields3)
        self.combo_update_fields3.currentIndexChanged.connect(
            self.get_combo_update_fields3
        )

    def get_combo_update_fields3(self):
        current_text = self.combo_update_fields3.currentText()
        if current_text != "Select field":
            self.combo_update_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.get_result_combo_update_fields3()
        else:
            self.table_update.removeCellWidget(2, 2)
            self.combo_update_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def get_result_combo_update_fields3(self):
        current_text_table = "FROM " + self.combo_update_table.currentText()
        current_text = self.combo_update_fields3.currentText()
        current_text = current_text.replace(" =", "")
        items = ConnectDb.get_data_column(self, current_text_table, current_text)
        result = set(items)
        result = list(result)
        result.sort()
        self.combo_update_fields4 = QComboBox()
        self.combo_update_fields4.addItem("Select data")
        self.combo_update_fields4.addItems(result)
        self.combo_update_fields4.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_update.setCellWidget(2, 2, self.combo_update_fields4)

    def change_lineedit_update1(self):
        if len(self.line_edit_update1.text()) is not None:
            self.line_edit_update1.setStyleSheet(self.style_qLine)
            self.combo_update_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
        if len(self.line_edit_update1.text()) > 0:
            self.create_combo_update_fields2()
            self.create_label_where()
            self.create_combo_update_fields3()
            self.line_edit_update1.setStyleSheet(self.style_qLine1)
            self.combo_update_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )

    def change_lineedit_update2(self):
        if len(self.line_edit_update2.text()) is not None:
            self.line_edit_update2.setStyleSheet(self.style_qLine)
            self.combo_update_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
        if len(self.line_edit_update2.text()) > 0:
            self.line_edit_update2.setStyleSheet(self.style_qLine1)
            self.combo_update_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
