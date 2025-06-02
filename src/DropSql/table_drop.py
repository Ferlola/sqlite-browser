from PyQt6.QtWidgets import QTableWidget, QComboBox, QCheckBox
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableDrop(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_drop()

    def create_table_drop(self):
        self.table_drop = QTableWidget(1, 2)
        self.table_drop.setMaximumHeight(30)
        self.table_drop.setMaximumWidth(267)
        self.table_drop.geometry().center()
        self.table_drop.setColumnWidth(0, 165)
        self.table_drop.setColumnWidth(1, 100)
        self.table_drop.horizontalHeader().setVisible(False)
        self.table_drop.verticalHeader().setVisible(False)
        self.row_drop = self.table_drop.rowCount()
        self.table_drop.setRowCount(1)
        self.create_combo_drop_truncate()

    def create_combo_drop_truncate(self):
        self.combo_drop_truncate = QComboBox()
        self.combo_drop_truncate.addItems(
            ["Select option", "DROP TABLE", "DELETE FROM"]
        )
        self.combo_drop_truncate.currentIndexChanged.connect(
            self.get_combo_drop_truncate
        )
        self.combo_drop_truncate.currentIndexChanged.connect(self.get_combo_drop_table)
        self.table_drop.setCellWidget(0, 0, self.combo_drop_truncate)

    def get_combo_drop_truncate(self):
        current_text = self.combo_drop_truncate.currentText()
        if current_text != "Select option":
            self.create_combo_drop_table()
            self.combo_drop_truncate.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_drop.setMaximumHeight(30)
            self.table_drop.setRowCount(1)
            self.combo_drop_truncate.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_drop_table(self):
        self.combo_drop_table = QComboBox()
        self.combo_drop_table.addItem("Select table")
        self.combo_drop_table.addItems(ConnectDb.get_all_tables(self))
        self.combo_drop_table.currentIndexChanged.connect(self.get_combo_drop_table)
        self.table_drop.setCellWidget(0, 1, self.combo_drop_table)

    def get_combo_drop_table(self):
        current_text = self.combo_drop_table.currentText()
        if current_text != "Select table":
            self.combo_drop_table.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            current_option = self.combo_drop_truncate.currentText()
            if current_option == "DELETE FROM":
                self.table_drop.setMaximumHeight(93)
                self.table_drop.setRowCount(3)
                self.create_checkbox_truncate()
                self.create_delete_combo_where()
            else:
                self.table_drop.setMaximumHeight(30)
                self.table_drop.setRowCount(1)
        else:
            self.table_drop.setMaximumHeight(30)
            self.table_drop.setRowCount(1)
            self.combo_drop_table.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_checkbox_truncate(self):
        self.checkbox_truncate = QCheckBox(text="Reset AUTOINCREMENT")
        self.checkbox_truncate.setTristate(False)
        self.checkbox_truncate.stateChanged.connect(self.get_checkbox_truncate)
        self.table_drop.setCellWidget(1, 0, self.checkbox_truncate)

    def get_checkbox_truncate(self):
        state = self.checkbox_truncate.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_truncate.setStyleSheet("color : green")
            self.table_drop.removeCellWidget(2, 1)
            self.delete_combo_where.setCurrentIndex(0)
        else:
            self.checkbox_truncate.setStyleSheet("color : black")

    def create_delete_combo_where(self):
        self.delete_combo_where = QComboBox()
        self.delete_combo_where.addItem("Select WHERE")
        current_text = self.combo_drop_table.currentText()
        fields = self.get_fields_table(current_text)
        for field in fields:
            field = "WHERE " + field + " ="
            self.delete_combo_where.addItem(field)
        self.delete_combo_where.currentIndexChanged.connect(self.get_delete_combo_where)
        self.table_drop.setCellWidget(2, 0, self.delete_combo_where)

    def get_delete_combo_where(self):
        current_text = self.delete_combo_where.currentText()
        if current_text != "Select WHERE":
            state = self.checkbox_truncate.checkState()
            if state == Qt.CheckState.Checked:
                self.checkbox_truncate.setCheckState(Qt.CheckState.Unchecked)
            self.create_delete_combo_where_result()
            self.delete_combo_where.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_drop.removeCellWidget(2, 1)
            self.delete_combo_where.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_delete_combo_where_result(self):
        current_field = self.delete_combo_where.currentText()
        current_field = current_field.replace("WHERE ", "")
        current_field = current_field.replace(" =", "")
        current_table = self.combo_drop_table.currentText()
        current_table = "FROM " + current_table
        self.delete_combo_where_result = QComboBox()
        values = ConnectDb.get_data_column(self, current_table, current_field)
        for value in values:
            self.delete_combo_where_result.addItem(value)
        self.delete_combo_where_result.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_drop.setCellWidget(2, 1, self.delete_combo_where_result)
