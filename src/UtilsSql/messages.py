import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt6 import QtCore


class Messagebox(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def info(self, text):
        QMessageBox.information(
            self,
            "Information",
            text,
        )

    def critical(self, e):
        QMessageBox.critical(
            self,
            "sqlite3.OperationalError",
            e,
        )

    def question(self):
        answer = QMessageBox.question(
            self,
            "Confirmation",
            "This requires restarting the \napplication.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.close()
            self.relaunch_application()
        else:
            self.close()

    def relaunch_application(self):
        QApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Messagebox()
    sys.exit(app.exec())
