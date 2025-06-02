from PyQt6.QtWidgets import (
    QTableWidget,
    QComboBox,
    QTableWidgetItem,
    QVBoxLayout,
    QPushButton,
)
from src.UtilsSql.connect_db import ConnectDb


class TableDataSheet(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_datasheet()
        self.layout_data = QVBoxLayout()

    def create_table_datasheet(self):
        self.table_data_sheet = QTableWidget(1, 2)
        self.table_data_sheet.setColumnWidth(0, 150)
        self.table_data_sheet.setColumnWidth(1, 80)
        self.table_data_sheet.setMaximumHeight(30)
        self.table_data_sheet.setMaximumWidth(232)
        self.table_data_sheet.horizontalHeader().setVisible(False)
        self.table_data_sheet.verticalHeader().setVisible(False)
        self.create_datasheet_combo()
        self.create_datasheet_update_button()

    def create_datasheet_combo(self):
        self.data_sheet_combo = QComboBox()
        self.data_sheet_combo.addItem("Select table")
        self.data_sheet_combo.addItems(ConnectDb.get_all_tables(self))
        self.data_sheet_combo.currentIndexChanged.connect(self.get_datasheet_combo)
        self.table_data_sheet.setCellWidget(0, 0, self.data_sheet_combo)

    def create_datasheet_update_button(self):
        self.data_sheet_update_button = QPushButton("Update")
        self.data_sheet_update_button.clicked.connect(self.get_datasheet_update_button)
        self.table_data_sheet.setCellWidget(0, 1, self.data_sheet_update_button)

    def get_datasheet_update_button(self):
        self.get_datasheet_combo()

    def get_datasheet_combo(self):
        current_data = self.data_sheet_combo.currentText()
        if current_data != "Select table":
            for i in reversed(range(self.layout_data.count())):
                self.layout_data.itemAt(i).widget().deleteLater()
                self.layout_data.itemAt(i).widget().setParent(None)
                del self.layout_data
                self.layout_data = QVBoxLayout()
            self.data = self.get_data_sheet(current_data)
            self.create_table()

    def create_table(self):
        self.data_table = QTableWidget()
        self.data_table.setMaximumHeight(600)
        self.data_table.setRowCount(len(self.data))
        self.data_table.setColumnCount(len(self.data.columns))
        self.data_table.verticalHeader().setVisible(False)
        self.data_table.setHorizontalHeaderLabels(self.data.columns.tolist())
        self.data_table.setRowCount(len(self.data))
        self.data_table.setColumnCount(len(self.data.columns))
        for i in range(len(self.data)):
            for j in range(len(self.data.columns)):
                self.data_table.setItem(
                    i, j, QTableWidgetItem(str(self.data.iat[i, j]))
                )
        self.layout_data.addWidget(self.data_table)
        self.qvbox_data_sheet.addLayout(self.layout_data)
