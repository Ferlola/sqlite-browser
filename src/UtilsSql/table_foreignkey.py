from PyQt6.QtWidgets import QTableWidget, QComboBox, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableForeignKey(ConnectDb):
    def __init__(self):
        super().__init__()
        if ConnectDb.get_table_len(self) != 0:
            self.create_table_foreignkey()

    def create_table_foreignkey(self):
        self.table_foreign_key = QTableWidget(1, 5)
        self.table_foreign_key.setMaximumHeight(30)
        self.table_foreign_key.setColumnWidth(0, 150)
        self.table_foreign_key.setColumnWidth(1, 100)
        self.table_foreign_key.setColumnWidth(2, 150)
        self.table_foreign_key.setColumnWidth(3, 150)
        self.table_foreign_key.setColumnWidth(4, 50)
        self.table_foreign_key.horizontalHeader().setVisible(False)
        self.table_foreign_key.verticalHeader().setVisible(False)
        self.rowTableForeignKey = self.table_foreign_key.rowCount()
        self.create_foreignkey_label1()
        self.create_foreignkey_combo_fields1()
        self.create_foreignkey_label()

    def create_foreignkey_label1(self):
        self.foreignkey_label1 = QLabel(",FOREIGN KEY")
        self.foreignkey_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foreignkey_label1.setStyleSheet("color: green")
        self.table_foreign_key.setCellWidget(0, 0, self.foreignkey_label1)

    def create_foreignkey_combo_fields1(self):
        self.foreignkey_combo_fields1 = QComboBox()
        self.foreignkey_combo_fields1.addItem("Select field")
        try:
            for row in range(self.number_of_rows - 1):
                item = "(" + self.table_field_edit["line_edit" + str(row)].text() + ")"
                self.foreignkey_combo_fields1.addItem(item)
            self.foreignkey_combo_fields1.currentIndexChanged.connect(
                self.get_foreignkey_combo_fields1
            )
            self.table_foreign_key.setCellWidget(0, 1, self.foreignkey_combo_fields1)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_foreignkey_combo_fields1")
        try:
            for item in ConnectDb.get_list_fields(self):
                item = "(" + item + ")"
                self.foreignkey_combo_fields1.addItem(item)
            self.foreignkey_combo_fields1.currentIndexChanged.connect(
                self.get_foreignkey_combo_fields1
            )
            self.table_foreign_key.setCellWidget(0, 1, self.foreignkey_combo_fields1)
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_foreignkey_combo_fields1")

    def get_foreignkey_combo_fields1(self):
        current_text = self.foreignkey_combo_fields1.currentText()
        if current_text != "Select field":
            self.create_references_label1()
            self.create_references_combo1()
            self.foreignkey_combo_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_foreign_key.removeCellWidget(0, 2)
            self.table_foreign_key.removeCellWidget(0, 3)
            self.table_foreign_key.removeCellWidget(0, 4)
            self.table_foreign_key.setMaximumHeight(30)
            self.table_foreign_key.setRowCount(1)
            self.foreignkey_combo_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_references_label1(self):
        self.references_label1 = QLabel("REFERENCES")
        self.references_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.references_label1.setStyleSheet("color: green")
        self.table_foreign_key.setCellWidget(0, 2, self.references_label1)

    def create_references_combo1(self):
        self.references_combo1 = QComboBox()
        self.references_combo1.addItem("Select field")
        try:
            for row in range(self.number_of_rows - 1):
                tableField = ConnectDb.get_table_field(
                    self, self.table_field_edit["line_edit" + str(row)].text()
                )
                if tableField is None:
                    tableField = self.line_edit_create_table.text()
                item = (
                    tableField
                    + "("
                    + self.table_field_edit["line_edit" + str(row)].text()
                    + ")"
                )
                self.references_combo1.addItem(item)
                self.references_combo1.currentIndexChanged.connect(
                    self.get_references_combo1
                )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_references_combo1")
        try:
            items = ConnectDb.get_all_references(self)
            for item in items:
                self.references_combo1.addItem(item)
            self.references_combo1.currentIndexChanged.connect(
                self.get_references_combo1
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_references_combo1")
        self.table_foreign_key.setCellWidget(0, 3, self.references_combo1)

    def get_references_combo1(self):
        current_text = self.references_combo1.currentText()
        if current_text != "Select field":
            self.table_foreign_key.setRowCount(2)
            self.table_foreign_key.setMaximumHeight(62)
            self.create_foreignkey_label2()
            self.create_foreignkey_combo_fields2()
            self.references_combo1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_foreignkey_label()
            self.table_foreign_key.setCellWidget(0, 4, self.foreigntkey_label)
            self.table_create_table.removeCellWidget(self.row_prts2, 6)
        else:
            self.table_foreign_key.setRowCount(1)
            self.table_foreign_key.setMaximumHeight(30)
            self.table_foreign_key.removeCellWidget(0, 4)
            self.create_create_new_row()
            self.table_create_table.setCellWidget(
                self.row_prts2, 6, self.create_label_prts2
            )
            self.references_combo1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_foreignkey_label2(self):
        self.foreignkey_label2 = QLabel(",FOREIGN KEY")
        self.foreignkey_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foreignkey_label2.setStyleSheet("color: green")
        self.table_foreign_key.setCellWidget(1, 0, self.foreignkey_label2)

    def create_foreignkey_combo_fields2(self):
        self.foreignkey_combo_fields2 = QComboBox()
        self.foreignkey_combo_fields2.addItem("Select field")
        try:
            for row in range(self.number_of_rows - 1):
                item = "(" + self.table_field_edit["line_edit" + str(row)].text() + ")"
                self.foreignkey_combo_fields2.addItem(item)
            self.foreignkey_combo_fields2.currentIndexChanged.connect(
                self.get_foreignkey_combo_fields2
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_foreignkey_combo_fields2")
        try:
            for item in self.get_list_fields():
                item = "(" + item + ")"
                self.foreignkey_combo_fields2.addItem(item)
            self.foreignkey_combo_fields2.currentIndexChanged.connect(
                self.get_foreignkey_combo_fields2
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_foreignkey_combo_fields2")
        self.table_foreign_key.setCellWidget(1, 1, self.foreignkey_combo_fields2)

    def get_foreignkey_combo_fields2(self):
        current_text = self.foreignkey_combo_fields2.currentText()
        if current_text != "Select field":
            self.create_references_label2()
            self.create_references_combo2()
            self.foreignkey_combo_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_foreign_key.setRowCount(2)
            self.table_foreign_key.setMaximumHeight(62)
            self.table_foreign_key.removeCellWidget(1, 2)
            self.table_foreign_key.removeCellWidget(1, 3)
            self.foreignkey_combo_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_references_label2(self):
        self.references_label2 = QLabel("REFERENCES")
        self.references_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.references_label2.setStyleSheet("color: green")
        self.table_foreign_key.setCellWidget(1, 2, self.references_label2)

    def create_references_combo2(self):
        self.references_combo2 = QComboBox()
        self.references_combo2.addItem("Select field")
        try:
            for row in range(self.number_of_rows - 1):
                tableField = ConnectDb.get_table_field(
                    self, self.table_field_edit["line_edit" + str(row)].text()
                )
                if tableField is None:
                    tableField = self.line_edit_create_table.text()
                item = (
                    tableField
                    + "("
                    + self.table_field_edit["line_edit" + str(row)].text()
                    + ")"
                )
                self.references_combo2.addItem(item)
            self.references_combo2.currentIndexChanged.connect(
                self.get_references_combo2
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_references_combo2")
        try:
            items = ConnectDb.get_all_references(self)
            for item in items:
                self.references_combo2.addItem(item)
            self.references_combo2.currentIndexChanged.connect(
                self.get_references_combo2
            )

        except (AttributeError, TypeError) as e:
            print(f"{e} :create_references_combo2")
        self.table_foreign_key.setCellWidget(1, 3, self.references_combo2)

    def get_references_combo2(self):
        current_text = self.references_combo2.currentText()
        if current_text != "Select field":
            self.table_foreign_key.setRowCount(3)
            self.table_foreign_key.setMaximumHeight(93)
            self.create_foreignkey_label3()
            self.create_foreigney_combo_fields3()
            self.references_combo2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.table_foreign_key.removeCellWidget(0, 4)
            self.create_foreignkey_label()
            self.table_foreign_key.setCellWidget(1, 4, self.foreigntkey_label)
        else:
            self.table_foreign_key.setRowCount(2)
            self.table_foreign_key.setMaximumHeight(62)
            self.create_foreignkey_label()
            self.table_foreign_key.setCellWidget(0, 4, self.foreigntkey_label)
            self.table_foreign_key.removeCellWidget(1, 4)
            self.references_combo2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_foreignkey_label3(self):
        self.foreignkey_label3 = QLabel(",FOREIGN KEY")
        self.foreignkey_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foreignkey_label3.setStyleSheet("color: green")
        self.table_foreign_key.setCellWidget(2, 0, self.foreignkey_label3)

    def create_foreigney_combo_fields3(self):
        self.foreignkey_combo_fields3 = QComboBox()
        self.foreignkey_combo_fields3.addItem("Select field")
        try:
            for row in range(self.number_of_rows - 1):
                item = "(" + self.table_field_edit["line_edit" + str(row)].text() + ")"
                self.foreignkey_combo_fields3.addItem(item)
            self.foreignkey_combo_fields3.currentIndexChanged.connect(
                self.get_foreignkey_combo_fields3
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_foreigney_combo_fields3")
        try:
            for item in self.get_list_fields():
                item = "(" + item + ")"
                self.foreignkey_combo_fields3.addItem(item)
            self.foreignkey_combo_fields3.currentIndexChanged.connect(
                self.get_foreignkey_combo_fields3
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_foreigney_combo_fields3")
        self.table_foreign_key.setCellWidget(2, 1, self.foreignkey_combo_fields3)

    def get_foreignkey_combo_fields3(self):
        current_text = self.foreignkey_combo_fields3.currentText()
        if current_text != "Select field":
            self.create_references_label3()
            self.create_references_combo3()
            self.foreignkey_combo_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_foreign_key.removeCellWidget(2, 2)
            self.table_foreign_key.removeCellWidget(2, 3)
            self.foreignkey_combo_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_references_label3(self):
        self.references_label3 = QLabel("REFERENCES")
        self.references_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.references_label3.setStyleSheet("color: green")
        self.table_foreign_key.setCellWidget(2, 2, self.references_label3)

    def create_references_combo3(self):
        self.references_combo3 = QComboBox()
        self.references_combo3.addItem("Select field")
        try:
            for row in range(self.number_of_rows - 1):
                tableField = ConnectDb.get_table_field(
                    self, self.table_field_edit["line_edit" + str(row)].text()
                )
                if tableField is None:
                    tableField = self.line_edit_create_table.text()
                item = (
                    tableField
                    + "("
                    + self.table_field_edit["line_edit" + str(row)].text()
                    + ")"
                )
                self.references_combo3.addItem(item)
            self.references_combo3.currentIndexChanged.connect(
                self.get_references_combo3
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_references_combo3")
        try:
            items = ConnectDb.get_all_references(self)
            for item in items:
                self.references_combo3.addItem(item)
            self.references_combo3.currentIndexChanged.connect(
                self.get_references_combo3
            )
        except (AttributeError, TypeError) as e:
            print(f"{e} :create_references_combo3")
        self.table_foreign_key.setCellWidget(2, 3, self.references_combo3)

    def get_references_combo3(self):
        current_text = self.references_combo3.currentText()
        if current_text != "Select field":
            self.references_combo3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.table_foreign_key.setCellWidget(2, 5, self.foreigntkey_label)
            self.table_foreign_key.removeCellWidget(1, 4)
            self.create_foreignkey_label()
            self.table_foreign_key.setCellWidget(2, 4, self.foreigntkey_label)
        else:
            self.table_foreign_key.removeCellWidget(2, 4)
            self.create_foreignkey_label()
            self.table_foreign_key.setCellWidget(1, 4, self.foreigntkey_label)
            self.references_combo3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_foreignkey_label(self):
        self.foreigntkey_label = QLabel(")")
        self.foreigntkey_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.foreigntkey_label.setStyleSheet("QLabel { color: green; }")
