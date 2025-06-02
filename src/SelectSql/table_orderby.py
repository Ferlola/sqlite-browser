from PyQt6.QtWidgets import QTableWidget, QComboBox, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableOrderBy(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_orderby()

    def create_table_orderby(self):
        self.table_order_by = QTableWidget(1, 5)
        self.table_order_by.setMaximumHeight(30)
        self.table_order_by.setColumnWidth(0, 150)
        self.table_order_by.setColumnWidth(1, 200)
        self.table_order_by.setColumnWidth(2, 100)
        self.table_order_by.setColumnWidth(3, 200)
        self.table_order_by.setColumnWidth(4, 100)
        self.table_order_by.horizontalHeader().setVisible(False)
        self.table_order_by.verticalHeader().setVisible(False)
        self.create_combo_orderby1()

    def create_combo_orderby1(self):
        self.combo_order_by1 = QComboBox()
        self.combo_order_by1.addItem("ORDER BY?")
        self.combo_order_by1.addItem("ORDER BY")
        self.combo_order_by1.addItem("ORDER BY (CASE")
        self.combo_order_by1.addItem("ORDER BY COUNT")
        self.table_order_by.setCellWidget(0, 0, self.combo_order_by1)
        self.combo_order_by1.currentIndexChanged.connect(self.get_combo_orderby1)

    def get_combo_orderby1(self):
        current_text = self.combo_order_by1.currentText()
        if current_text != "ORDER BY?":
            self.combo_order_by1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "ORDER BY (CASE":
                self.table_order_by.removeCellWidget(0, 1)
                self.table_order_by.removeCellWidget(0, 2)
                self.table_order_by.removeCellWidget(0, 3)
                self.table_order_by.removeCellWidget(0, 4)
                self.create_combo_having_case_fields1()
            elif current_text == "ORDER BY COUNT":
                self.table_order_by.removeCellWidget(0, 1)
                self.table_order_by.removeCellWidget(0, 2)
                self.table_order_by.removeCellWidget(0, 3)
                self.table_order_by.removeCellWidget(0, 4)
                self.create_combo_orderby_avg()
            else:
                self.table_order_by.removeCellWidget(0, 1)
                self.table_order_by.removeCellWidget(0, 2)
                self.table_order_by.removeCellWidget(0, 3)
                self.create_combo_orderby2()
                self.create_combo_asc1()
                self.create_combo_orderby3()
                self.create_combo_asc2()
        else:
            self.table_order_by.removeCellWidget(0, 1)
            self.table_order_by.removeCellWidget(0, 2)
            self.table_order_by.removeCellWidget(0, 3)
            self.table_order_by.removeCellWidget(0, 4)
            self.combo_order_by1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_orderby2(self):
        self.combo_order_by2 = QComboBox()
        current_table = self.combo_tables.currentText()
        current_table = current_table.replace("FROM ", "")
        fields = ConnectDb.get_fields_table_by(self, current_table)
        self.combo_order_by2.addItem("Select field")
        self.combo_order_by2.addItems(fields)
        try:
            current_text = self.combo_join_tables1.currentText()
            fields = ConnectDb.get_fields_table_by(self, current_text)
            self.combo_order_by2.addItems(fields)
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combo_orderby2")
        self.table_order_by.setCellWidget(0, 1, self.combo_order_by2)
        self.combo_order_by2.currentIndexChanged.connect(self.get_combo_order_by2)

    def get_combo_order_by2(self):
        current_text = self.combo_order_by2.currentText()
        if current_text != "Select field":
            self.combo_order_by2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_order_by2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_asc1(self):
        self.combo_asc1 = QComboBox()
        self.combo_asc1.addItem("ASC/DESC")
        self.combo_asc1.addItems(["ASC", "DESC"])
        self.combo_asc1.currentIndexChanged.connect(self.get_combo_asc1)
        self.table_order_by.setCellWidget(0, 2, self.combo_asc1)

    def get_combo_asc1(self):
        currentText1 = self.combo_asc1.currentText()
        if currentText1 != "ASC/DESC":
            self.combo_asc1.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.combo_asc1.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_orderby3(self):
        self.combo_order_by3 = QComboBox()
        self.combo_order_by3.addItem("Next Order by")
        current_table = self.combo_tables.currentText()
        current_table = current_table.replace("FROM ", "")
        for field in ConnectDb.get_fields_table_by(self, current_table):
            field = ", " + field
            self.combo_order_by3.addItem(field)
        try:
            current_text = self.combo_join_tables1.currentText()
            for field in ConnectDb.get_fields_table_by(self, current_text):
                field = ", " + field
                self.combo_order_by3.addItem(field)
        except AttributeError as e:
            print(f"{e} :create_combo_orderby3")
        self.table_order_by.setCellWidget(0, 3, self.combo_order_by3)
        self.combo_order_by3.currentIndexChanged.connect(self.get_combo_orderby3)

    def get_combo_orderby3(self):
        currentText2 = self.combo_order_by3.currentText()
        if currentText2 != "Next Order by":
            self.combo_order_by3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_order_by3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_asc2(self):
        self.combo_asc2 = QComboBox()
        self.combo_asc2.addItem("ASC/DESC")
        self.combo_asc2.addItems(["ASC", "DESC"])
        self.table_order_by.setCellWidget(0, 4, self.combo_asc2)
        self.combo_asc2.currentIndexChanged.connect(self.get_combo_asc2)

    def get_combo_asc2(self):
        currentText2 = self.combo_asc2.currentText()
        if currentText2 != "ASC/DESC":
            self.combo_asc2.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.combo_asc2.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_orderby_avg(self):
        currentTable = self.combo_tables.currentText()
        currentTable = currentTable.replace("FROM ", "")
        fields = ConnectDb.get_fields_table(self, currentTable)
        self.combo_order_by_avg = QComboBox()
        self.combo_order_by_avg.addItem("Select field")
        for field in fields:
            field = "(" + field + ")"
            self.combo_order_by_avg.addItem(field)
        self.combo_order_by_avg.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_order_by.setCellWidget(0, 1, self.combo_order_by_avg)
        self.create_combo_avg_asc()

    def create_combo_avg_asc(self):
        self.combo_avg_asc = QComboBox()
        self.combo_avg_asc.addItem("ASC/DESC")
        self.combo_avg_asc.addItems(["ASC", "DESC"])
        self.table_order_by.setCellWidget(0, 2, self.combo_avg_asc)
        self.combo_avg_asc.currentIndexChanged.connect(self.get_combo_avg_asc)

    def get_combo_avg_asc(self):
        current_text = self.combo_avg_asc.currentText()
        if current_text != "ASC/DESC":
            self.combo_avg_asc.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.combo_avg_asc.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_having_case_fields1(self):
        current_table = self.combo_tables.currentText()
        current_table = current_table.replace("FROM ", "")
        fields = ConnectDb.get_fields_table(self, current_table)
        self.combo_having_case_fields1 = QComboBox()
        self.combo_having_case_fields1.addItem("WHEN field")
        for item in fields:
            self.combo_having_case_fields1.addItem("WHEN " + item + " IS NULL ")
        self.table_order_by.setColumnWidth(1, 140)
        self.table_order_by.setCellWidget(0, 1, self.combo_having_case_fields1)
        self.combo_having_case_fields1.currentIndexChanged.connect(
            self.get_combo_having_case_fields1
        )

    def get_combo_having_case_fields1(self):
        current_text = self.combo_having_case_fields1.currentText()
        if current_text != "WHEN field":
            self.create_combo_having_case_fields2()
            self.combo_having_case_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_having_case_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_having_case_fields2(self):
        current_table = self.combo_tables.currentText()
        current_table = current_table.replace("FROM ", "")
        fields = ConnectDb.get_fields_table(self, current_table)
        self.combo_having_case_fields2 = QComboBox()
        self.combo_having_case_fields2.addItem("THEN field")
        for item in fields:
            self.combo_having_case_fields2.addItem("THEN " + item)
        self.table_order_by.setColumnWidth(2, 120)
        self.table_order_by.setCellWidget(0, 2, self.combo_having_case_fields2)
        self.combo_having_case_fields2.currentIndexChanged.connect(
            self.get_combo_having_case_fields2
        )

    def get_combo_having_case_fields2(self):
        current_text = self.combo_having_case_fields2.currentText()
        if current_text != "THEN field":
            self.create_label_having_case()
            self.combo_having_case_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_order_by.removeCellWidget(0, 3)
            self.combo_having_case_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_label_having_case(self):
        current_text = self.combo_having_case_fields1.currentText()
        current_field = current_text.replace("WHEN ", "")
        current_field = current_field.replace(" IS NULL ", "")
        self.label_having_case = QLabel("ELSE " + current_field + " END)")
        self.label_having_case.setStyleSheet("color:green;")
        self.label_having_case.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_order_by.setColumnWidth(3, 160)
        self.table_order_by.setCellWidget(0, 3, self.label_having_case)
