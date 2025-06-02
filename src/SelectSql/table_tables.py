from PyQt6.QtWidgets import QTableWidget, QComboBox, QLabel, QCheckBox, QLineEdit
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableTables(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_tables()

    def create_table_tables(self):
        self.table_tables = QTableWidget(1, 5)
        self.table_tables.setMaximumHeight(30)
        self.table_tables.setColumnWidth(0, 150)
        self.table_tables.setColumnWidth(1, 50)
        self.table_tables.setColumnWidth(2, 120)
        self.table_tables.setColumnWidth(3, 80)
        self.table_tables.setColumnWidth(4, 50)
        self.table_tables.horizontalHeader().setVisible(False)
        self.table_tables.verticalHeader().setVisible(False)
        self.create_combobox_tables()

    def create_combobox_tables(self):
        self.combo_tables = QComboBox()
        self.combo_tables.addItem("FROM table")
        for table in ConnectDb.get_all_tables(self):
            self.combo_tables.addItem("FROM " + table)
        self.table_tables.setCellWidget(0, 0, self.combo_tables)
        self.combo_tables.currentIndexChanged.connect(self.get_combo_tables)

    def get_combo_tables(self):
        current_text_tables = self.combo_tables.currentText()
        current_text_select_option = self.combobox_select_options.currentText()
        if current_text_tables != "FROM table":
            if current_text_select_option == "SELECT ALL":
                self.table_join.hide()
            else:
                self.table_join.show()
            self.table_where.show()
            self.table_and.show()
            self.table_and_or.show()
            self.table_group_by.show()
            self.table_having.show()
            self.table_union.show()
            self.table_order_by.show()
            self.create_checkbox_tables_coma()
            self.create_limit_label()
            self.create_limit_lineedit()
            self.combo_tables.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.table_join.hide()
            self.table_where.hide()
            self.table_and.hide()
            self.table_and_or.hide()
            self.table_group_by.hide()
            self.table_having.hide()
            self.table_union.hide()
            self.table_order_by.hide()
            self.table_tables.removeCellWidget(0, 1)
            self.table_tables.removeCellWidget(0, 2)
            self.table_tables.removeCellWidget(0, 3)
            self.table_tables.removeCellWidget(0, 4)
            self.combo_tables.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_checkbox_tables_coma(self):
        self.checkbox_tables_coma = QCheckBox(text=",")
        self.checkbox_tables_coma.setTristate(False)
        self.checkbox_tables_coma.stateChanged.connect(
            self.on_state_changed_checkbox_tables_coma
        )
        self.table_tables.setCellWidget(0, 1, self.checkbox_tables_coma)

    def on_state_changed_checkbox_tables_coma(self):
        state = self.checkbox_tables_coma.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_tables_coma.setStyleSheet("color: green")
            self.create_combobox_tables2()
        else:
            self.table_tables.removeCellWidget(0, 2)
            self.checkbox_tables_coma.setStyleSheet("color: black")

    def create_combobox_tables2(self):
        self.combo_tables2 = QComboBox()
        self.combo_tables2.addItem("Select table")
        self.combo_tables2.addItems(ConnectDb.get_all_tables(self))
        self.table_tables.setCellWidget(0, 2, self.combo_tables2)
        self.combo_tables2.currentIndexChanged.connect(self.get_combo_tables2)

    def get_combo_tables2(self):
        current_text = self.combo_tables2.currentText()
        if current_text != "Select table":
            self.combo_tables2.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
        else:
            self.table_tables.removeCellWidget(0, 4)
            self.combo_tables2.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_limit_label(self):
        self.limit_label = QLabel("LIMIT")
        self.limit_label.setStyleSheet("color:black;")
        self.limit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_tables.setCellWidget(0, 3, self.limit_label)

    def create_limit_lineedit(self):
        self.limit_lineedit = QLineEdit()
        self.limit_lineedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.limit_lineedit.setStyleSheet(self.style_qLine)
        self.limit_lineedit.textChanged.connect(self.get_limit_lineedit)
        self.table_tables.setCellWidget(0, 4, self.limit_lineedit)

    def get_limit_lineedit(self):
        current_text = self.limit_lineedit.text()
        if len(current_text) is not None:
            self.limit_label.setStyleSheet("color:black;")
            self.limit_lineedit.setStyleSheet(self.style_qLine)
        if len(current_text) > 0:
            self.limit_label.setStyleSheet("color:green;")
            self.limit_lineedit.setStyleSheet(self.style_qLine1)
