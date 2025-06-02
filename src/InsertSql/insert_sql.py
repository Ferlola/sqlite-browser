from PyQt6.QtWidgets import (
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt
import sqlite3
from src.InsertSql.table_insert import TableInsert
from src.UtilsSql.table_structure import TableStructure
from src.UtilsSql.messages import Messagebox
from src.UtilsSql.split_text import split_text
from PyQt6.QtCore import pyqtSignal


class Insert(QWidget, TableInsert, TableStructure):
    dataChangedInsert = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.qvbox_insert = QVBoxLayout()
        self.qvbox_insert.addWidget(self.table_insert)
        self.qvbox_insert.addWidget(self.table_structure)
        self.qvbox_insert.setContentsMargins(10, 10, 10, 10)
        self.qvbox_insert.addStretch()
        self.layout_label_insert = QVBoxLayout()
        self.qvbox_insert.addLayout(self.layout_label_insert)
        self.setLayout(self.qvbox_insert)
        self.create_table_label_insert()

    def create_table_label_insert(self):
        self.table_label_insert = QTableWidget(1, 1)
        self.table_label_insert.setMaximumHeight(30)
        self.table_label_insert.setColumnWidth(0, 970)
        self.table_label_insert.horizontalHeader().setVisible(False)
        self.table_label_insert.verticalHeader().setVisible(False)
        self.button_check_insert = QPushButton("Check insert")
        self.button_check_insert.clicked.connect(self.check_data_insert)
        self.button_execute_insert = QPushButton("Execute insert")
        self.button_execute_insert.clicked.connect(self.execute_insert)
        self.layout_button_insert = QHBoxLayout()
        self.layout_button_insert.addWidget(self.button_check_insert)
        self.layout_button_insert.addWidget(self.button_execute_insert)
        self.layout_label_insert.addWidget(self.table_label_insert)
        self.qvbox_insert.addLayout(self.layout_button_insert)

    def check_data_insert(self):
        self.current_text_insert = []
        try:
            self.current_text_insert.append(self.combo_insert.currentText())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_insert.append(self.label_insert_prths1.text())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            labels = ""
            for i, field in enumerate(self.fields, 3):
                if len(self.lines["self.lineEditInsert" + str(i)].text()) > 0:
                    labels += ", " + field
            labels = str(labels).replace(", ", " ", 1)
            self.current_text_insert.append(labels)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_insert.append(self.label_insert_prths2.text())
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_insert.append("VALUES(")
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            line = " "
            for i, field in enumerate(self.fields, 3):
                if len(self.lines["self.lineEditInsert" + str(i)].text()) > 0:
                    line += (
                        ", '" + self.lines["self.lineEditInsert" + str(i)].text() + "' "
                    )
            values = str(line).replace(", ", " ", 1)
            self.current_text_insert.append(values)
        except (AttributeError, RuntimeError) as e:
            print(e)

        try:
            self.current_text_insert.append(")")
        except (AttributeError, RuntimeError) as e:
            print(e)

        self.process_current_text_insert()

    def process_current_text_insert(self):
        first_items = ["Select table"]
        lista = []
        lista.append("INSERT INTO")
        for e, text in enumerate(self.current_text_insert):
            if text in first_items:
                pass
            elif text is None:
                pass
            elif text == "":
                pass
            else:
                lista.append(text)
        self.lista_insert = ""
        self.lista_insert = " ".join(map(str, lista))
        insert_label = split_text(self.lista_insert)
        self.label_insert_check = QLabel(insert_label)
        self.label_insert_check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_insert_check.setStyleSheet("QLabel { color: green; }")
        self.table_label_insert.setCellWidget(0, 0, self.label_insert_check)

    def execute_insert(self):
        self.check_data_insert()
        print(self.lista_insert)

        try:
            lista_insert = self.lista_insert.replace(
                "INSERT INTO", "WITH RECURSIVE INSERT OR FAIL INTO"
            )
            with sqlite3.connect(self.filename) as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                done = "BEGIN TRANSACTION;" + lista_insert + ";COMMIT TRANSACTION;"
                cur.execute("BEGIN TRANSACTION;")
                cur.execute(self.lista_insert)
                cur.execute(";COMMIT TRANSACTION;")
                print(
                    "_" * 120,
                    "\nDONE\n",
                    done,
                )
                message = Messagebox()
                text = (
                    "Inserted values in " + self.combo_insert.currentText() + " table"
                )
                message.info(text)
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as e:
            print(f"sqlite3.OperationalError {e} :executeCreate")
            message = Messagebox()
            message.critical(str(e))
