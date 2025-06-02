from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget
import sys
from pathlib import Path


class OpenDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("PyQt File Dialog")
        self.setGeometry(100, 100, 600, 100)

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self, "Select a File", " ", ("sqlite3 (*.db);;All files (*.*)")
        )
        if filename:
            path = Path(filename)
            return path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OpenDialog()
    sys.exit(app.exec())
