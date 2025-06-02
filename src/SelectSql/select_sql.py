import os
import csv
import sqlite3
import pandas as pd
from pandas.io.sql import DatabaseError
from PyQt6.QtWidgets import (
    QTableWidget,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt
from src.SelectSql.table_select import TableSelect
from src.SelectSql.table_distinct import TableDistinct
from src.SelectSql.table_fields import TableFields
from src.SelectSql.table_fields2 import TableFields2
from src.SelectSql.table_tables import TableTables
from src.SelectSql.table_where import TableWhere
from src.SelectSql.table_orderby import TableOrderBy
from src.SelectSql.table_and import TableAnd
from src.SelectSql.table_sum import TableSum
from src.SelectSql.table_avg import TableAvg
from src.SelectSql.table_select_sum import TableSelectSum
from src.SelectSql.table_count import TableCount
from src.SelectSql.table_and_or import TableAndOr
from src.SelectSql.table_join import TableJoin
from src.SelectSql.table_groupby import TableGroupBy
from src.SelectSql.table_having import TableHaving
from src.SelectSql.table_case import TableCase
from src.SelectSql.table_union import TableUnion
from src.UtilsSql.check_data import CheckDataSelect
from src.UtilsSql.clear_data import ClearDataSelect
from src.UtilsSql.messages import Messagebox
from src.SelectSql.result_select_sql import ResultSelect


class Select(
    QWidget,
    TableUnion,
    TableCase,
    TableGroupBy,
    TableHaving,
    TableSum,
    TableAvg,
    TableJoin,
    TableCount,
    TableAnd,
    TableAndOr,
    TableOrderBy,
    TableWhere,
    TableTables,
    TableDistinct,
    TableFields,
    TableFields2,
    TableSelectSum,
    TableSelect,
):

    def __init__(self):
        super().__init__()
        self.qvbox_select = QVBoxLayout()
        self.qvbox_select.addWidget(self.table_select_option)
        self.qvbox_select.addWidget(self.table_fields)
        self.table_fields.hide()
        self.qvbox_select.addWidget(self.table_fields2)
        self.table_fields2.hide()
        self.qvbox_select.addWidget(self.table_distinct_option)
        self.table_distinct_option.hide()
        self.qvbox_select.addWidget(self.table_sum)
        self.table_sum.hide()
        self.qvbox_select.addWidget(self.table_select_sum)
        self.table_select_sum.hide()
        self.qvbox_select.addWidget(self.table_avg)
        self.table_avg.hide()
        self.qvbox_select.addWidget(self.table_count)
        self.table_count.hide()
        self.qvbox_select.addWidget(self.table_case)
        self.table_case.hide()
        self.qvbox_select.addWidget(self.table_tables)
        self.table_tables.hide()
        self.qvbox_select.addWidget(self.table_join)
        self.table_join.hide()
        self.qvbox_select.addWidget(self.table_where)
        self.table_where.hide()
        self.qvbox_select.addWidget(self.table_and)
        self.table_and.hide()
        self.qvbox_select.addWidget(self.table_and_or)
        self.table_and_or.hide()
        self.qvbox_select.addWidget(self.table_group_by)
        self.table_group_by.hide()
        self.qvbox_select.addWidget(self.table_having)
        self.table_having.hide()
        self.qvbox_select.addWidget(self.table_union)
        self.table_union.hide()
        self.qvbox_select.addWidget(self.table_order_by)
        self.table_order_by.hide()
        self.qvbox_select.addStretch()
        self.layout_label_select = QVBoxLayout()
        self.qvbox_select.addLayout(self.layout_label_select)
        self.setLayout(self.qvbox_select)
        self.create_table_label_select()

    def create_table_label_select(self):
        self.table_label_select = QTableWidget(1, 1)
        self.table_label_select.setMaximumHeight(30)
        self.table_label_select.setColumnWidth(0, 970)
        self.table_label_select.horizontalHeader().setVisible(False)
        self.table_label_select.verticalHeader().setVisible(False)
        self.button_check_select = QPushButton("Check query")
        self.button_check_select.clicked.connect(self.process_current_test_list)
        self.button_execute_select = QPushButton("Execute")
        self.button_execute_select.clicked.connect(self.new_window)
        self.button_save_as_csv = QPushButton("Save as CSV")
        self.button_save_as_csv.clicked.connect(self.execute_data_select)
        self.button_clear_select = QPushButton("Clear form")
        self.button_clear_select.clicked.connect(self.clear_full_data_select)
        self.layout_button_select = QHBoxLayout()
        self.layout_button_select.addWidget(self.button_check_select)
        self.layout_button_select.addWidget(self.button_execute_select)
        self.layout_button_select.addWidget(self.button_save_as_csv)
        self.layout_button_select.addWidget(self.button_clear_select)
        self.layout_label_select.addWidget(self.table_label_select)
        self.qvbox_select.addLayout(self.layout_button_select)
        self.current_text_list = []

    def clear_full_data_select(self):
        ClearDataSelect.clear_data(self)
        ClearDataSelect.clear_column_combo_fields1_in(self)
        ClearDataSelect.clear_column_combo_fields2_in(self)
        ClearDataSelect.clear_column_combo_where_in(self)
        ClearDataSelect.clear_column_combobox_and_in(self)
        ClearDataSelect.clear_column_comboitems_and_or_in(self)
        ClearDataSelect.clear_column_combo_union_in(self)

    def create_label1(self):
        self.label_query = QLabel()
        self.label_query.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_query.setStyleSheet("QLabel { color: green; }")
        self.table_label_select.setCellWidget(0, 0, self.label_query)

    def process_current_test_list(self):
        self.create_label1()
        items = CheckDataSelect.check_data(self)
        first_items = [
            "Select option",
            "Select table",
            "Select WHERE",
            "Select data",
            "Select DISTINCT",
            "Select field/s",
            "Select field",
            "Select JOIN",
            "WHERE table",
            "WHERE field",
            "FROM table",
            "FROM table)",
            "Operators",
            "ASC/DESC",
            "ORDER BY?",
            "Next Order by",
            "SUM",
            "optr",
            "AND/OR",
            "AND?",
            "AND field",
            "HAVING",
            "count/avg/sum",
            "Operator",
            "WHEN/ELSE",
            "(AS)",
            "()",
            "( ?",
            ".",
        ]
        lista = []
        for e, text in enumerate(items):
            if text in first_items:
                pass
            elif text is None:
                pass
            elif text == "":
                pass
            else:
                lista.append(text)
        self.lista = "".join(" ".join(map(str, lista)))
        if len(self.lista) > 90:
            words = self.lista.split()
            up = " ".join(words[: len(words) // 2])
            below = " ".join(words[len(words) // 2:])
            self.table_label_select.setMaximumHeight(45)
            self.table_label_select.setRowHeight(0, 45)
            self.label_query.setText(up + "\n" + below)
            QLabel.repaint(self)
        else:
            self.table_label_select.setMaximumHeight(30)
            self.table_label_select.setRowHeight(0, 30)
            self.label_query.setText(self.lista)

    def execute_data_select(self):
        self.process_current_test_list()
        try:
            with sqlite3.connect(self.filename) as con:
                con.row_factory = sqlite3.Row
                cur = con.cursor()
                cur.execute(self.lista)
                self.df = pd.read_sql(self.lista, con)
                try:
                    with open("rename_this.csv", "w") as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter="\t")
                        csv_writer.writerow([i[0] for i in cur.description])
                        csv_writer.writerows(cur)
                        csv_reader = csv.reader("rename_this.csv", delimiter=",")
                        line_count = 0
                        for row in csv_reader:
                            if line_count == 0:
                                line_count += 1
                            else:
                                line_count += 1
                        print(f"Processed {line_count} lines.")
                        dirpath = os.getcwd() + "/rename_this.csv"
                        text = "Data exported Successfully into {}".format(dirpath)
                        message = Messagebox()
                        message.info(text)
                except (
                    AttributeError,
                    ValueError,
                ) as e:
                    message = Messagebox()
                    message.critical(str(e))
        except sqlite3.OperationalError as e:
            message = Messagebox()
            message.critical(str(e))

    def new_window(self):
        self.process_current_test_list()
        print(self.lista)
        try:
            texto = self.lista
            self.Open = ResultSelect(texto)
            self.Open.show()
        except DatabaseError as e:
            message = Messagebox()
            message.critical(str(e))
