from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from src.UtilsSql.connect_db import ConnectDb


class TableAvg(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_avg()

    def create_table_avg(self):
        self.table_avg = QTableWidget(1, 6)
        self.table_avg.setMaximumHeight(30)
        self.table_avg.setColumnWidth(0, 150)
        self.table_avg.setColumnWidth(1, 50)
        self.table_avg.setColumnWidth(2, 50)
        self.table_avg.setColumnWidth(3, 150)
        self.table_avg.horizontalHeader().setVisible(False)
        self.table_avg.verticalHeader().setVisible(False)
        self.create_combo_avg1()

    def create_combo_avg1(self):
        row = self.table_avg.rowCount()
        self.combo_avg1 = QComboBox()
        self.combo_avg1.addItem("Select field")
        self.combo_avg1.addItem("(*)")
        for item in self.get_list_fields():
            item = "(" + item + ")"
            self.combo_avg1.addItem(item)
        self.table_avg.setCellWidget(0, 0, self.combo_avg1)
        self.combo_avg1.currentIndexChanged.connect(self.get_combo_avg1)
        first_item = QtGui.QStandardItem(row)
        first_item.setSelectable(False)

    def get_combo_avg1(self):
        current_text = self.combo_avg1.currentText()
        if current_text != "Select field":
            self.combo_avg1.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            self.create_checkbox_avg()
            self.create_combo_avg_count()
            self.create_combo_avg2()
        else:
            self.table_avg.removeCellWidget(0, 1)
            self.table_avg.removeCellWidget(0, 2)
            self.table_avg.removeCellWidget(0, 3)
            self.table_avg.removeCellWidget(0, 4)
            self.table_avg.removeCellWidget(0, 5)
            self.combo_avg1.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_checkbox_avg(self):
        self.checkbox_avg = QCheckBox(text="AS")
        self.checkbox_avg.setTristate(False)
        self.checkbox_avg.setStyleSheet("color: black")
        self.checkbox_avg.stateChanged.connect(self.on_state_changed_avg)
        self.table_avg.setCellWidget(0, 1, self.checkbox_avg)

    def on_state_changed_avg(self):
        state = self.checkbox_avg.checkState()
        if state == Qt.CheckState.Checked:
            self.create_avg_as()
        else:
            self.table_avg.removeCellWidget(0, 2)

    def create_avg_as(self):
        self.lineedit_avg_as = QLineEdit()
        self.lineedit_avg_as.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineedit_avg_as.setStyleSheet(self.style_qLine)
        self.table_avg.setCellWidget(0, 2, self.lineedit_avg_as)
        self.lineedit_avg_as.textChanged.connect(self.changed_avg_as)

    def changed_avg_as(self):
        texto = self.lineedit_avg_as.text()
        if len(texto) is not None:
            self.checkbox_avg.setStyleSheet("color: black")
            self.lineedit_avg_as.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.checkbox_avg.setStyleSheet("color: green")
            self.lineedit_avg_as.setStyleSheet(self.style_qLine1)

    def create_combo_avg2(self):
        self.combo_avg2 = QComboBox()
        self.combo_avg2.addItem("Select field")
        for item in self.get_list_fields():
            item = "," + item
            self.combo_avg2.addItem(item)
        self.table_avg.setCellWidget(0, 5, self.combo_avg2)
        self.combo_avg2.currentIndexChanged.connect(self.get_combo_avg2)

    def get_combo_avg2(self):
        current_text = self.combo_avg2.currentText()
        if current_text != "Select field":
            self.combo_avg2.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.combo_avg2.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_avg_count(self):
        self.combo_aAvg_count = QComboBox()
        self.combo_aAvg_count.addItems(["count/avg/sum", ",COUNT", ",AVG", ",SUM"])
        self.table_avg.setCellWidget(0, 3, self.combo_aAvg_count)
        self.combo_aAvg_count.currentIndexChanged.connect(self.get_combo_avg_count)

    def get_combo_avg_count(self):
        current_text = self.combo_aAvg_count.currentText()
        if current_text != "count/avg/sum":
            self.create_combo_avg_fields()
            self.combo_aAvg_count.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_avg.removeCellWidget(0, 4)
            self.combo_aAvg_count.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_avg_fields(self):
        self.combo_avg_fields = QComboBox()
        self.combo_avg_fields.addItem("Select field")
        for item in self.get_list_fields():
            item = "(" + item + ")"
            self.combo_avg_fields.addItem(item)
        self.table_avg.setCellWidget(0, 4, self.combo_avg_fields)
        self.combo_avg_fields.currentIndexChanged.connect(self.get_combo_avg_fields)

    def get_combo_avg_fields(self):
        current_text = self.combo_avg_fields.currentText()
        if current_text != "Select field":
            self.combo_avg_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_avg_fields.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
