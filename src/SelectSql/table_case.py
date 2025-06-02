from PyQt6.QtWidgets import QTableWidget, QComboBox, QCheckBox, QLabel, QLineEdit
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableCase(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_case()

    def create_table_case(self):
        self.table_case = QTableWidget(1, 6)
        self.table_case.setMaximumHeight(30)
        self.table_case.horizontalHeader().setVisible(False)
        self.table_case.verticalHeader().setVisible(False)
        self.row_case = self.table_case.rowCount()
        self.create_checkbox_case()

    def create_checkbox_case(self):
        self.checkbox_case = QCheckBox(text="CASE")
        self.checkbox_case.setTristate(False)
        self.checkbox_case.stateChanged.connect(self.on_state_changed_checkbox_case)
        self.table_case.setCellWidget(0, 0, self.checkbox_case)

    def on_state_changed_checkbox_case(self):
        state = self.checkbox_case.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_case.setStyleSheet("color : green")
            self.table_case.setMaximumHeight(62)
            self.table_case.setRowCount(1)
            self.table_case.insertRow(self.row_case)
            self.create_case_label_when1()
            self.create_combo_case_fields1()
        else:
            self.table_case.setRowCount(1)
            self.table_case.setMaximumHeight(30)
            self.checkbox_case.setStyleSheet("color : black")
            self.table_case.removeRow(self.row_case)

    def create_case_label_when1(self):
        self.case_label_when1 = QLabel("WHEN")
        self.case_label_when1.setStyleSheet("color:green;")
        self.case_label_when1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(1, 0, self.case_label_when1)

    def create_combo_case_fields1(self):
        fieldsCase = self.items_checked + self.items_checked2
        self.combo_case_fields1 = QComboBox()
        self.combo_case_fields1.addItem("Select field")
        self.combo_case_fields1.addItems(fieldsCase)
        self.combo_case_fields1.currentIndexChanged.connect(self.get_combo_case_fields1)
        self.table_case.setCellWidget(1, 1, self.combo_case_fields1)

    def get_combo_case_fields1(self):
        current_text = self.combo_case_fields1.currentText()
        if current_text != "Select field":
            self.create_case_combo_operator1()
            self.combo_case_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_case_fields1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_case_combo_operator1(self):
        self.combo_case_operator1 = QComboBox()
        self.combo_case_operator1.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>", "IS NULL"]
        )
        self.combo_case_operator1.currentIndexChanged.connect(
            self.get_case_combo_operator1
        )
        self.table_case.setCellWidget(1, 2, self.combo_case_operator1)

    def get_case_combo_operator1(self):
        current_text = self.combo_case_operator1.currentText()
        currentText1 = self.combo_case_fields1.currentText()
        if current_text != "Operator":
            self.combo_case_operator1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text != "IS NULL":
                table = ConnectDb.get_table_field(self, currentText1)
                table = "FROM " + table
                self.Casetable1 = ConnectDb.get_data_column(self, table, currentText1)
                self.create_combo_case_result_fields1()
                self.create_case_label_then1()
                self.create_case_lineedit1()
                self.create_case_combo_when_else1()
            else:
                self.table_case.removeCellWidget(1, 3)
                self.create_case_label_then1()
                self.create_case_lineedit1()
                self.create_case_combo_when_else1()
        else:
            self.combo_case_operator1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_case_result_fields1(self):
        self.combo_case_result_fields1 = QComboBox()
        self.combo_case_result_fields1.addItems(self.Casetable1)
        self.combo_case_result_fields1.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_case.setCellWidget(1, 3, self.combo_case_result_fields1)

    def create_case_label_then1(self):
        self.case_label_then1 = QLabel("THEN")
        self.case_label_then1.setStyleSheet("color:green;")
        self.case_label_then1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(1, 4, self.case_label_then1)

    def create_case_lineedit1(self):
        self.case_lineedit1 = QLineEdit()
        self.case_lineedit1.setStyleSheet(self.style_qLine)
        self.case_lineedit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_lineedit1.textChanged.connect(self.get_case_lineedit1)
        self.table_case.setCellWidget(1, 5, self.case_lineedit1)

    def get_case_lineedit1(self):
        current_text = self.case_lineedit1.text()
        if len(current_text) is not None:
            self.case_lineedit1.setStyleSheet(self.style_qLine)
            self.table_case.setMaximumHeight(62)
            self.table_case.setRowCount(2)
        if len(current_text) > 0:
            self.table_case.setMaximumHeight(93)
            self.table_case.setRowCount(3)
            self.create_case_combo_when_else1()
            self.case_lineedit1.setStyleSheet(self.style_qLine1)

    def create_case_combo_when_else1(self):
        self.case_ombo_else1 = QComboBox()
        self.case_ombo_else1.setEditable(True)
        self.case_ombo_else1.addItems(["WHEN/ELSE", "WHEN", "ELSE"])
        self.case_elselineedit = self.case_ombo_else1.lineEdit()
        self.case_elselineedit.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.case_elselineedit.setReadOnly(True)
        self.case_ombo_else1.currentIndexChanged.connect(self.get_case_combo_else1)
        self.table_case.setCellWidget(2, 0, self.case_ombo_else1)

    def get_case_combo_else1(self):
        current_text = self.case_ombo_else1.currentText()
        if current_text != "WHEN/ELSE":
            self.case_ombo_else1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "WHEN":
                self.table_case.removeCellWidget(2, 2)
                self.table_case.removeCellWidget(2, 3)
                self.table_case.removeCellWidget(2, 4)
                self.table_case.removeCellWidget(2, 5)
                self.table_case.setMaximumHeight(93)
                self.table_case.setRowCount(3)
                self.create_combo_case_fields2()
            else:
                self.table_case.removeCellWidget(2, 2)
                self.table_case.removeCellWidget(2, 3)
                self.table_case.removeCellWidget(2, 4)
                self.table_case.removeCellWidget(2, 5)
                self.table_case.setMaximumHeight(93)
                self.table_case.setRowCount(3)
                self.create_case_else_lineedit1()
        else:
            self.table_case.removeCellWidget(2, 1)
            self.table_case.removeCellWidget(2, 2)
            self.table_case.removeCellWidget(2, 3)
            self.table_case.removeCellWidget(2, 4)
            self.table_case.removeCellWidget(2, 5)
            self.table_case.setMaximumHeight(93)
            self.table_case.setRowCount(3)
            self.case_ombo_else1.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_case_else_lineedit1(self):
        self.case_else_lineedit1 = QLineEdit()
        self.case_else_lineedit1.setStyleSheet(self.style_qLine)
        self.case_else_lineedit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_else_lineedit1.textChanged.connect(self.get_case_else_lineedit1)
        self.table_case.setCellWidget(2, 1, self.case_else_lineedit1)

    def get_case_else_lineedit1(self):
        current_text = self.case_else_lineedit1.text()
        if len(current_text) is not None:
            self.case_else_lineedit1.setStyleSheet(self.style_qLine)
            self.table_case.removeCellWidget(2, 2)
            self.table_case.removeCellWidget(2, 3)
        if len(current_text) > 0:
            self.case_else_lineedit1.setStyleSheet(self.style_qLine1)
            self.create_case_label_end_as1()
            self.create_case_end_as_lineedit1()

    def create_case_label_end_as1(self):
        self.case_label_end_as1 = QLabel("END AS")
        self.case_label_end_as1.setStyleSheet("color:green;")
        self.case_label_end_as1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(2, 2, self.case_label_end_as1)

    def create_case_end_as_lineedit1(self):
        self.case_end_as_lineedit1 = QLineEdit()
        self.case_end_as_lineedit1.setStyleSheet(self.style_qLine)
        self.case_end_as_lineedit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_end_as_lineedit1.textChanged.connect(self.get_case_end_as_lineedit1)
        self.table_case.setCellWidget(2, 3, self.case_end_as_lineedit1)

    def get_case_end_as_lineedit1(self):
        current_text = self.case_end_as_lineedit1.text()
        if len(current_text) is not None:
            self.case_end_as_lineedit1.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.case_end_as_lineedit1.setStyleSheet(self.style_qLine1)

    def create_combo_case_fields2(self):
        fieldsCase = self.items_checked + self.items_checked2
        self.combo_case_fields2 = QComboBox()
        self.combo_case_fields2.addItem("Select field")
        self.combo_case_fields2.addItems(fieldsCase)
        self.combo_case_fields2.currentIndexChanged.connect(self.get_combo_case_fields2)
        self.table_case.setCellWidget(2, 1, self.combo_case_fields2)

    def get_combo_case_fields2(self):
        current_text = self.combo_case_fields2.currentText()
        if current_text != "Select field":
            self.create_case_combo_operator2()
            self.combo_case_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_case_fields2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_case_combo_operator2(self):
        self.combo_case_operator2 = QComboBox()
        self.combo_case_operator2.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>", "IS NULL"]
        )
        self.combo_case_operator2.currentIndexChanged.connect(
            self.get_case_combo_operator2
        )
        self.table_case.setCellWidget(2, 2, self.combo_case_operator2)

    def get_case_combo_operator2(self):
        current_text = self.combo_case_operator2.currentText()
        currentText2 = self.combo_case_fields2.currentText()
        if current_text != "Operator":
            self.combo_case_operator2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text != "IS NULL":
                table = ConnectDb.get_table_field(self, currentText2)
                table = "FROM " + table
                self.Casetable2 = ConnectDb.get_data_column(self, table, currentText2)
                self.create_combo_case_result_fields2()
                self.create_case_label_then2()
                self.create_case_lineedit2()
                self.create_case_combo_when_else2()
            else:
                self.table_case.removeCellWidget(2, 3)
                self.create_case_label_then2()
                self.create_case_lineedit2()
                self.create_case_combo_when_else2()
        else:
            self.combo_case_operator2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_case_result_fields2(self):
        self.combo_case_result_fields2 = QComboBox()
        self.combo_case_result_fields2.addItems(self.Casetable2)
        self.combo_case_result_fields2.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_case.setCellWidget(2, 3, self.combo_case_result_fields2)

    def create_case_label_then2(self):
        self.case_label_then2 = QLabel("THEN")
        self.case_label_then2.setStyleSheet("color:green;")
        self.case_label_then2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(2, 4, self.case_label_then2)

    def create_case_lineedit2(self):
        self.case_lineEdit2 = QLineEdit()
        self.case_lineEdit2.setStyleSheet(self.style_qLine)
        self.case_lineEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_lineEdit2.textChanged.connect(self.get_case_lineedit2)
        self.table_case.setCellWidget(2, 5, self.case_lineEdit2)

    def get_case_lineedit2(self):
        current_text = self.case_lineEdit2.text()
        if len(current_text) is not None:
            self.table_case.setMaximumHeight(93)
            self.table_case.setRowCount(3)
            self.case_lineEdit2.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.table_case.setMaximumHeight(124)
            self.table_case.setRowCount(4)
            self.create_case_combo_when_else2()
            self.case_lineEdit2.setStyleSheet(self.style_qLine1)

    def create_case_combo_when_else2(self):
        self.case_combo_else2 = QComboBox()
        self.case_combo_else2.setEditable(True)
        self.case_combo_else2.addItems(["WHEN/ELSE", "WHEN", "ELSE"])
        self.case_elselineedit2 = self.case_combo_else2.lineEdit()
        self.case_elselineedit2.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.case_elselineedit2.setReadOnly(True)
        self.case_combo_else2.currentIndexChanged.connect(self.get_case_combo_else2)
        self.table_case.setCellWidget(3, 0, self.case_combo_else2)

    def get_case_combo_else2(self):
        current_text = self.case_combo_else2.currentText()
        if current_text != "WHEN/ELSE":
            self.case_combo_else2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text == "WHEN":
                self.table_case.removeCellWidget(3, 2)
                self.table_case.removeCellWidget(3, 3)
                self.table_case.removeCellWidget(3, 4)
                self.table_case.removeCellWidget(3, 5)
                self.table_case.setMaximumHeight(124)
                self.table_case.setRowCount(4)
                self.create_combo_case_fields3()
            else:
                self.table_case.removeCellWidget(3, 2)
                self.table_case.removeCellWidget(3, 3)
                self.table_case.removeCellWidget(3, 4)
                self.table_case.removeCellWidget(3, 5)
                self.table_case.setMaximumHeight(124)
                self.table_case.setRowCount(4)
                self.create_case_else_lineedit2()
        else:
            self.table_case.removeCellWidget(3, 1)
            self.table_case.removeCellWidget(3, 2)
            self.table_case.removeCellWidget(3, 3)
            self.table_case.removeCellWidget(3, 4)
            self.table_case.removeCellWidget(3, 5)
            self.table_case.setMaximumHeight(124)
            self.table_case.setRowCount(4)
            self.case_combo_else2.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_case_else_lineedit2(self):
        self.case_else_lineedit2 = QLineEdit()
        self.case_else_lineedit2.setStyleSheet(self.style_qLine)
        self.case_else_lineedit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_else_lineedit2.textChanged.connect(self.get_case_else_lineedit2)
        self.table_case.setCellWidget(3, 1, self.case_else_lineedit2)

    def get_case_else_lineedit2(self):
        current_text = self.case_else_lineedit2.text()
        if len(current_text) is not None:
            self.case_else_lineedit2.setStyleSheet(self.style_qLine)
            self.table_case.removeCellWidget(3, 2)
            self.table_case.removeCellWidget(3, 3)
        if len(current_text) > 0:
            self.case_else_lineedit2.setStyleSheet(self.style_qLine1)
            self.create_case_label_end_as2()
            self.create_case_end_as_lineedit2()

    def create_case_label_end_as2(self):
        self.case_label_end_as2 = QLabel("END AS")
        self.case_label_end_as2.setStyleSheet("color:green;")
        self.case_label_end_as2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(3, 2, self.case_label_end_as2)

    def create_case_end_as_lineedit2(self):
        self.case_end_as_lineedit2 = QLineEdit()
        self.case_end_as_lineedit2.setStyleSheet(self.style_qLine)
        self.case_end_as_lineedit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_end_as_lineedit2.textChanged.connect(self.get_case_end_as_lineedit2)
        self.table_case.setCellWidget(3, 3, self.case_end_as_lineedit2)

    def get_case_end_as_lineedit2(self):
        current_text = self.case_end_as_lineedit2.text()
        if len(current_text) is not None:
            self.case_end_as_lineedit2.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.case_end_as_lineedit2.setStyleSheet(self.style_qLine1)

    def create_combo_case_fields3(self):
        fieldsCase = self.items_checked + self.items_checked2
        self.combo_case_fields3 = QComboBox()
        self.combo_case_fields3.addItem("Select field")
        self.combo_case_fields3.addItems(fieldsCase)
        self.combo_case_fields3.currentIndexChanged.connect(self.get_combo_case_fields3)
        self.table_case.setCellWidget(3, 1, self.combo_case_fields3)

    def get_combo_case_fields3(self):
        current_text = self.combo_case_fields3.currentText()
        if current_text != "Select field":
            self.create_case_combo_operator3()
            self.combo_case_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.combo_case_fields3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_case_combo_operator3(self):
        self.combo_case_operator3 = QComboBox()
        self.combo_case_operator3.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>", "IS NULL"]
        )
        self.combo_case_operator3.currentIndexChanged.connect(
            self.get_case_combo_operator3
        )
        self.table_case.setCellWidget(3, 2, self.combo_case_operator3)

    def get_case_combo_operator3(self):
        current_text = self.combo_case_operator3.currentText()
        current_text1 = self.combo_case_fields3.currentText()
        if current_text != "Operator":
            self.combo_case_operator3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            if current_text != "IS NULL":
                table = ConnectDb.get_table_field(self, current_text1)
                table = "FROM " + table
                self.Casetable3 = ConnectDb.get_data_column(self, table, current_text1)
                self.create_combo_case_result_fields3()
                self.create_case_label_then3()
                self.create_case_lineedit3()
            else:
                self.table_case.removeCellWidget(3, 3)
                self.create_case_label_then3()
                self.create_case_lineedit3()
                self.create_case_label_else()
        else:
            self.combo_case_operator3.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_combo_case_result_fields3(self):
        self.combo_case_result_fields3 = QComboBox()
        self.combo_case_result_fields3.addItems(self.Casetable3)
        self.combo_case_result_fields3.setStyleSheet(
            "QComboBox{{ color: {} }}".format("green")
        )
        self.table_case.setCellWidget(3, 3, self.combo_case_result_fields3)

    def create_case_label_then3(self):
        self.case_label_then3 = QLabel("THEN")
        self.case_label_then3.setStyleSheet("color:green;")
        self.case_label_then3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(3, 4, self.case_label_then3)

    def create_case_lineedit3(self):
        self.case_lineedit3 = QLineEdit()
        self.case_lineedit3.setStyleSheet(self.style_qLine)
        self.case_lineedit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_lineedit3.textChanged.connect(self.get_case_lineedit3)
        self.table_case.setCellWidget(3, 5, self.case_lineedit3)

    def get_case_lineedit3(self):
        current_text = self.case_lineedit3.text()
        if len(current_text) is not None:
            self.table_case.setMaximumHeight(123)
            self.table_case.setRowCount(4)
            self.case_lineedit3.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.table_case.setMaximumHeight(154)
            self.table_case.setRowCount(5)
            self.create_case_label_else()
            self.create_case_else_lineedit3()
            self.case_lineedit3.setStyleSheet(self.style_qLine1)

    def create_case_label_else(self):
        self.case_label_else = QLabel("ELSE")
        self.case_label_else.setStyleSheet("color:green;")
        self.case_label_else.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(4, 0, self.case_label_else)

    def create_case_else_lineedit3(self):
        self.case_else_lineedit3 = QLineEdit()
        self.case_else_lineedit3.setStyleSheet(self.style_qLine)
        self.case_else_lineedit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_else_lineedit3.textChanged.connect(self.get_case_else_lineedit3)
        self.table_case.setCellWidget(4, 1, self.case_else_lineedit3)

    def get_case_else_lineedit3(self):
        current_text = self.case_else_lineedit3.text()
        if len(current_text) is not None:
            self.case_else_lineedit3.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.case_else_lineedit3.setStyleSheet(self.style_qLine1)
            self.create_case_label_end_as()
            self.create_case_end_as_lineedit3()

    def create_case_label_end_as(self):
        self.case_label_end_as = QLabel("END AS")
        self.case_label_end_as.setStyleSheet("color:green;")
        self.case_label_end_as.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_case.setCellWidget(4, 2, self.case_label_end_as)

    def create_case_end_as_lineedit3(self):
        self.case_end_as_lineedit3 = QLineEdit()
        self.case_end_as_lineedit3.setStyleSheet(self.style_qLine)
        self.case_end_as_lineedit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.case_end_as_lineedit3.textChanged.connect(self.get_case_end_as_lineedit)
        self.table_case.setCellWidget(4, 3, self.case_end_as_lineedit3)

    def get_case_end_as_lineedit(self):
        current_text = self.case_end_as_lineedit3.text()
        if len(current_text) is not None:
            self.case_end_as_lineedit3.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.case_end_as_lineedit3.setStyleSheet(self.style_qLine1)
