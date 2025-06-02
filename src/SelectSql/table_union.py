from PyQt6.QtWidgets import QTableWidget, QComboBox, QCheckBox, QLabel, QTableWidgetItem
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from src.UtilsSql.connect_db import ConnectDb
from src.UtilsSql.create_model import create_model
from src.UtilsSql.clear_data import ClearDataSelect


class TableUnion(ConnectDb):
    def __init__(self):
        super().__init__()
        self.create_table_union()

    def current_text_color_union(self, row, column, current_text):
        current_text.setForeground(QColor("green"))
        self.table_union.setItem(row, column, QTableWidgetItem(current_text))

    def create_table_union(self):
        self.table_union = QTableWidget(1, 4)
        self.table_union.setMaximumHeight(30)
        self.table_union.setColumnWidth(0, 100)
        self.table_union.setColumnWidth(1, 120)
        self.table_union.setColumnWidth(2, 200)
        self.table_union.horizontalHeader().setVisible(False)
        self.table_union.verticalHeader().setVisible(False)
        self.rowUnion = self.table_union.rowCount()
        self.create_checkbox_union()

    def create_checkbox_union(self):
        self.checkbox_union = QCheckBox(text="UNION")
        self.checkbox_union.setTristate(False)
        self.checkbox_union.stateChanged.connect(self.on_state_changed_checkbox_union)
        self.table_union.setCellWidget(0, 0, self.checkbox_union)

    def on_state_changed_checkbox_union(self):
        state = self.checkbox_union.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_union.setStyleSheet("color : green")
            self.table_union.setMaximumHeight(123)
            self.table_union.setRowCount(3)
            self.table_union.insertRow(self.rowUnion)
            self.create_checkbox_all()
            self.create_union_label_select()
            self.create_union_select_combo()
        else:
            self.checkbox_all.setChecked(False)
            self.table_union.setRowCount(1)
            self.table_union.setMaximumHeight(30)
            self.checkbox_union.setStyleSheet("color : black")
            self.checkbox_all.setStyleSheet("color : black")
            self.table_union.removeRow(self.rowUnion)
            self.table_union.setMaximumHeight(30)
            self.table_union.removeCellWidget(0, 1)
            self.table_union.removeCellWidget(2, 0)
            self.table_union.removeCellWidget(3, 0)
            ClearDataSelect.clear_column_combo_union_in(self)

    def create_checkbox_all(self):
        self.checkbox_all = QCheckBox(text="ALL")
        self.checkbox_all.setTristate(False)
        self.checkbox_all.stateChanged.connect(self.on_state_changed_checkbox_all)
        self.table_union.setCellWidget(0, 1, self.checkbox_all)

    def on_state_changed_checkbox_all(self):
        state = self.checkbox_all.checkState()
        if state == Qt.CheckState.Checked:
            self.checkbox_all.setStyleSheet("color : green")
        else:
            self.checkbox_all.setStyleSheet("color : black")

    def create_union_label_select(self):
        self.union_label_select = QLabel("SELECT")
        self.union_label_select.setStyleSheet("color:green;")
        self.union_label_select.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_union.setCellWidget(1, 0, self.union_label_select)

    def create_union_select_combo(self):
        self.union_select_combo = QtWidgets.QComboBox()
        current_table = self.combo_tables.currentText()
        current_table = current_table.replace("FROM ", "")
        fields = ConnectDb.get_fields_table(self, current_table)
        model = create_model(fields)
        self.models_union = {}
        row = self.table_union.rowCount()
        self.union_select_combo.setModel(model)
        model.itemChanged.connect(lambda _, row=row: self.on_item_changed_union(row))
        item = QTableWidgetItem()
        self.table_union.setItem(1, 2, item)
        self.models_union[row] = model
        self.table_union.setCellWidget(1, 1, self.union_select_combo)
        firstItem = QtGui.QStandardItem("Select field/s")
        model.setItem(0, firstItem)

    def on_item_changed_union(self, tableRow):
        model = self.models_union[tableRow]
        self.items_checked_union = []
        for row in range(model.rowCount()):
            if model.item(row).checkState() == Qt.CheckState.Checked:
                first_string = model.item(row).text().split(",")[-1]
                self.items_checked_union.append(first_string)
        if len(self.items_checked_union) > 0:
            self.create_union_label_from()
            self.create_union_combo_tables()
        else:
            self.table_union.removeCellWidget(2, 0)
        for item in self.items_checked_union:
            item = QTableWidgetItem(item)
            self.current_text_color_union(1, 2, item)
        try:
            self.table_union.item(1, 2).setText(", ".join(self.items_checked_union))
        except AttributeError as e:
            print(f"{e} :on_item_changed_union")
        self.itemsUnion = ", ".join(self.items_checked_union)

    def create_union_label_from(self):
        self.union_label_from = QLabel("FROM")
        self.union_label_from.setStyleSheet("color:green;")
        self.union_label_from.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_union.setCellWidget(2, 0, self.union_label_from)

    def create_union_combo_tables(self):
        self.union_tables = QComboBox()
        self.union_tables.addItem("FROM table")
        self.union_tables.addItems(ConnectDb.get_all_tables(self))
        self.table_union.setCellWidget(2, 1, self.union_tables)
        self.union_tables.currentIndexChanged.connect(self.get_union_tables)

    def get_union_tables(self):
        current_text = self.union_tables.currentText()
        if current_text != "FROM table":
            self.union_tables.setStyleSheet("QComboBox{{ color: {} }}".format("green"))
            self.create_union_label_where()
            self.create_union_where_combo()
        else:
            self.table_union.removeCellWidget(3, 0)
            self.table_union.removeCellWidget(3, 1)
            self.union_tables.setStyleSheet("QComboBox{{ color: {} }}".format("black"))

    def create_union_label_where(self):
        self.union_label_where = QLabel("WHERE")
        self.union_label_where.setStyleSheet("color:green;")
        self.union_label_where.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_union.setCellWidget(3, 0, self.union_label_where)

    def create_union_where_combo(self):
        current_text = self.union_tables.currentText()
        items = ConnectDb.get_fields_table(self, current_text)
        self.union_where_combo = QComboBox()
        self.union_where_combo.addItem("WHERE field")
        for item in items:
            self.union_where_combo.addItem(item)
        self.table_union.setCellWidget(3, 1, self.union_where_combo)
        self.union_where_combo.currentIndexChanged.connect(self.get_union_where_combo)

    def get_union_where_combo(self):
        current_text = self.union_where_combo.currentText()
        if current_text != "WHERE field":
            self.create_union_combobox_operators()
            self.union_where_combo.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_union.removeCellWidget(3, 2)
            self.union_where_combo.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def create_union_combobox_operators(self):
        self.combo_union_operator = QComboBox()
        self.combo_union_operator.addItems(
            ["Operator", "=", ">", "<", ">=", "<=", "<>", "IS NULL", "IS NOT NULL"]
        )
        self.table_union.setCellWidget(3, 2, self.combo_union_operator)
        self.combo_union_operator.currentIndexChanged.connect(self.get_union_operator)

    def get_union_operator(self):
        current_text = self.combo_union_operator.currentText()
        if current_text != "Operator":
            self.result_union_operator()
            self.combo_union_operator.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
        else:
            self.table_union.removeCellWidget(3, 3)
            self.combo_union_operator.setStyleSheet(
                "QComboBox{{ color: {} }}".format("black")
            )

    def result_union_operator(self):
        self.union_operator = QComboBox()
        current_text_table = self.union_tables.currentText()
        current_text_table = "FROM " + current_text_table
        current_text = self.union_where_combo.currentText()
        if current_text != "WHERE field":
            items = ConnectDb.get_data_column(self, current_text_table, current_text)
            itemsSet = set(items)
            items = list(itemsSet)
            self.union_operator.addItems(items)
            self.union_operator.setStyleSheet(
                "QComboBox{{ color: {} }}".format("green")
            )
            self.table_union.setCellWidget(3, 3, self.union_operator)
        else:
            self.table_union.removeCellWidget(3, 1)
            self.table_union.removeCellWidget(3, 2)
