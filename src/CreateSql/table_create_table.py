from PyQt6.QtWidgets import (
    QTableWidget,
    QComboBox,
    QLineEdit,
    QCheckBox,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableCreateTable(ConnectDb):
    def __init__(self):
        super().__init__()
        self.hight_table = 31
        self.main_layout_create = QHBoxLayout()
        self.table_layout = QVBoxLayout()
        self.table_layout_button_create = QVBoxLayout()
        self.main_layout_create.addLayout(self.table_layout)
        self.create_table_table()

    def create_table_table(self):
        self.table_create_table = QTableWidget(1, 7)
        self.table_create_table.setFixedHeight(self.hight_table)
        self.table_create_table.setColumnWidth(0, 150)
        self.table_create_table.setColumnWidth(1, 120)
        self.table_create_table.setColumnWidth(2, 90)
        self.table_create_table.setColumnWidth(3, 110)
        self.table_create_table.setColumnWidth(4, 130)
        self.table_create_table.setColumnWidth(5, 80)
        self.table_create_table.setColumnWidth(6, 50)
        self.table_create_table.horizontalHeader().setVisible(False)
        self.table_create_table.verticalHeader().setVisible(False)
        self.row_table = self.table_create_table.rowCount()
        self.table_layout.addWidget(self.table_create_table)
        self.create_create_label_table()
        self.create_lineedit_create_table()
        self.create_create_label_prts1()
        self.create_table_addrow_button()
        self.create_table_removerow_button()

    def remove_row(self):
        self.table_create_table.removeRow(self.row_table)
        if self.number_of_rows > 1:
            self.number_of_rows -= 1
            self.hight_table -= 31
            self.table_create_table.setFixedHeight(self.hight_table)

    number_of_rows = 1

    def add_row(self):
        self.table_create_table.insertRow(self.row_table)
        self.hight_table += 31
        self.table_create_table.setFixedHeight(self.hight_table)
        self.number_of_rows += 1
        self.table_field_edit = {}
        self.table_field_combo = {}
        self.table_field_checkbox_nn = {}
        self.table_field_checkbox_pk = {}
        self.table_field_checkbox_ai = {}
        self.table_field_checkbox_u = {}
        self.table_fields = []
        self.table_label_coma = {}
        self.create_create_new_row()

    def create_create_new_row(self):
        for row in range(self.number_of_rows):
            self.table_field_edit["line_edit" + str(row)] = QLineEdit()
            self.table_field_edit["line_edit" + str(row)].setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )
            self.table_field_edit["line_edit" + str(row)].setStyleSheet(
                self.style_qLine1
            )
            self.table_field_edit["line_edit" + str(row)].textChanged.connect(
                self.create_foreignkey_combo_fields1
            )
            self.table_create_table.setCellWidget(
                row + 1, 0, self.table_field_edit["line_edit" + str(row)]
            )
            self.table_field_combo["Combo" + str(row)] = QComboBox()
            self.table_field_combo["Combo" + str(row)].addItems(
                [
                    "Select type",
                    "INTEGER",
                    "TEXT",
                    "BLOB",
                    "NUMERIC",
                    "DATE",
                    "DATETIME",
                ]
            )
            self.table_create_table.setCellWidget(
                row + 1, 1, self.table_field_combo["Combo" + str(row)]
            )
            self.table_field_checkbox_nn["Check" + str(row)] = QCheckBox(
                text="NOT NULL"
            )
            self.table_field_checkbox_nn["Check" + str(row)].setTristate(False)
            self.table_create_table.setCellWidget(
                row + 1, 2, self.table_field_checkbox_nn["Check" + str(row)]
            )
            self.table_field_checkbox_pk["Check" + str(row)] = QCheckBox(
                text="PRIMARY KEY"
            )
            self.table_field_checkbox_pk["Check" + str(row)].stateChanged.connect(
                self.get_checkbox_pk
            )
            self.table_field_checkbox_pk["Check" + str(row)].setTristate(False)
            self.table_create_table.setCellWidget(
                row + 1, 3, self.table_field_checkbox_pk["Check" + str(row)]
            )
            self.table_field_checkbox_ai["Check" + str(row)] = QCheckBox(
                text="AUTOINCREMENT"
            )
            self.table_field_checkbox_ai["Check" + str(row)].stateChanged.connect(
                self.get_checkbox_ai
            )
            self.table_field_checkbox_ai["Check" + str(row)].setTristate(False)
            self.table_create_table.setCellWidget(
                row + 1, 4, self.table_field_checkbox_ai["Check" + str(row)]
            )
            self.table_field_checkbox_u["Check" + str(row)] = QCheckBox(text="UNIQUE")
            self.table_field_checkbox_u["Check" + str(row)].setTristate(False)
            self.table_create_table.setCellWidget(
                row + 1, 5, self.table_field_checkbox_u["Check" + str(row)]
            )

        for row in list(range(1, self.number_of_rows - 1)):
            self.table_label_coma["Coma" + str(row)] = QLabel(",")
            self.table_label_coma["Coma" + str(row)].setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )
            self.table_label_coma["Coma" + str(row)].setStyleSheet("color: green")
            self.table_create_table.setCellWidget(
                row, 6, self.table_label_coma["Coma" + str(row)]
            )

        for self.row_prts2 in list(range(self.number_of_rows - 1, self.number_of_rows)):
            self.create_label_prts2 = QLabel(")")
            self.create_label_prts2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.create_label_prts2.setStyleSheet("color: green")
            self.table_create_table.setCellWidget(
                self.row_prts2, 6, self.create_label_prts2
            )

    def get_checkbox_ai(self):
        for row in range(self.number_of_rows):
            state = self.table_field_checkbox_ai["Check" + str(row)].checkState()
            if state == Qt.CheckState.Checked:
                self.table_field_checkbox_pk["Check" + str(row)].setCheckState(
                    Qt.CheckState.Checked
                )

    def get_checkbox_pk(self):
        for row in range(self.number_of_rows):
            state = self.table_field_checkbox_pk["Check" + str(row)].checkState()
            if state == Qt.CheckState.Unchecked:
                self.table_field_checkbox_ai["Check" + str(row)].setCheckState(
                    Qt.CheckState.Unchecked
                )

    def create_create_label_table(self):
        self.create_label_table = QLabel("CREATE TABLE")
        self.create_label_table.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.create_label_table.setStyleSheet("color: green")
        self.table_create_table.setCellWidget(0, 0, self.create_label_table)

    def create_create_label_prts1(self):
        self.create_label_prts1 = QLabel("(")
        self.create_label_prts1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.create_label_prts1.setStyleSheet("color: green")
        self.table_create_table.setCellWidget(0, 2, self.create_label_prts1)

    def create_lineedit_create_table(self):
        self.line_edit_create_table = QLineEdit()
        self.line_edit_create_table.setStyleSheet(self.style_qLine1)
        self.line_edit_create_table.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_edit_create_table.textChanged.connect(self.get_lineedit_create_table)
        self.table_create_table.setCellWidget(0, 1, self.line_edit_create_table)

    def get_lineedit_create_table(self):
        current_text = self.line_edit_create_table.text()
        if len(current_text) is not None:
            self.line_edit_create_table.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.line_edit_create_table.setStyleSheet(self.style_qLine1)

    def create_table_addrow_button(self):
        self.button_add = QPushButton("Add Table Field")
        self.table_layout_button_create.addWidget(self.button_add)
        self.main_layout_create.addLayout(self.table_layout_button_create)
        self.button_add.clicked.connect(self.add_row)

    def create_table_removerow_button(self):
        self.button_remove = QPushButton("Remove Table Field")
        self.table_layout_button_create.addWidget(self.button_remove)
        self.button_remove.clicked.connect(self.remove_row)
