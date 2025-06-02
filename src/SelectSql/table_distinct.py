from PyQt6.QtWidgets import QTableWidget, QComboBox
from PyQt6 import QtGui
from src.UtilsSql.connect_db import ConnectDb


class TableDistinct(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_distinct()

    def create_table_distinct(self):
        self.table_distinct_option = QTableWidget(1, 2)
        self.table_distinct_option.setMaximumHeight(30)
        self.table_distinct_option.setColumnWidth(0, 200)
        self.table_distinct_option.horizontalHeader().setVisible(False)
        self.table_distinct_option.verticalHeader().setVisible(False)
        self.create_combobox_distinct()

    def create_combobox_distinct(self):
        row = self.table_distinct_option.rowCount()
        self.combo_distinct = QComboBox()
        self.combo_distinct.addItem("Select DISTINCT")
        for item in self.get_list_fields():
            item = "(DISTINCT " + item + ")"
            self.combo_distinct.addItem(item)
        self.table_distinct_option.setCellWidget(0, 0, self.combo_distinct)
        self.combo_distinct.currentIndexChanged.connect(self.get_combo_distinct)
        firstItem = QtGui.QStandardItem(row)
        firstItem.setSelectable(False)

    def get_combo_distinct(self):
        current_text = self.combo_distinct.currentText()
        if current_text != "Select DISTINCT":
            self.combo_distinct.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_distinct.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
