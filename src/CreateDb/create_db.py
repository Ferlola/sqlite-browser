import sys
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QTableWidget,
    QApplication,
)
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
from src.CreateDb.table_create_db import TableCreateDb


class CreateDb(QWidget, TableCreateDb):
    def __init__(self):
        super().__init__()
        self.qvbox_create_db = QVBoxLayout()
        self.qvbox_create_db_stretch = QHBoxLayout()
        self.button_relaunch = QPushButton("Restart")
        self.qvbox_create_db_stretch.addStretch()
        self.qvbox_create_db_stretch.addWidget(self.table_db)
        self.qvbox_create_db_stretch.addWidget(self.message_db)
        self.qvbox_create_db.addLayout(self.qvbox_create_db_stretch)
        self.qvbox_create_db_stretch.addStretch()
        self.qvbox_create_db.setContentsMargins(10, 10, 10, 10)
        self.qvbox_create_db.addStretch()
        self.layout_label_CreateDb = QVBoxLayout()
        self.qvbox_create_db.addLayout(self.layout_label_CreateDb)
        self.setLayout(self.qvbox_create_db)
        self.create_table_label_createdb()

    def create_table_label_createdb(self):
        self.table_label_create_db = QTableWidget(1, 1)
        self.table_label_create_db.setMaximumHeight(30)
        self.table_label_create_db.setColumnWidth(0, 970)
        self.table_label_create_db.horizontalHeader().setVisible(False)
        self.table_label_create_db.verticalHeader().setVisible(False)
        self.button_check_create_db = QPushButton("Check create DATABASE")
        self.button_check_create_db.clicked.connect(self.check_data_db)
        self.button_execute_create_db = QPushButton("Execute create DATABASE")
        self.button_execute_create_db.clicked.connect(self.execute_db)
        self.layout_button_CreateDb = QHBoxLayout()
        self.layout_button_CreateDb.addWidget(self.button_check_create_db)
        self.layout_button_CreateDb.addWidget(self.button_execute_create_db)
        self.layout_label_CreateDb.addWidget(self.table_label_create_db)
        self.qvbox_create_db.addLayout(self.layout_button_CreateDb)

    def check_data_db(self):
        self.current_text_db = []
        try:
            text = self.db_line_edit.text()
            if text:
                text = "CREATE DATABASE " + text
                self.current_text_db.append(text)
        except (AttributeError, RuntimeError) as e:
            print(e)

        self.current_text_db = " ".join(map(str, self.current_text_db))
        self.label_db = QLabel(self.current_text_db)
        self.label_db.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_db.setStyleSheet("color: green")
        self.table_label_create_db.setCellWidget(0, 0, self.label_db)

    def execute_db(self):
        self.check_data_db()
        import sqlite3

        try:
            text = self.db_line_edit.text()
            if text[-3:] == ".db":
                with sqlite3.connect(self.db_line_edit.text()):
                    self.message_db.setStyleSheet("color: green")
                    self.message_db.setText(
                        f"Please restart the application to select:  {self.db_line_edit.text()}"
                    )
                    self.button_relaunch = QPushButton("Restart")
                    self.button_relaunch.clicked.connect(self.relaunch)
                    self.qvbox_create_db_stretch.addWidget(self.button_relaunch)
            else:
                self.qvbox_create_db_stretch.removeWidget(self.button_relaunch)
                self.button_relaunch.deleteLater()
                self.button_relaunch = None
                self.message_db.setStyleSheet("color: red")
                self.message_db.setText("Error: missing '.db' extension")
        except sqlite3.OperationalError as e:
            print(f"{e} :execute_db")

    def relaunch(self):
        QApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)
