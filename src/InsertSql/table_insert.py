from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableInsert(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_insert()
        self.create_label_insert()
        self.create_label_values()
        self.create_combo_insert()
        self.create_label_insert_prths1()

    def create_table_insert(self):
        self.table_insert = QTableWidget(2, 3)
        self.table_insert.setMaximumHeight(62)
        self.table_insert.setColumnWidth(0, 100)
        self.table_insert.setColumnWidth(1, 100)
        self.table_insert.setColumnWidth(2, 50)
        for i in range(self.get_table_len()):
            self.table_insert.setColumnWidth(i + 3, 50)
        self.table_insert.horizontalHeader().setVisible(False)
        self.table_insert.verticalHeader().setVisible(False)

    def create_label_insert(self):
        self.label_insert = QLabel("INSERT INTO")
        self.table_insert.setCellWidget(0, 0, self.label_insert)
        self.label_insert.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_insert.setStyleSheet("QLabel { color: green; }")

    def create_label_values(self):
        self.label_values = QLabel("VALUES")
        self.label_values.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_values.setStyleSheet("QLabel { color: green; }")
        self.table_insert.setCellWidget(1, 0, self.label_values)

    def create_combo_insert(self):
        self.combo_insert = QComboBox()
        self.combo_insert.addItem("Select table")
        self.combo_insert.addItems(ConnectDb.get_all_tables(self))
        self.table_insert.setCellWidget(0, 1, self.combo_insert)
        self.combo_insert.currentIndexChanged.connect(self.get_combo_insert)

    def create_label_insert_prths1(self):
        self.label_insert_prths1 = QLabel("(")
        self.label_insert_prths1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_insert.setCellWidget(0, 2, self.label_insert_prths1)
        self.label_insert_prths1.setStyleSheet("QLabel { color: green; }")

    def create_label_insert_prths2(self):
        self.label_insert_prths2 = QLabel(")")
        self.label_insert_prths2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_insert.setColumnWidth(len(self.fields) + 3, 50)
        self.table_insert.setCellWidget(
            0, len(self.fields) + 3, self.label_insert_prths2
        )
        self.label_insert_prths2.setStyleSheet("QLabel { color: green; }")

    def get_combo_insert(self):
        self.table_insert.setColumnCount(3)
        column_index = self.table_insert.columnCount()
        current_text = self.combo_insert.currentText()
        self.fields = []
        if current_text != "Select table":
            item = ConnectDb.get_primary_key(self, current_text)
            self.structure = ConnectDb.get_structure(self, current_text)
            fields = ConnectDb.get_fields_table(self, current_text)
            self.create_label_structure()
            self.combo_insert.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            for x in fields:
                if x in item:
                    pass
                else:
                    self.fields.append(x)
            self.lines = {}
            self.labels = {}
            for x in range(len(self.fields) + 1):
                self.table_insert.insertColumn(column_index)
            for i, field in enumerate(self.fields, 3):
                self.labels["labelInsetField" + str(i)] = QLabel(field)
                self.labels["labelInsetField" + str(i)].setAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )
                self.labels["labelInsetField" + str(i)].setStyleSheet(
                    "QLabel { color: black; }"
                )
                self.table_insert.setCellWidget(
                    0, i, self.labels["labelInsetField" + str(i)]
                )
                self.lines["self.lineEditInsert" + str(i)] = QLineEdit()
                self.lines["self.lineEditInsert" + str(i)].setAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )
                self.lines["self.lineEditInsert" + str(i)].setStyleSheet(
                    self.style_qLine
                )
                self.lines["self.lineEditInsert" + str(i)].textChanged.connect(
                    self.change_lineedit_insert
                )
                self.table_insert.setCellWidget(
                    1, i, self.lines["self.lineEditInsert" + str(i)]
                )
                self.table_insert.setColumnWidth(i, 100)
                self.create_label_insert_value_prths1()
                self.create_label_insert_value_prths2()
                self.create_label_insert_prths2()
        else:
            self.table_structure.removeCellWidget(0, 0)
            self.combo_insert.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def change_lineedit_insert(self):
        for i, field in enumerate(self.fields, 3):
            if len(self.lines["self.lineEditInsert" + str(i)].text()) is not None:
                self.labels["labelInsetField" + str(i)].setStyleSheet(
                    "QLabel { color: black; }"
                )
                self.lines["self.lineEditInsert" + str(i)].setStyleSheet(
                    self.style_qLine
                )
            if len(self.lines["self.lineEditInsert" + str(i)].text()) > 0:
                self.labels["labelInsetField" + str(i)].setStyleSheet(
                    "QLabel { color: green; }"
                )
                self.lines["self.lineEditInsert" + str(i)].setStyleSheet(
                    self.style_qLine1
                )

    def create_label_insert_value_prths1(self):
        self.label_insert_value_prths1 = QLabel("(")
        self.label_insert_value_prths1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_insert.setCellWidget(1, 2, self.label_insert_value_prths1)
        self.label_insert_value_prths1.setStyleSheet("QLabel { color: green; }")

    def create_label_insert_value_prths2(self):
        self.label_insert_value_prths2 = QLabel(")")
        self.label_insert_value_prths2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_insert.setCellWidget(
            1, len(self.fields) + 3, self.label_insert_value_prths2
        )
        self.label_insert_value_prths2.setStyleSheet("QLabel { color: green; }")
