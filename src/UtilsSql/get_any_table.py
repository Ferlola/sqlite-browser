import sqlite3


def get_any_table():
    try:
        from src.UtilsSql.utils import filename

        con = sqlite3.connect(filename)
        cursor = con.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        )
        anyTable = cursor.fetchall()
        return anyTable
    except (AttributeError, RuntimeError) as e:
        print(f"{e} :getAnyTable")
