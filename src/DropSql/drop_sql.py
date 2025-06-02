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
from src.DropSql.table_drop import TableDrop
from src.UtilsSql.connect_db import ConnectDb
from src.UtilsSql.messages import Messagebox


class Drop(QWidget, TableDrop):
    def __init__(self):
        super().__init__()
        self.qvbox_drop = QVBoxLayout()
        self.qvbox_drop_stretch = QHBoxLayout()
        self.qvbox_drop_stretch.addStretch()
        self.qvbox_drop_stretch.addWidget(self.table_drop)
        self.qvbox_drop.addLayout(self.qvbox_drop_stretch)
        self.qvbox_drop_stretch.addStretch()
        self.qvbox_drop.setContentsMargins(10, 10, 10, 10)
        self.qvbox_drop.addStretch()
        self.layout_label_Drop = QVBoxLayout()
        self.qvbox_drop.addLayout(self.layout_label_Drop)
        self.setLayout(self.qvbox_drop)
        self.create_table_label_drop()

    def create_table_label_drop(self):
        self.table_label_drop = QTableWidget(1, 1)
        self.table_label_drop.setMaximumHeight(30)
        self.table_label_drop.setColumnWidth(0, 970)
        self.table_label_drop.horizontalHeader().setVisible(False)
        self.table_label_drop.verticalHeader().setVisible(False)
        self.button_check_drop = QPushButton("Check drop / delete")
        self.button_check_drop.clicked.connect(self.check_data_drop)
        self.button_execute_drop = QPushButton("Execute drop / delete")
        self.button_execute_drop.clicked.connect(self.execute_drop)
        self.layout_button_Drop = QHBoxLayout()
        self.layout_button_Drop.addWidget(self.button_check_drop)
        self.layout_button_Drop.addWidget(self.button_execute_drop)
        self.layout_label_Drop.addWidget(self.table_label_drop)
        self.qvbox_drop.addLayout(self.layout_button_Drop)

    def check_data_drop(self):
        self.current_text_drop = []
        try:
            self.current_text_drop.append(self.combo_drop_truncate.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_drop.append(self.combo_drop_table.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_drop.append(self.delete_combo_where.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_drop.append(self.delete_combo_where_result.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            if self.checkbox_truncate.isChecked() is True:
                primarykey = ConnectDb.get_primary_key(
                    self, self.combo_drop_table.currentText()
                )
                primarykey = " ".join(primarykey)
                self.current_text_truncate = (
                    "UPDATE sqlite_sequence SET seq = (SELECT MAX(",
                    primarykey,
                    ") FROM "
                    + "'"
                    + self.combo_drop_table.currentText()
                    + "'"
                    + ") WHERE name = "
                    + "'"
                    + self.combo_drop_table.currentText()
                    + "'",
                )
                self.current_text_truncate = " ".join(self.current_text_truncate)
        except (AttributeError, ValueError, RuntimeError) as e:
            print(e)

        self.process_current_drop()

    def process_current_drop(self):
        first_items = ["Select table", "Select option", "Select WHERE"]
        lista_drop = []
        for e, text in enumerate(self.current_text_drop):
            if text in first_items:
                pass
            elif text is None:
                pass
            elif text == "":
                pass
            else:
                lista_drop.append(text)
        self.lista_drop = ""
        self.lista_drop = " ".join(lista_drop)
        label_drop = self.lista_drop
        try:
            if self.checkbox_truncate.isChecked() is True:
                label_drop = self.lista_drop + "; " + self.current_text_truncate
        except (AttributeError, RuntimeError) as e:  # noqa: F841
            print(f"{e} :process_current_drop")
        self.label_drop_check = QLabel(label_drop)
        self.label_drop_check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_drop_check.setStyleSheet("QLabel { color: green; }")
        self.table_label_drop.setCellWidget(0, 0, self.label_drop_check)

    def execute_drop(self):
        self.check_data_drop()
        try:
            with sqlite3.connect(self.filename) as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                done = "BEGIN TRANSACTION;" + self.lista_drop + ";COMMIT TRANSACTION;"
                cur.execute("BEGIN TRANSACTION;")
                cur.execute(self.lista_drop)
                cur.execute(";COMMIT TRANSACTION;")
                print(
                    "_" * 120,
                    "\nDONE\n",
                    done,
                )
                message = Messagebox()
                option = self.combo_drop_truncate.currentText()
                if option == "DROP TABLE":
                    message.question()
                else:
                    info = f"Table {self.combo_drop_table.currentText()} Deleted From"
                    message.info(info)
                    self.execute_autoincrement()
        except sqlite3.OperationalError as e:
            print(f"sqlite3.OperationalError {e} :execute_drop")
            message = Messagebox()
            message.critical(str(e))

    def execute_autoincrement(self):
        if self.checkbox_truncate.isChecked() is True:
            try:
                # self.current_text_truncate = " ".join(self.current_text_truncate)
                with sqlite3.connect(self.filename) as con:
                    con.row_factory = sqlite3.Row
                    cur = con.cursor()
                    done = (
                        "BEGIN TRANSACTION;",
                        self.current_text_truncate,
                        ";COMMIT TRANSACTION;",
                    )
                    cur.execute("BEGIN TRANSACTION;")
                    cur.execute(self.current_text_truncate)
                    cur.execute(";COMMIT TRANSACTION;")
                    print(
                        "_" * 120,
                        "\nDONE\n",
                        done,
                    )
                    message = Messagebox()
                    info = f"Table {self.combo_drop_table.currentText()} Reseted autoincrement"
                    message.info(info)
            except (sqlite3.OperationalError, AttributeError) as e:
                print(f"sqlite3.OperationalError {e} :execute_autoincrement")
                message = Messagebox()
                message.critical(str(e))
