import sqlite3
from PyQt6 import QtWidgets
import pandas as pd


class ConnectDb:
    def __init__(self):
        super(ConnectDb, self).__init__()
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
        from .utils import filename

        self.filename = filename
        self.tables = dict()
        self.allTables = dict()
        self.connect_db()

    def connect_db(self):
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tablerow in cursor.fetchall():
                    tableRow = tablerow[0]
                    cursor.execute("PRAGMA table_info('%s')" % tableRow)
                    names = cursor.fetchall()
                    self.columns = []
                    for i in names:
                        self.columns.append(i[1])
                    self.tables[tableRow] = self.columns
        except sqlite3.OperationalError as e:
            print(f"{e} :connect_db")

    def get_all_tables(self) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tablerow in cursor.fetchall():
                    tableRow = tablerow[0]
                    cursor.execute("PRAGMA table_info('%s')" % tableRow)
                    names = cursor.fetchall()
                    allTables = []
                    for i in names:
                        tupla = tuple()
                        tupla = (*tupla, i[1])
                        tupla = (*tupla, i[2])
                        allTables.append(tupla)
                    self.allTables[tableRow] = allTables
                return self.allTables
        except sqlite3.OperationalError as e:
            print(f"{e} :get_all_tables")

    def get_table_len(self) -> int:
        return len(self.tables)

    def get_list_all_pr(self, current_table) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tableRow in cursor.fetchall():
                    tableRow = tableRow[0]
                    cursor.execute("PRAGMA table_xinfo('%s')" % tableRow)
                    names = cursor.fetchall()
                    columns = []
                    for i in names:
                        columns.append(i[1])
                    self.tables[tableRow] = columns
                    listAllPr = []
                    for key, value in self.tables.items():
                        if key == current_table:
                            for item in value:
                                listAllPr.append("(" + key + "." + item + ")")
                    return listAllPr
        except sqlite3.OperationalError as e:
            print(f"{e} :get_list_all_pr")

    def get_list_count(self) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tableRow in cursor.fetchall():
                    tableRow = tableRow[0]
                    cursor.execute("PRAGMA table_xinfo('%s')" % tableRow)
                    names = cursor.fetchall()
                    columns = []
                    for i in names:
                        columns.append(i[1])
                    self.tables[tableRow] = columns
                    list_count = []
                    for key, value in self.tables.items():
                        for item in value:
                            list_count.append("(" + key + "." + item + ")")
                    return list_count
        except sqlite3.OperationalError as e:
            print(f"{e} :get_list_count")

    def get_list_all(self) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tableRow in cursor.fetchall():
                    tableRow = tableRow[0]
                    cursor.execute("PRAGMA table_xinfo('%s')" % tableRow)
                    names = cursor.fetchall()
                    columns = []
                    for i in names:
                        columns.append(i[1])
                    self.tables[tableRow] = columns
                    listAll = []
                    for key, value in self.tables.items():
                        for item in value:
                            listAll.append(key + "," + item)
                    return listAll
        except sqlite3.OperationalError as e:
            print(f"{e} :get_list_all")

    def get_all_references(self) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tableRow in cursor.fetchall():
                    tableRow = tableRow[0]
                    cursor.execute("PRAGMA table_xinfo('%s')" % tableRow)
                    names = cursor.fetchall()
                    columns = []
                    for i in names:
                        columns.append(i[1])
                    self.tables[tableRow] = columns
                    referencesAll = []
                    for key, value in self.tables.items():
                        for item in value:
                            referencesAll.append(key + " (" + item + ")")
                    return referencesAll
        except sqlite3.OperationalError as e:
            print(f"{e} :get_all_references")

    def get_list_fields(self) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tableRow in cursor.fetchall():
                    tableRow = tableRow[0]
                    cursor.execute("PRAGMA table_xinfo('%s')" % tableRow)
                    names = cursor.fetchall()
                    columns = []
                    for i in names:
                        columns.append(i[1])
                    self.tables[tableRow] = columns
                    setFields = set()
                    for value in self.tables.values():
                        for item in value:
                            setFields.add(item)
                    listFields = []
                    for item in setFields:
                        listFields.append(item)
                        listFields.sort()
                    return listFields
        except sqlite3.OperationalError as e:
            print(f"{e} :get_list_fields")

    def get_primary_key(self, current_text: str) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT oid FROM ('%s')" % current_text)
                field_names = [i[0] for i in cursor.description]
                return field_names
        except sqlite3.OperationalError as e:
            print(f"{e} :get_primary_key")

    def get_structure(self, currentText: str) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                anser = cursor.execute(
                    "SELECT sql  FROM sqlite_master WHERE type = 'table' AND tbl_name = '%s'"
                    % currentText
                )
                for tableRow in anser.fetchall():
                    tableRow = tableRow[0]
                    return tableRow
        except sqlite3.OperationalError as e:
            print(f"{e} :get_structure")

    def get_table_field(self, current_text: str) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                )
                for tableRow in cursor.fetchall():
                    tableRow = tableRow[0]
                    cursor.execute("PRAGMA table_xinfo('%s')" % tableRow)
                    names = cursor.fetchall()
                    columns = []
                    for i in names:
                        columns.append(i[1])
                    self.tables[tableRow] = columns
                    for key, value in self.tables.items():
                        for item in value:
                            if current_text == item:
                                return key
        except sqlite3.OperationalError as e:
            print(f"{e} :get_table_field")

    def get_fields_table(self, table: str) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM ('%s')" % table)
                field_names = [i[0] for i in cursor.description]
                return field_names
        except sqlite3.OperationalError as e:
            print(f"{e} :get_fields_table")

    def get_fields_table_by(self, table: str) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM ('%s')" % table)
                for tablerow in cursor.fetchall():
                    tableRow = tablerow[0]
                    cursor.execute("PRAGMA table_info('%s')" % tableRow)
                    names = cursor.fetchall()
                    self.columns = []
                    for i in names:
                        self.columns.append(i[1])
                    self.tables[tableRow] = self.columns
                    fields_list = []
                    for k, v in self.tables.items():
                        if k == table:
                            for item in v:
                                fields_list.append(k + "." + item)
                            return fields_list
        except sqlite3.OperationalError as e:
            print(f"{e} :get_fields_table_by")

    def get_data_column(self, table: str, field: str) -> str:
        try:
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT {} {}".format(field, table))
                resultQuery = cursor.fetchall()
                result = []
                for item in resultQuery:
                    item = str(item[0])
                    if '"' in item:
                        item = "'" + item + "'"
                        result.append(item)
                    else:
                        item = '"' + item + '"'
                        result.append(item)
                return result
        except (sqlite3.OperationalError, TypeError) as e:
            print(f"{e} :get_data_column")

    def get_data_sheet(self, currentTable: str) -> str:
        try:
            datasheet = "SELECT * FROM  {}".format(currentTable)
            with sqlite3.connect(self.filename) as conn:
                conn.row_factory = sqlite3.Row
                return pd.read_sql(datasheet, conn)
        except (sqlite3.OperationalError, TypeError) as e:
            print(f"{e} : get_data_sheet")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    connectdb = ConnectDb()
    sys.exit(app.exec_())
