from PyQt6.QtWidgets import QTableWidget, QLineEdit, QLabel
from PyQt6.QtCore import Qt


class TableCreateDb:
    def __init__(self):
        super().__init__()
        self.style_qLine = (
            "QLineEdit" "{" "border : 2px solid black;" "background : lightgreen;" "}"
        )
        self.style_qLine1 = (
            "QLineEdit"
            "{"
            "color: green; border : 2px solid green;"
            "background : white;"
            "}"
        )
        self.message_db = QLabel()
        self.create_table_db()

    def create_table_db(self):
        self.table_db = QTableWidget(1, 2)
        self.table_db.setMaximumHeight(30)
        self.table_db.setMaximumWidth(232)
        self.table_db.setColumnWidth(0, 130)
        self.table_db.setColumnWidth(1, 100)
        self.table_db.horizontalHeader().setVisible(False)
        self.table_db.verticalHeader().setVisible(False)
        self.create_db_label()
        self.create_db_lineedit()

    def create_db_label(self):
        self.db_label = QLabel("CREATE DATABASE")
        self.db_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.db_label.setStyleSheet("color: black")
        self.table_db.setCellWidget(0, 0, self.db_label)

    def create_db_lineedit(self):
        self.db_line_edit = QLineEdit()
        self.db_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.db_line_edit.setStyleSheet(self.style_qLine)
        self.db_line_edit.textChanged.connect(self.get_db_lineedit)
        self.table_db.setCellWidget(0, 1, self.db_line_edit)

    def get_db_lineedit(self):
        if len(self.db_line_edit.text()) is not None:
            self.db_line_edit.setStyleSheet(self.style_qLine)
            self.db_label.setStyleSheet("color: black")
        if len(self.db_line_edit.text()) > 0:
            self.db_line_edit.setStyleSheet(self.style_qLine1)
            self.db_label.setStyleSheet("color: green")
