from PyQt6.QtWidgets import QTableWidget, QComboBox, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableAlter(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_alter()

    def create_table_alter(self):
        self.table_alter = QTableWidget(2, 7)
        self.table_alter.setMaximumHeight(63)
        self.table_alter.setColumnWidth(0, 150)
        self.table_alter.setColumnWidth(1, 120)
        self.table_alter.horizontalHeader().setVisible(False)
        self.table_alter.verticalHeader().setVisible(False)
        self.create_alter_table_label()
        self.create_alter_table_combo_tables()

    def create_alter_table_label(self):
        self.alter_table_label = QLabel("ALTER TABLE")
        self.alter_table_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alter_table_label.setStyleSheet("color: green")
        self.table_alter.setCellWidget(0, 0, self.alter_table_label)

    def create_alter_table_combo_tables(self):
        self.alter_table_combo = QComboBox()
        self.alter_table_combo.addItem("Select table")
        self.alter_table_combo.addItems(ConnectDb.get_all_tables(self))
        self.table_alter.setCellWidget(0, 1, self.alter_table_combo)
        self.alter_table_combo.currentIndexChanged.connect(self.get_alter_table_combo)

    def get_alter_table_combo(self):
        current_text = self.alter_table_combo.currentText()
        if current_text != "Select table":
            self.structure = ConnectDb.get_structure(self, current_text)
            self.create_label_structure()
            self.create_alter_table_options_combo()
            self.alter_table_combo.setStyleSheet("QComboBox { color: green; }")
        else:
            self.table_alter.removeCellWidget(1, 0)
            self.table_alter.removeCellWidget(1, 1)
            self.table_alter.removeCellWidget(1, 2)
            self.table_alter.removeCellWidget(1, 3)
            self.table_alter.removeCellWidget(1, 4)
            self.table_alter.removeCellWidget(1, 5)
            self.table_alter.removeCellWidget(1, 6)
            self.alter_table_combo.setStyleSheet("QComboBox { color: black; }")

    def create_alter_table_options_combo(self):
        self.alter_options_combo = QComboBox()
        self.alter_options_combo.addItems(
            ["Select option", "ADD", "DROP COLUMN", "RENAME COLUMN"]
        )
        self.alter_options_combo.setEditable(True)
        line_edit = self.alter_options_combo.lineEdit()
        line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_alter.setCellWidget(1, 0, self.alter_options_combo)
        self.alter_options_combo.currentIndexChanged.connect(
            self.get_alter_options_combo
        )

    def get_alter_options_combo(self):
        current_text = self.alter_options_combo.currentText()
        if current_text != "Select option":
            self.alter_options_combo.setStyleSheet("QComboBox { color: green; }")
            if current_text == "ADD":
                self.table_alter.removeCellWidget(1, 2)
                self.table_alter.removeCellWidget(1, 3)
                self.table_alter.removeCellWidget(1, 4)
                self.table_alter.removeCellWidget(1, 5)
                self.table_alter.removeCellWidget(1, 6)
                self.create_alter_add_lineedit()
            elif current_text == "DROP COLUMN":
                self.table_alter.removeCellWidget(1, 2)
                self.table_alter.removeCellWidget(1, 3)
                self.table_alter.removeCellWidget(1, 4)
                self.table_alter.removeCellWidget(1, 5)
                self.table_alter.removeCellWidget(1, 6)
                self.create_alter_drop_combo()
            else:
                self.table_alter.removeCellWidget(1, 2)
                self.table_alter.removeCellWidget(1, 3)
                self.table_alter.removeCellWidget(1, 4)
                self.table_alter.removeCellWidget(1, 5)
                self.table_alter.removeCellWidget(1, 6)
                self.create_alter_rename_combo()
        else:
            self.table_alter.removeCellWidget(1, 1)
            self.table_alter.removeCellWidget(1, 2)
            self.table_alter.removeCellWidget(1, 3)
            self.table_alter.removeCellWidget(1, 4)
            self.table_alter.removeCellWidget(1, 5)
            self.table_alter.removeCellWidget(1, 6)
            self.alter_options_combo.setStyleSheet("QComboBox { color: black; }")

    def create_alter_add_lineedit(self):
        self.alter_add_line_edit = QLineEdit()
        self.alter_add_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alter_add_line_edit.setStyleSheet(self.style_qLine)
        self.alter_add_line_edit.textChanged.connect(self.get_alter_add_lineedit)
        self.table_alter.setCellWidget(1, 1, self.alter_add_line_edit)

    def get_alter_add_lineedit(self):
        if len(self.alter_add_line_edit.text()) is not None:
            self.alter_add_line_edit.setStyleSheet(self.style_qLine)
            self.table_alter.removeCellWidget(1, 2)
            self.table_alter.removeCellWidget(1, 3)
            self.table_alter.removeCellWidget(1, 4)
            self.table_alter.removeCellWidget(1, 5)
            self.table_alter.removeCellWidget(1, 6)
        if len(self.alter_add_line_edit.text()) > 0:
            self.alter_add_line_edit.setStyleSheet(self.style_qLine1)
            self.create_alter_types_combo()

    def create_alter_types_combo(self):
        self.alter_types_combo = QComboBox()
        self.alter_types_combo.addItems(
            ["Select option", "INTEGER", "TEXT", "NUMERIC", "DATE", "DATETIME"]
        )
        self.alter_types_combo.currentIndexChanged.connect(self.get_alter_type_combo)
        self.table_alter.setCellWidget(1, 2, self.alter_types_combo)

    def get_alter_type_combo(self):
        current_text = self.alter_types_combo.currentText()
        if current_text != "Select option":
            self.alter_types_combo.setStyleSheet("QComboBox { color: green; }")
        else:
            self.alter_types_combo.setStyleSheet("QComboBox { color: black; }")

    def create_alter_drop_combo(self):
        self.alter_drop_combo = QComboBox()
        current_text = self.alter_table_combo.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        self.alter_drop_combo.addItem("Select field")
        self.alter_drop_combo.addItems(items)
        self.table_alter.setCellWidget(1, 1, self.alter_drop_combo)
        self.alter_drop_combo.currentIndexChanged.connect(self.get_alter_drop_combo)

    def get_alter_drop_combo(self):
        current_text = self.alter_drop_combo.currentText()
        if current_text != "Select table":
            self.alter_drop_combo.setStyleSheet("QComboBox { color: green; }")
        else:
            self.alter_drop_combo.setStyleSheet("QComboBox { color: black; }")

    def create_alter_rename_combo(self):
        current_text = self.alter_table_combo.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        self.alter_rename_combo = QComboBox()
        self.alter_rename_combo.addItem("Select field")
        self.alter_rename_combo.addItems(items)
        self.table_alter.setCellWidget(1, 1, self.alter_rename_combo)
        self.alter_rename_combo.currentIndexChanged.connect(self.get_alter_rename_combo)

    def get_alter_rename_combo(self):
        current_text = self.alter_rename_combo.currentText()
        if current_text != "Select table":
            self.create_alter_to_label()
            self.create_alter_to_lineedit()
            self.alter_rename_combo.setStyleSheet("QComboBox { color: green; }")
        else:
            self.table_alter.removeCellWidget(1, 2)
            self.alter_rename_combo.setStyleSheet("QComboBox { color: black; }")

    def create_alter_to_label(self):
        self.alter_to_label = QLabel("TO")
        self.alter_to_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alter_to_label.setStyleSheet("color: green")
        self.table_alter.setCellWidget(1, 2, self.alter_to_label)

    def create_alter_to_lineedit(self):
        self.alter_to_line_edit = QLineEdit()
        self.alter_to_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.alter_to_line_edit.setStyleSheet(self.style_qLine)
        self.alter_to_line_edit.textChanged.connect(self.get_alter_to_lineedit)
        self.table_alter.setCellWidget(1, 3, self.alter_to_line_edit)

    def get_alter_to_lineedit(self):
        if len(self.alter_to_line_edit.text()) is not None:
            self.alter_to_line_edit.setStyleSheet(self.style_qLine)
        if len(self.alter_to_line_edit.text()) > 0:
            self.alter_to_line_edit.setStyleSheet(self.style_qLine1)

    def create_alter_modify_column_combo(self):
        current_text = self.alter_table_combo.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        self.alter_modify_column_combo = QComboBox()
        self.alter_modify_column_combo.addItem("Select field")
        self.alter_modify_column_combo.addItems(items)
        self.alter_modify_column_combo.currentIndexChanged.connect(
            self.get_alter_modify_column_combo
        )
        self.table_alter.setCellWidget(1, 1, self.alter_modify_column_combo)

    def get_alter_modify_column_combo(self):
        current_text = self.alter_modify_column_combo.currentText()
        if current_text != "Select field":
            self.create_alter_types_combo()
            self.alter_modify_column_combo.setStyleSheet("QComboBox { color: green; }")
        else:
            self.table_alter.removeCellWidget(1, 2)
            self.table_alter.removeCellWidget(1, 3)
            self.table_alter.removeCellWidget(1, 4)
            self.table_alter.removeCellWidget(1, 5)
            self.table_alter.removeCellWidget(1, 6)
            self.alter_modify_column_combo.setStyleSheet("QComboBox { color: black; }")
