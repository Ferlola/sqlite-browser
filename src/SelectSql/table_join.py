from PyQt6.QtWidgets import QTableWidget, QComboBox, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableJoin(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_join()

    def create_table_join(self):
        self.table_join = QTableWidget(1, 7)
        self.table_join.setMaximumHeight(30)
        self.table_join.setColumnWidth(0, 150)
        self.table_join.horizontalHeader().setVisible(False)
        self.table_join.verticalHeader().setVisible(False)
        self.row_join = self.table_join.rowCount()
        self.create_combo_join()

    def create_combo_join(self):
        items = ["Select JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"]
        self.combo_join = QComboBox()
        self.combo_join.addItems(items)
        self.table_join.setCellWidget(0, 0, self.combo_join)
        self.combo_join.currentIndexChanged.connect(self.get_combo_join)

    def get_combo_join(self):
        current_text = self.combo_join.currentText()
        if current_text != "Select JOIN":
            self.combo_join.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            self.create_combobox_join_tables1()
            if self.row_join > 1:
                self.table_join.removeRow(self.row_join - 1)
                self.table_join.setMaximumHeight(30)
        else:
            self.table_join.setMaximumHeight(30)
            self.table_join.removeRow(self.row_join)
            self.combo_join.setStyleSheet("QComboBox{{ color: {} }}".format("black"))
            self.table_join.removeCellWidget(0, 1)
            self.table_join.removeCellWidget(0, 2)
            self.table_join.removeCellWidget(0, 3)
            self.table_join.removeCellWidget(0, 4)
            self.table_join.removeCellWidget(0, 5)
            self.table_join.removeCellWidget(0, 6)

    def create_combobox_join_tables1(self):
        self.combo_join_tables1 = QComboBox()
        self.combo_join_tables1.addItem("Select table")
        self.combo_join_tables1.addItems(ConnectDb.get_all_tables(self))
        self.table_join.setColumnWidth(0, 120)
        self.table_join.setCellWidget(0, 1, self.combo_join_tables1)
        self.combo_join_tables1.currentIndexChanged.connect(self.get_combo_join_tables1)

    def get_combo_join_tables1(self):
        current_text = self.combo_join_tables1.currentText()
        if current_text != "Select table":
            self.combo_join_tables1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_label_on()
            self.create_combobox_join_tables2()
        else:
            self.table_join.removeCellWidget(0, 2)
            self.table_join.removeCellWidget(0, 3)
            self.table_join.removeCellWidget(0, 4)
            self.table_join.removeCellWidget(0, 5)
            self.table_join.removeCellWidget(0, 6)
            self.combo_join_tables1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_label_on(self):
        self.label_on = QLabel("ON")
        self.label_on.setStyleSheet(
            "background-color: white; color: green; border:1px solid silver;"
        )
        self.label_on.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_join.setColumnWidth(2, 50)
        self.table_join.setCellWidget(0, 2, self.label_on)

    def create_combobox_join_tables2(self):
        self.combo_join_tables2 = QComboBox()
        self.combo_join_tables2.addItem("Select table")
        self.combo_join_tables2.addItems(ConnectDb.get_all_tables(self))
        self.table_join.setColumnWidth(3, 120)
        self.table_join.setCellWidget(0, 3, self.combo_join_tables2)
        self.combo_join_tables2.currentIndexChanged.connect(self.get_combo_join_tables2)

    def get_combo_join_tables2(self):
        current_text = self.combo_join_tables2.currentText()
        if current_text != "Select table":
            self.combo_join_tables2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_combobox_join_fields1()
        else:
            self.combo_join_tables2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_join.removeCellWidget(0, 4)
            self.table_join.removeCellWidget(0, 5)
            self.table_join.removeCellWidget(0, 6)

    def create_combobox_join_fields1(self):
        self.combobox_join_fields1 = QComboBox()
        self.combobox_join_fields1.addItem("Select field")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_tables)
        for item in items:
            item = "." + item + " = "
            self.combobox_join_fields1.addItem(item)
        current_text = self.combo_join_tables1.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        for item in items:
            item = "." + item + " = "
            self.combobox_join_fields1.addItem(item)
        self.table_join.setColumnWidth(4, 120)
        self.table_join.setCellWidget(0, 4, self.combobox_join_fields1)
        self.combobox_join_fields1.currentIndexChanged.connect(
            self.get_combobox_join_fields1
        )

    def get_combobox_join_fields1(self):
        current_text = self.combobox_join_fields1.currentText()
        if current_text != "Select field":
            self.create_combobox_join_tables3()
            self.combobox_join_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combobox_join_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_join.removeCellWidget(0, 5)
            self.table_join.removeCellWidget(0, 6)

    def create_combobox_join_tables3(self):
        self.combo_join_tables3 = QComboBox()
        self.combo_join_tables3.addItem("Select table")
        self.combo_join_tables3.addItems(ConnectDb.get_all_tables(self))
        self.table_join.setColumnWidth(5, 120)
        self.table_join.setCellWidget(0, 5, self.combo_join_tables3)
        self.combo_join_tables3.currentIndexChanged.connect(self.get_combo_join_tables3)

    def get_combo_join_tables3(self):
        current_text = self.combo_join_tables3.currentText()
        if current_text != "Select table":
            self.combo_join_tables3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_combobox_join_fields2()
        else:
            self.combo_join_tables3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_join.removeCellWidget(0, 6)

    def create_combobox_join_fields2(self):
        self.combobox_join_fields2 = QComboBox()
        self.combobox_join_fields2.addItem("Select field")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_tables)
        for item in items:
            item = "." + item
            self.combobox_join_fields2.addItem(item)
        current_text = self.combo_join_tables1.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        for item in items:
            item = "." + item
            self.combobox_join_fields2.addItem(item)
        self.table_join.setColumnWidth(6, 120)
        self.table_join.setCellWidget(0, 6, self.combobox_join_fields2)
        self.combobox_join_fields2.currentIndexChanged.connect(
            self.get_combobox_join_fields2
        )

    def get_combobox_join_fields2(self):
        current_text = self.combobox_join_fields2.currentText()
        if current_text != "Select field":
            self.combobox_join_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            currentTextcomboJoin = self.combo_join.currentText()
            if currentTextcomboJoin == "INNER JOIN":
                self.table_join.setMaximumHeight(63)
                self.table_join.insertRow(self.row_join)
                self.create_label_inner_join()
                self.create_combobox_join_tables4()
            else:
                if self.row_join > 1:
                    self.table_join.removeRow(self.row_join - 1)
                    self.table_join.setMaximumHeight(30)
        else:
            if self.row_join > 1:
                self.table_join.removeRow(self.row_join - 1)
                self.table_join.setMaximumHeight(30)
            self.combobox_join_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_label_inner_join(self):
        self.label_inner_join = QLabel("INNER JOIN")
        self.label_inner_join.setStyleSheet(
            "background-color: white; color: green; border:1px solid silver;"
        )
        self.table_join.setColumnWidth(0, 120)
        self.table_join.setCellWidget(1, 0, self.label_inner_join)

    def create_combobox_join_tables4(self):
        self.combobox_join_tables4 = QComboBox()
        self.combobox_join_tables4.addItem("Select table")
        self.combobox_join_tables4.addItems(ConnectDb.get_all_tables(self))
        self.table_join.setColumnWidth(1, 120)
        self.table_join.setCellWidget(1, 1, self.combobox_join_tables4)
        self.combobox_join_tables4.currentIndexChanged.connect(
            self.get_combo_join_tables4
        )

    def get_combo_join_tables4(self):
        current_text = self.combobox_join_tables4.currentText()
        if current_text != "Select table":
            self.combobox_join_tables4.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_label_on2()
            self.create_combobox_join_tables5()
        else:
            self.table_join.removeCellWidget(1, 2)
            self.table_join.removeCellWidget(1, 3)
            self.table_join.removeCellWidget(1, 4)
            self.table_join.removeCellWidget(1, 5)
            self.table_join.removeCellWidget(1, 6)
            self.combobox_join_tables4.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_label_on2(self):
        self.label_on2 = QLabel("ON")
        self.label_on2.setStyleSheet(
            "background-color: white; color: green; border:1px solid silver;"
        )
        self.label_on2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_join.setColumnWidth(2, 50)
        self.table_join.setCellWidget(1, 2, self.label_on2)

    def create_combobox_join_tables5(self):
        self.combobox_join_tables5 = QComboBox()
        self.combobox_join_tables5.addItem("Select table")
        self.combobox_join_tables5.addItems(ConnectDb.get_all_tables(self))
        self.table_join.setColumnWidth(3, 120)
        self.table_join.setCellWidget(1, 3, self.combobox_join_tables5)
        self.combobox_join_tables5.currentIndexChanged.connect(
            self.get_combo_join_tables5
        )

    def get_combo_join_tables5(self):
        current_text = self.combobox_join_tables5.currentText()
        if current_text != "Select table":
            self.combobox_join_tables5.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_combobox_join_fields3()
        else:
            self.combobox_join_tables5.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_join.removeCellWidget(1, 4)
            self.table_join.removeCellWidget(1, 5)
            self.table_join.removeCellWidget(1, 6)

    def create_combobox_join_fields3(self):
        self.combobox_join_fields3 = QComboBox()
        self.combobox_join_fields3.addItem("Select field")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_tables)
        for item in items:
            item = "." + item + " = "
            self.combobox_join_fields3.addItem(item)
        current_text = self.combobox_join_tables4.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        for item in items:
            item = "." + item + " = "
            self.combobox_join_fields3.addItem(item)
        self.table_join.setCellWidget(1, 4, self.combobox_join_fields3)
        self.combobox_join_fields3.currentIndexChanged.connect(
            self.get_combobox_join_fields3
        )

    def get_combobox_join_fields3(self):
        current_text = self.combobox_join_fields3.currentText()
        if current_text != "Select field":
            self.create_combobox_join_tables6()
            self.combobox_join_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combobox_join_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_join.removeCellWidget(1, 5)
            self.table_join.removeCellWidget(1, 6)

    def create_combobox_join_tables6(self):
        self.combobox_join_tables6 = QComboBox()
        self.combobox_join_tables6.addItem("Select table")
        self.combobox_join_tables6.addItems(ConnectDb.get_all_tables(self))
        self.table_join.setColumnWidth(5, 120)
        self.table_join.setCellWidget(1, 5, self.combobox_join_tables6)
        self.combobox_join_tables6.currentIndexChanged.connect(
            self.get_combo_join_tables6
        )

    def get_combo_join_tables6(self):
        current_text = self.combobox_join_tables6.currentText()
        if current_text != "Select table":
            self.combobox_join_tables6.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.create_combobox_join_fields4()
        else:
            self.combobox_join_tables6.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
            self.table_join.removeCellWidget(1, 6)

    def create_combobox_join_fields4(self):
        self.combobox_join_fields4 = QComboBox()
        self.combobox_join_fields4.addItem("Select field")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        items = ConnectDb.get_fields_table(self, current_text_tables)
        for item in items:
            item = "." + item
            self.combobox_join_fields4.addItem(item)
        current_text = self.combobox_join_tables6.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        for item in items:
            item = "." + item
            self.combobox_join_fields4.addItem(item)
        self.table_join.setColumnWidth(6, 120)
        self.table_join.setCellWidget(1, 6, self.combobox_join_fields4)
        self.combobox_join_fields4.currentIndexChanged.connect(
            self.get_combobox_join_fields4
        )

    def get_combobox_join_fields4(self):
        current_text = self.combobox_join_fields4.currentText()
        if current_text != "Select field":
            self.combobox_join_fields4.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combobox_join_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )
