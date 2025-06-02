from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QTableWidget,
)
from PyQt6.QtCore import Qt
import sqlite3
from src.UpdateSql.table_update import TableUpdate
from src.UtilsSql.get_comillas import get_comillas
from src.UtilsSql.messages import Messagebox


class Update(QWidget, TableUpdate):
    def __init__(self):
        super().__init__()
        self.qvbox_update = QVBoxLayout()
        self.qvbox_update.addWidget(self.table_update)
        self.qvbox_update.setContentsMargins(10, 10, 10, 10)
        self.qvbox_update.addStretch()
        self.layout_label_update = QVBoxLayout()
        self.qvbox_update.addLayout(self.layout_label_update)
        self.setLayout(self.qvbox_update)
        self.create_table_label_update()

    def create_table_label_update(self):
        self.table_label_update = QTableWidget(1, 1)
        self.table_label_update.setMaximumHeight(30)
        self.table_label_update.setColumnWidth(0, 970)
        self.table_label_update.horizontalHeader().setVisible(False)
        self.table_label_update.verticalHeader().setVisible(False)
        self.button_check_update = QPushButton("Check update")
        self.button_check_update.clicked.connect(self.check_data_update)
        self.button_execute_update = QPushButton("Execute update")
        self.button_execute_update.clicked.connect(self.execute_update)
        self.layout_button_Update = QHBoxLayout()
        self.layout_button_Update.addWidget(self.button_check_update)
        self.layout_button_Update.addWidget(self.button_execute_update)
        self.layout_label_update.addWidget(self.table_label_update)
        self.qvbox_update.addLayout(self.layout_button_Update)

    def check_data_update(self):
        self.current_text_update = []
        try:
            self.current_text_update.append(self.combo_update_table.currentText())
        except AttributeError as e:
            print(e)

        try:
            tableUpdate = self.combo_update_table.currentText()
            if tableUpdate != "Select table":
                self.current_text_update.append("SET")
        except AttributeError as e:
            print(e)

        try:
            self.current_text_update.append(self.combo_update_fields1.currentText())
        except AttributeError as e:
            print(e)

        try:
            item = get_comillas(self.line_edit_update1.text())
            self.current_text_update.append(item)
        except AttributeError as e:
            print(e)

        try:
            self.current_text_update.append(self.combo_update_fields2.currentText())
        except AttributeError as e:
            print(e)

        try:
            item = get_comillas(self.line_edit_update2.text())
            self.current_text_update.append(item)
        except AttributeError as e:
            print(e)

        try:
            self.current_text_update.append(self.label_where.text())
        except AttributeError as e:
            print(e)

        try:
            self.current_text_update.append(self.combo_update_fields3.currentText())
        except AttributeError as e:
            print(e)

        try:
            self.current_text_update.append(self.combo_update_fields4.currentText())
        except AttributeError as e:
            print(e)
        self.process_current_update()

    def process_current_update(self):
        first_items = ["Select table", "Select field", "Select data"]
        lista_update = []
        lista_update.append("UPDATE")
        for e, text in enumerate(self.current_text_update):
            if text in first_items:
                pass
            elif text is None:
                pass
            elif text == "":
                pass
            else:
                lista_update.append(text)
        self.lista_update = ""
        self.lista_update = " ".join(lista_update)
        self.label_update_check = QLabel(self.lista_update)
        self.label_update_check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_update_check.setStyleSheet("QLabel { color: green; }")
        self.table_label_update.setCellWidget(0, 0, self.label_update_check)

    def execute_update(self):
        self.check_data_update()
        print(self.lista_update)
        try:
            with sqlite3.connect(self.filename) as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                done = "BEGIN TRANSACTION;" + self.lista_update + ";COMMIT TRANSACTION;"
                cur.execute("BEGIN TRANSACTION;")
                cur.execute(self.lista_update)
                cur.execute(";COMMIT TRANSACTION;")
                print(
                    "_" * 120,
                    "\nDONE\n",
                    done,
                )
                message = Messagebox()
                text = (
                    "Updated values in "
                    + self.combo_update_table.currentText()
                    + " table"
                )
                message.info(text)
        except sqlite3.OperationalError as e:
            print(f"sqlite3.OperationalError {e} :execute_update")
            message = Messagebox()
            message.critical(str(e))
