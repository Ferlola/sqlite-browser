from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit, QCheckBox, QLabel
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from src.UtilsSql.connect_db import ConnectDb


class TableSelectSum(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_select_sum()

    def create_table_select_sum(self):
        self.table_select_sum = QTableWidget(1, 7)
        self.table_select_sum.setMaximumHeight(30)
        self.table_select_sum.setColumnWidth(0, 150)
        self.table_select_sum.setColumnWidth(1, 50)
        self.table_select_sum.setColumnWidth(2, 50)
        self.table_select_sum.setColumnWidth(3, 120)
        self.table_select_sum.setColumnWidth(4, 50)
        self.table_select_sum.setColumnWidth(5, 50)
        self.table_select_sum.setColumnWidth(6, 50)
        self.table_select_sum.horizontalHeader().setVisible(False)
        self.table_select_sum.verticalHeader().setVisible(False)
        self.create_combo_select_sum1()

    def create_combo_select_sum1(self):
        self.combobox_select_sum1 = QComboBox()
        self.combobox_select_sum1.addItem("Select field")
        for item in self.get_list_fields():
            item = "(" + item
            self.combobox_select_sum1.addItem(item)
        self.table_select_sum.setCellWidget(0, 0, self.combobox_select_sum1)
        self.combobox_select_sum1.currentIndexChanged.connect(
            self.get_combo_select_sum1
        )

    def get_combo_select_sum1(self):
        current_text = self.combobox_select_sum1.currentText()
        if current_text != "Select field":
            self.create_checkbox_sum1()
            self.create_label_parh3()
            self.create_checkbox_sum2()
            self.combobox_select_sum1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_select_sum.removeCellWidget(0, 1)
            self.table_select_sum.removeCellWidget(0, 2)
            self.table_select_sum.removeCellWidget(0, 3)
            self.table_select_sum.removeCellWidget(0, 4)
            self.table_select_sum.removeCellWidget(0, 5)
            self.table_select_sum.removeCellWidget(0, 6)
            self.combobox_select_sum1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_checkbox_sum1(self):
        self.checkbox_sum1 = QCheckBox(text="*")
        self.checkbox_sum1.setTristate(False)
        self.checkbox_sum1.setStyleSheet("color: black")
        self.checkbox_sum1.stateChanged.connect(self.on_state_changed1)
        self.table_select_sum.setCellWidget(0, 1, self.checkbox_sum1)

    def on_state_changed1(self):
        state = self.checkbox_sum1.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_sum1.setStyleSheet("color: green")
            self.create_number_edit()
            self.create_combo_select_sum2()
        else:
            self.checkbox_sum1.setStyleSheet("color: black")
            self.table_select_sum.removeCellWidget(0, 2)
            self.table_select_sum.removeCellWidget(0, 3)

    def create_number_edit(self):
        self.number_edit = QLineEdit()
        self.number_edit.setStyleSheet(self.style_qLine)
        self.number_edit.textChanged.connect(self.changed_number_edit)
        self.table_select_sum.setCellWidget(0, 2, self.number_edit)

    def changed_number_edit(self):
        texto = self.number_edit.text()
        if len(texto) is not None:
            self.checkbox_sum1.setStyleSheet("color: black")
            self.number_edit.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.checkbox_sum1.setStyleSheet("color: green")
            self.number_edit.setStyleSheet(self.style_qLine1)

    def create_combo_select_sum2(self):
        row = self.table_select_sum.rowCount()
        self.combobox_select_sum2 = QComboBox()
        self.combobox_select_sum2.addItem("Select field")
        self.combobox_select_sum2.addItems(self.get_list_fields())
        self.table_select_sum.setCellWidget(0, 3, self.combobox_select_sum2)
        self.combobox_select_sum2.currentIndexChanged.connect(
            self.get_combo_select_sum2
        )
        firstItem = QtGui.QStandardItem(row)
        firstItem.setSelectable(False)

    def get_combo_select_sum2(self):
        current_text = self.combobox_select_sum2.currentText()
        if current_text != "Select field":
            self.create_checkbox_sum2()
            self.combobox_select_sum2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combobox_select_sum2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_label_parh3(self):
        self.label_prh3 = QLabel(")")
        self.label_prh3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_select_sum.setCellWidget(0, 4, self.label_prh3)
        self.label_prh3.setStyleSheet("QLabel { color: green; }")

    def create_checkbox_sum2(self):
        self.checkbox_sum2 = QCheckBox(text="AS")
        self.checkbox_sum2.setTristate(False)
        self.checkbox_sum2.setStyleSheet("color: black")
        self.checkbox_sum2.stateChanged.connect(self.on_state_changed2)
        self.table_select_sum.setCellWidget(0, 5, self.checkbox_sum2)

    def on_state_changed2(self):
        state = self.checkbox_sum2.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_sum2.setText("AS")
            self.create_sum_as()
        else:
            self.table_select_sum.removeCellWidget(0, 6)
            self.checkbox_sum2.setText("AS")

    def create_sum_as(self):
        self.sum_as = QLineEdit()
        self.sum_as.setStyleSheet(self.style_qLine)
        self.sum_as.textChanged.connect(self.changed_sum_as)
        self.table_select_sum.setCellWidget(0, 6, self.sum_as)

    def changed_sum_as(self):
        texto = self.sum_as.text()
        if len(texto) is not None:
            self.checkbox_sum2.setStyleSheet("color: black")
            self.sum_as.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.checkbox_sum2.setStyleSheet("color: green")
            self.sum_as.setStyleSheet(self.style_qLine1)
