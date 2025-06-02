from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableHaving(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_having()

    def create_table_having(self):
        self.table_having = QTableWidget(1, 8)
        self.table_having.setMaximumHeight(30)
        self.table_having.setColumnWidth(0, 150)
        self.table_having.setColumnWidth(1, 150)
        self.table_having.setColumnWidth(2, 50)
        self.table_having.setColumnWidth(3, 50)
        self.table_having.setColumnWidth(4, 120)
        self.table_having.setColumnWidth(5, 150)
        self.table_having.setColumnWidth(6, 50)
        self.table_having.setColumnWidth(7, 50)
        self.table_having.horizontalHeader().setVisible(False)
        self.table_having.verticalHeader().setVisible(False)
        self.create_combo_having1()

    def create_combo_having1(self):
        self.combo_having1 = QComboBox()
        self.combo_having1.addItems(
            ["HAVING", "HAVING COUNT", "HAVING AVG", "HAVING SUM"]
        )
        self.combo_having1.currentIndexChanged.connect(self.get_combo_having1)
        self.table_having.setCellWidget(0, 0, self.combo_having1)

    def get_combo_having1(self):
        current_text = self.combo_having1.currentText()
        if current_text != "HAVING":
            self.combo_having1.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            self.create_combo_having1_fields()
            self.create_combo_having1_optrs1()
        else:
            self.table_having.removeCellWidget(0, 1)
            self.table_having.removeCellWidget(0, 2)
            self.table_having.removeCellWidget(0, 3)
            self.table_having.removeCellWidget(0, 4)
            self.table_having.removeCellWidget(0, 5)
            self.table_having.removeCellWidget(0, 6)
            self.table_having.removeCellWidget(0, 7)
            self.combo_having1.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_having1_fields(self):
        self.combo_having1_fields = QComboBox()
        self.combo_having1_fields.addItem("(*)")
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            self.combo_having1_fields.addItems(
                ConnectDb.get_list_all_pr(self, current_text_tables)
            )
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combo_having1_fields")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        self.combo_having1_fields.addItems(
            ConnectDb.get_list_all_pr(self, current_text_tables)
        )
        self.combo_having1_fields.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_having.setCellWidget(0, 1, self.combo_having1_fields)
        self.create_combo_having1_optrs1()

    def create_combo_having1_optrs1(self):
        self.combo_having1_optrs1 = QComboBox()
        self.combo_having1_optrs1.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>"]
        )
        self.combo_having1_optrs1.currentIndexChanged.connect(
            self.get_combo_having1_optrs1
        )
        self.table_having.setCellWidget(0, 2, self.combo_having1_optrs1)

    def get_combo_having1_optrs1(self):
        current_text = self.combo_having1_optrs1.currentText()
        if current_text != "Operator":
            self.create_lineedit_having1()
            self.combo_having1_optrs1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_having.removeCellWidget(0, 3)
            self.table_having.removeCellWidget(0, 4)
            self.table_having.removeCellWidget(0, 5)
            self.table_having.removeCellWidget(0, 6)
            self.table_having.removeCellWidget(0, 7)
            self.combo_having1_optrs1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_lineedit_having1(self):
        self.lineedit_having1 = QLineEdit()
        self.lineedit_having1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineedit_having1.textChanged.connect(self.changed_lineedit_having1)
        self.lineedit_having1.setStyleSheet(self.style_qLine)
        self.table_having.setCellWidget(0, 3, self.lineedit_having1)

    def changed_lineedit_having1(self):
        texto = self.lineedit_having1.text()
        if len(texto) is not None:
            self.lineedit_having1.setStyleSheet(self.style_qLine)
            self.table_having.removeCellWidget(0, 4)
            self.table_having.removeCellWidget(0, 5)
            self.table_having.removeCellWidget(0, 6)
            self.table_having.removeCellWidget(0, 7)
        if len(texto) > 0:
            self.create_combo_having2()
            self.lineedit_having1.setStyleSheet(self.style_qLine1)

    def create_combo_having2(self):
        self.combo_having2 = QComboBox()
        self.combo_having2.addItems(["AND?", "AND COUNT", "AND AVG", "AND SUM"])
        self.combo_having2.currentIndexChanged.connect(self.get_combo_having2)
        self.table_having.setCellWidget(0, 4, self.combo_having2)

    def get_combo_having2(self):
        current_text = self.combo_having2.currentText()
        if current_text != "AND?":
            self.combo_having2.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            self.create_combo_having2_fields()
            self.create_combo_having2_optrs2()
        else:
            self.table_having.removeCellWidget(0, 5)
            self.table_having.removeCellWidget(0, 6)
            self.table_having.removeCellWidget(0, 7)
            self.combo_having2.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_combo_having2_fields(self):
        self.combo_having2_fields = QComboBox()
        self.combo_having2_fields.addItem("(*)")
        try:
            current_text_tables = self.combo_join_tables1.currentText()
            self.combo_having2_fields.addItems(
                ConnectDb.get_list_all_pr(self, current_text_tables)
            )
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combo_having2_fields")
        current_text_tables = self.combo_tables.currentText()
        current_text_tables = current_text_tables.replace("FROM ", "")
        self.combo_having2_fields.addItems(
            ConnectDb.get_list_all_pr(self, current_text_tables)
        )
        self.combo_having2_fields.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_having.setCellWidget(0, 5, self.combo_having2_fields)
        self.create_combo_having2_optrs2()

    def create_combo_having2_optrs2(self):
        self.combo_having2_optrs2 = QComboBox()
        self.combo_having2_optrs2.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>"]
        )
        self.combo_having2_optrs2.currentIndexChanged.connect(
            self.get_combo_having2_optrs2
        )
        self.table_having.setCellWidget(0, 6, self.combo_having2_optrs2)

    def get_combo_having2_optrs2(self):
        current_text = self.combo_having2_optrs2.currentText()
        if current_text != "Operator":
            self.create_lineedit_having2()
            self.combo_having2_optrs2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_having.removeCellWidget(0, 7)
            self.combo_having2_optrs2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_lineedit_having2(self):
        self.lineedit_having2 = QLineEdit()
        self.lineedit_having2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineedit_having2.textChanged.connect(self.changed_lineedit_having2)
        self.lineedit_having2.setStyleSheet(self.style_qLine)
        self.table_having.setCellWidget(0, 7, self.lineedit_having2)

    def changed_lineedit_having2(self):
        texto = self.lineedit_having2.text()
        if len(texto) is not None:
            self.lineedit_having2.setStyleSheet(self.style_qLine)
        if len(texto) > 0:
            self.lineedit_having2.setStyleSheet(self.style_qLine1)
