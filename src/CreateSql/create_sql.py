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
from src.CreateSql.table_create_table import TableCreateTable
from src.UtilsSql.table_foreignkey import TableForeignKey
from src.UtilsSql.connect_db import ConnectDb
from src.UtilsSql.messages import Messagebox


class Create(QWidget, TableCreateTable, TableForeignKey):
    def __init__(self):
        super().__init__()
        self.qvbox_create = QVBoxLayout()
        self.qvbox_create.addLayout(self.main_layout_create)
        if ConnectDb.get_table_len(self) != 0:
            self.table_layout.addWidget(self.table_foreign_key)
        self.qvbox_create.setContentsMargins(10, 10, 10, 10)
        self.qvbox_create.addStretch()
        self.layout_label_create = QVBoxLayout()
        self.qvbox_create.addLayout(self.layout_label_create)
        self.setLayout(self.qvbox_create)
        self.create_table_label_create()

    def create_table_label_create(self):
        self.table_label_create = QTableWidget(1, 1)
        self.table_label_create.setMaximumHeight(30)
        self.table_label_create.setColumnWidth(0, 910)
        self.table_label_create.horizontalHeader().setVisible(False)
        self.table_label_create.verticalHeader().setVisible(False)
        self.button_check_create = QPushButton("Check create table")
        self.button_check_create.clicked.connect(self.check_data_create)
        self.button_execute_create = QPushButton("Execute create table")
        self.button_execute_create.clicked.connect(self.execute_create)
        self.layout_button_create = QHBoxLayout()
        self.layout_button_create.addWidget(self.button_check_create)
        self.layout_button_create.addWidget(self.button_execute_create)
        self.layout_label_create.addWidget(self.table_label_create)
        self.qvbox_create.addLayout(self.layout_button_create)

    def check_data_create(self):
        self.current_text_create = []
        try:
            self.current_text_create.append("CREATE TABLE IF NOT EXISTS")
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_create.append(self.line_edit_create_table.text())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_create.append("(")
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            for row, field in enumerate(self.table_field_edit):
                largo = len(self.table_field_edit)
                largo = largo - 2
                self.current_text_create.append(
                    self.table_field_edit["line_edit" + str(row)].text()
                )
                self.current_text_create.append(
                    self.table_field_combo["Combo" + str(row)].currentText()
                )
                state = self.table_field_checkbox_nn["Check" + str(row)].checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_create.append("NOT NULL")
                state = self.table_field_checkbox_pk["Check" + str(row)].checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_create.append("PRIMARY KEY")
                state = self.table_field_checkbox_ai["Check" + str(row)].checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_create.append("AUTOINCREMENT")
                state = self.table_field_checkbox_u["Check" + str(row)].checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_create.append("UNIQUE")
                if largo > row:
                    self.current_text_create.append(",")
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            current_text = self.foreignkey_combo_fields1.currentText()
            if current_text != "Select field":
                current_text = (
                    ",FOREIGN KEY" + self.foreignkey_combo_fields1.currentText()
                )
                self.current_text_create.append(current_text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            current_text = self.references_combo1.currentText()
            if current_text != "Select field":
                current_text = "REFERENCES " + self.references_combo1.currentText()
                self.current_text_create.append(current_text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            current_text = self.foreignkey_combo_fields2.currentText()
            if current_text != "Select field":
                current_text = (
                    ",FOREIGN KEY" + self.foreignkey_combo_fields2.currentText()
                )
                self.current_text_create.append(current_text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            current_text = self.references_combo2.currentText()
            if current_text != "Select field":
                current_text = "REFERENCES " + self.references_combo2.currentText()
                self.current_text_create.append(current_text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            current_text = self.foreignkey_combo_fields3.currentText()
            if current_text != "Select field":
                current_text = (
                    ",FOREIGN KEY" + self.foreignkey_combo_fields3.currentText()
                )
                self.current_text_create.append(current_text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            current_text = self.references_combo3.currentText()
            if current_text != "Select field":
                current_text = "REFERENCES " + self.references_combo3.currentText()
                self.current_text_create.append(current_text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_create.append(")")
        except (AttributeError, RuntimeError) as e:
            print(e)

        self.process_current_create()

    def process_current_create(self):
        firstItems = ["Select table", "Select field", "Select option", "Select type"]
        lista_create = []
        for e, text in enumerate(self.current_text_create):
            if text in firstItems:
                pass
            elif text is None:
                pass
            elif text == "":
                pass
            else:
                lista_create.append(text)
        self.lista_create = " ".join(lista_create)
        self.create_label_create()

    def create_label_create(self):
        self.label_create_check = QLabel()
        self.label_create_check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_label_create.setCellWidget(0, 0, self.label_create_check)
        self.label_create_check.setStyleSheet("QLabel { color: green; }")
        if len(self.lista_create) > 190:
            words = self.lista_create.split()
            above = " ".join(words[: len(words) // 3])
            half = " ".join(words[len(words) // 3: (len(words) // 3) * 2])
            below = " ".join(words[(len(words) // 3) * 2:])
            self.table_label_create.setMaximumHeight(70)
            self.table_label_create.setRowHeight(0, 70)
            self.label_create_check.setText(above + "\n" + half + "\n" + below)
        elif len(self.lista_create) > 90:
            words = self.lista_create.split()
            above = " ".join(words[: len(words) // 2])
            below = " ".join(words[len(words) // 2:])
            self.table_label_create.setMaximumHeight(45)
            self.table_label_create.setRowHeight(0, 45)
            self.label_create_check.setText(above + "\n" + below)
        else:
            self.table_label_create.setMaximumHeight(30)
            self.table_label_create.setRowHeight(0, 30)
            self.label_create_check.setText(self.lista_create)

    def execute_create(self):
        self.check_data_create()
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                done = "BEGIN TRANSACTION;" + self.lista_create + ";COMMIT TRANSACTION;"
                cursor.execute("BEGIN TRANSACTION;")
                cursor.execute(self.lista_create)
                cursor.execute(";COMMIT TRANSACTION;")
                print(
                    "_" * 120,
                    "\nDONE\n",
                    done,
                )
                message = Messagebox()
                message.question()
        except sqlite3.OperationalError as e:
            print(f"sqlite3.OperationalError {e} :execute_create")
            message = Messagebox()
            message.critical(str(e))
