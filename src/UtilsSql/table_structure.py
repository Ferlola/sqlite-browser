from PyQt6.QtWidgets import QTableWidget, QLabel
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableStructure(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_structure()

    def create_table_structure(self):
        self.table_structure = QTableWidget(1, 1)
        self.table_structure.setMaximumHeight(30)
        self.table_structure.setColumnWidth(0, 950)
        self.table_structure.horizontalHeader().setVisible(False)
        self.table_structure.verticalHeader().setVisible(False)

    def create_label_structure(self):
        self.labelStructure = QLabel()
        self.labelStructure.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_structure.setCellWidget(0, 0, self.labelStructure)
        self.labelStructure.setStyleSheet("QLabel { color: green; }")
        self.structure = "TABLE STRUCTURE:  " + self.structure
        if len(self.structure) > 190:
            palabras = self.structure.split()
            arriba = " ".join(palabras[: len(palabras) // 3])
            medio = " ".join(palabras[len(palabras) // 3: (len(palabras) // 3) * 2])
            abajo = " ".join(palabras[(len(palabras) // 3) * 2:])
            self.table_structure.setMaximumHeight(70)
            self.table_structure.setRowHeight(0, 70)
            self.labelStructure.setText(arriba + "\n" + medio + "\n" + abajo)
        elif len(self.structure) > 90:
            palabras = self.structure.split()
            self.arriba = " ".join(palabras[: len(palabras) // 2])
            self.abajo = " ".join(palabras[len(palabras) // 2:])
            self.table_structure.setMaximumHeight(45)
            self.table_structure.setRowHeight(0, 45)
            self.labelStructure.setText(self.arriba + "\n" + self.abajo)
        else:
            self.table_structure.setMaximumHeight(30)
            self.table_structure.setRowHeight(0, 30)
            self.labelStructure.setText(self.structure)
