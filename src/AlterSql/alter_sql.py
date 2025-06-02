from PyQt6.QtWidgets import (
    QTableWidget,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt
import sqlite3
from src.AlterSql.table_alter import TableAlter
from src.UtilsSql.table_structure import TableStructure
from src.UtilsSql.messages import Messagebox


class Alter(QWidget, TableAlter, TableStructure):
    def __init__(self):
        super().__init__()
        self.qvbox_alter = QVBoxLayout()
        self.qvbox_alter.addWidget(self.table_alter)
        self.qvbox_alter.addWidget(self.table_structure)
        self.qvbox_alter.setContentsMargins(10, 10, 10, 10)
        self.qvbox_alter.addStretch()
        self.layout_label_alter = QVBoxLayout()
        self.qvbox_alter.addLayout(self.layout_label_alter)
        self.setLayout(self.qvbox_alter)
        self.create_table_label_alter()

    def create_table_label_alter(self):
        self.table_label_alter = QTableWidget(1, 1)
        self.table_label_alter.setMaximumHeight(30)
        self.table_label_alter.setColumnWidth(0, 970)
        self.table_label_alter.horizontalHeader().setVisible(False)
        self.table_label_alter.verticalHeader().setVisible(False)
        self.button_check_alter = QPushButton("Check alter table")
        self.button_check_alter.clicked.connect(self.check_data_alter)
        self.button_execute_alter = QPushButton("Execute alter table")
        self.button_execute_alter.clicked.connect(self.execute_alter)
        self.layout_button_alter = QHBoxLayout()
        self.layout_button_alter.addWidget(self.button_check_alter)
        self.layout_button_alter.addWidget(self.button_execute_alter)
        self.layout_label_alter.addWidget(self.table_label_alter)
        self.qvbox_alter.addLayout(self.layout_button_alter)

    def check_data_alter(self):
        self.current_text_alter = []
        self.current_text_alter.append("ALTER TABLE")
        try:
            self.current_text_alter.append(self.alter_table_combo.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_alter.append(self.alter_options_combo.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_alter.append(self.alter_add_line_edit.text())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_alter.append(self.alter_modify_column_combo.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_alter.append(self.alter_types_combo.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_alter.append(self.alter_drop_combo.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_alter.append(self.alter_rename_combo.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            if self.alter_to_line_edit.text():
                text = " TO " + self.alter_to_line_edit.text()
                self.current_text_alter.append(text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        self.process_current_alter()

    def process_current_alter(self):
        first_items = ["Select table", "Select field", "Select option"]
        lista_alter = []
        for e, text in enumerate(self.current_text_alter):
            if text in first_items:
                pass
            elif text is None:
                pass
            elif text == "":
                pass
            else:
                lista_alter.append(text)
        self.lista_alter = ""
        self.lista_alter = " ".join(lista_alter)
        self.label_alter_check = QLabel(self.lista_alter)
        self.label_alter_check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_alter_check.setStyleSheet("QLabel { color: green; }")
        self.table_label_alter.setCellWidget(0, 0, self.label_alter_check)

    def execute_alter(self):
        self.check_data_alter()
        print(self.lista_alter)
        try:
            with sqlite3.connect(self.filename) as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute(self.lista_alter)
                con.commit()
                message = Messagebox()
                message.question()
        except sqlite3.OperationalError as e:
            print(f"sqlite3.OperationalError {e} :execute_alter")
            message = Messagebox()
            message.critical(str(e))
