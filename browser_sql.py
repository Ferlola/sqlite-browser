import sys
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QDialog,
    QTabWidget,
    QPushButton,
    QHBoxLayout,
)
from src.SelectSql.select_sql import Select
from src.InsertSql.insert_sql import Insert
from src.UpdateSql.update_sql import Update
from src.AlterSql.alter_sql import Alter
from src.CreateSql.create_sql import Create
from src.DropSql.drop_sql import Drop
from src.CreateDb.create_db import CreateDb
from src.DataSheetSql.table_data_sql import DataSheet
from src.UtilsSql.get_any_table import get_any_table


class MyApp(QDialog):
    """
    Ventana principal de la aplicación DB Browser for SQLite.
 
    Muestra dos botones iniciales para que el usuario elija entre
    crear una nueva base de datos o abrir una existente. Según la
    elección, construye dinámicamente las pestañas correspondientes.
    """
    def __init__(self):
        """Inicializa la ventana principal y muestra los botones de inicio."""
        super().__init__()
        self.createButtons()

    def createTab(self):
        """
        Muestra únicamente la pestaña 'CREATE DB'.

        Se usa cuando no hay una base de datos seleccionada y el usuario
        quiere crear una nueva.
        """
        self.vbox.removeWidget(self.create_button)
        self.create_button.deleteLater()
        self.create_button = None
        self.vbox.removeWidget(self.search_button)
        self.search_button.deleteLater()
        self.search_button = None
        tabs = QTabWidget()
        tabs.addTab(CreateDb(), "CREATE DB")
        self.vbox.addWidget(tabs)
        self.setLayout(self.vbox)
        self.setGeometry(10, 10, 950, 100)
        self.show()

    def createTabs(self):
        """
        Construye y muestra todas las pestañas de la aplicación.

        Si la base de datos seleccionada no tiene tablas, solo muestra
        la pestaña 'CREATE TABLE'. En caso contrario, carga todas las
        pestañas disponibles (SELECT, INSERT, UPDATE, etc.).
        """
        self.vbox.removeWidget(self.create_button)
        self.create_button.deleteLater()
        self.create_button = None
        self.vbox.removeWidget(self.search_button)
        self.search_button.deleteLater()
        self.search_button = None
        tabs = QTabWidget()
        if not get_any_table():
            tabs.addTab(Create(), "CREATE TABLE")
            self.setGeometry(10, 10, 950, 700)
        else:
            tabs.addTab(Select(), "SELECT")
            tabs.addTab(Insert(), "INSERT INTO")
            tabs.addTab(Update(), "UPDATE")
            tabs.addTab(Alter(), "ALTER TABLE")
            tabs.addTab(Create(), "CREATE TABLE")
            tabs.addTab(Drop(), "DROP TABLE, DELETE FROM")
            tabs.addTab(DataSheet(), "DATA SHEET")
            tabs.addTab(CreateDb(), "CREATE DB")
            self.setGeometry(10, 10, 950, 700)
        self.vbox.addWidget(tabs)
        self.setLayout(self.vbox)
        self.show()

    def createButtons(self):
        """
        Construye el layout inicial con los botones 'Create DATABASE'
        y 'Search DATABASE', centrados horizontalmente en la ventana.
        """
        self.create_button = QPushButton("Create DATABASE")
        self.search_button = QPushButton("Search DATABASE")
        self.create_button.setFixedWidth(200)
        self.search_button.setFixedWidth(200)
        
        self.create_button.clicked.connect(self.createTab)
        self.search_button.clicked.connect(self.search)
        
        # Layout horizontal con stretch para centrar los botones
        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.vbox = QVBoxLayout()
        self.hbox.addWidget(self.create_button)
        self.hbox.addWidget(self.search_button)
        self.hbox.addStretch()
        
        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)
        
        self.setGeometry(10, 10, 600, 100)
        self.show()

    def search(self):
        """
        Gestiona la acción del botón 'Search DATABASE'.

        Si ya hay un archivo de base de datos seleccionado en utils,
        carga todas las pestañas y actualiza el título de la ventana.
        Si no hay ninguno seleccionado, muestra solo la pestaña 'CREATE DB'
        para que el usuario pueda crear una base de datos nueva.
        """
        from src.UtilsSql import utils

        if utils.filename:
            self.createTabs()
            self.setWindowTitle(str(utils.filename))
            return utils.filename
        else:
            self.createTab()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("FUSION")
    ex = MyApp()
    sys.exit(app.exec())
