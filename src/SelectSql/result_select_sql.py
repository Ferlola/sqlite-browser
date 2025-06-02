import sqlite3
import pandas as pd
from PyQt6.QtWidgets import QTableWidget, QVBoxLayout, QLabel, QTableWidgetItem, QDialog
from PyQt6.QtCore import Qt
from src.UtilsSql.split_text import split_text


class ResultSelect(QDialog):
    def __init__(self, texto):
        super(ResultSelect, self).__init__()
        from src.UtilsSql.utils import filename

        self.setGeometry(10, 10, 950, 700)
        self.texto = texto
        self.filename = filename
        self.setWindowTitle(str(filename))
        try:
            with sqlite3.connect(self.filename) as con:
                con = sqlite3.connect(self.filename)
                df = pd.read_sql(self.texto, con)
        except sqlite3.OperationalError as e:
            print(f"{e} :ResultSelect")
        table = QTableWidget()
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        table.verticalHeader().setVisible(False)
        table.setHorizontalHeaderLabels(df.columns.tolist())
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        for i in range(len(df)):
            for j in range(len(df.columns)):
                table.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
        self.main_layout = QVBoxLayout(self)
        self.label_query = QLabel()
        texto = split_text(self.texto)
        self.label_query = QLabel(texto, self)
        self.label_query.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_query.setStyleSheet("QLabel { color: green; }")
        self.main_layout.addWidget(self.label_query)
        self.main_layout.addWidget(table)
        self.main_layout.stretch(0)
