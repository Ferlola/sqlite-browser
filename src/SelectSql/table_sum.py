from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit
from PyQt6 import QtGui
from src.UtilsSql.connect_db import ConnectDb


class TableSum(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_sum()

    def create_table_sum(self):
        self.table_sum = QTableWidget(1, 4)
        self.table_sum.setMaximumHeight(30)
        self.table_sum.setColumnWidth(0, 150)
        self.table_sum.setColumnWidth(1, 150)
        self.table_sum.setColumnWidth(2, 50)
        self.table_sum.setColumnWidth(3, 50)
        self.table_sum.horizontalHeader().setVisible(False)
        self.table_sum.verticalHeader().setVisible(False)
        self.create_combo_sum()

    def create_combo_sum(self):
        row = self.table_sum.rowCount()
        self.combo_sum = QComboBox()
        self.combo_sum.addItem("SUM")
        self.combo_sum.addItem("(*)")
        for item in self.get_list_fields():
            item = ",SUM(" + item + ")"
            self.combo_sum.addItem(item)
        self.table_sum.setCellWidget(0, 0, self.combo_sum)
        self.combo_sum.currentIndexChanged.connect(self.get_combo_sum)
        firstItem = QtGui.QStandardItem(row)
        firstItem.setSelectable(False)

    def get_combo_sum(self):
        current_text = self.combo_sum.currentText()
        if current_text != "Select field":
            self.create_combo_sum_as()
            self.combo_sum.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.combo_sum.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_sum_as(self):
        self.combo_as = QComboBox()
        self.combo_as.addItems(["(AS)", "AS"])
        self.table_sum.setCellWidget(0, 2, self.combo_as)
        self.combo_as.currentIndexChanged.connect(self.get_combo_as)

    def get_combo_as(self):
        current_text = self.combo_as.currentText()
        if current_text == "(AS)":
            self.combo_as.setStyleSheet("QComboBox{{ color : {} }}".format("black"))
            self.table_sum.removeCellWidget(0, 3)
        else:
            self.combo_as.setStyleSheet("QComboBox{{ color : {} }}".format("green"))
            self.line_edit = QLineEdit()
            self.line_edit.setStyleSheet(self.style_qLine)
            self.table_sum.setCellWidget(0, 3, self.line_edit)
