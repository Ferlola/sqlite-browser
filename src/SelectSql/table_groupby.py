from PyQt6.QtWidgets import QTableWidget, QComboBox, QCheckBox
from PyQt6.QtCore import Qt
from src.UtilsSql.connect_db import ConnectDb


class TableGroupBy(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_groupby()

    def create_table_groupby(self):
        self.table_group_by = QTableWidget(1, 2)
        self.table_group_by.setMaximumHeight(30)
        self.table_group_by.setColumnWidth(0, 120)
        self.table_group_by.setColumnWidth(1, 180)
        self.table_group_by.horizontalHeader().setVisible(False)
        self.table_group_by.verticalHeader().setVisible(False)
        self.create_checkbox_groupby()

    def create_checkbox_groupby(self):
        self.checkbox_group_by = QCheckBox(text="GROUP BY")
        self.checkbox_group_by.setTristate(False)
        self.checkbox_group_by.stateChanged.connect(
            self.on_state_changed_checkbox_groupby
        )
        self.table_group_by.setCellWidget(0, 0, self.checkbox_group_by)

    def on_state_changed_checkbox_groupby(self):
        state = self.checkbox_group_by.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_group_by.setStyleSheet("color: green")
            self.create_combo_groupby()
        else:
            self.table_group_by.removeCellWidget(0, 1)
            self.checkbox_group_by.setStyleSheet("color: black")

    def create_combo_groupby(self):
        self.combo_group_by = QComboBox()
        self.combo_group_by.addItem("Select field")
        try:
            current_text = self.combo_join_tables1.currentText()
            items = ConnectDb.get_fields_table_by(self, current_text)
            self.combo_group_by.addItems(items)
        except (AttributeError, RuntimeError) as e:
            print(f"{e} :create_combo_groupby")
        try:
            current_text = self.combo_tables.currentText()
            current_text = current_text.replace("FROM ", "")
            items = ConnectDb.get_fields_table_by(self, current_text)
            self.combo_group_by.addItems(items)
        except AttributeError as e:
            print(f"{e} :create_combo_groupby")
        self.table_group_by.setCellWidget(0, 1, self.combo_group_by)
        self.combo_group_by.currentIndexChanged.connect(self.get_combo_groupby)

    def get_combo_groupby(self):
        current_text = self.combo_group_by.currentText()
        if current_text != "Select field":
            self.combo_group_by.setStyleSheet("color: green")
        else:
            self.combo_group_by.setStyleSheet("color: black")
