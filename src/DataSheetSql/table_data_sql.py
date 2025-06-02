from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
from src.DataSheetSql.table_data_sheet import TableDataSheet


class DataSheet(QWidget, TableDataSheet):
    def __init__(self):
        super().__init__()
        self.qvbox_data_sheet = QVBoxLayout()
        self.qvbox_data_sheet_stretch = QHBoxLayout()
        self.qvbox_data_sheet.addLayout(self.qvbox_data_sheet_stretch)
        self.qvbox_data_sheet_stretch.addStretch()
        self.qvbox_data_sheet_stretch.addWidget(self.table_data_sheet)
        self.qvbox_data_sheet_stretch.addStretch()
        self.qvbox_data_sheet.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.qvbox_data_sheet)
