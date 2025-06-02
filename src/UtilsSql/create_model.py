from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt


def create_model(column):
    counter = len(column)
    while counter > 0:
        counter -= 1
        model = QStandardItemModel(1, 1)
        for i, area in enumerate(column):
            item = QStandardItem(area)
            item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
            item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
            model.setItem(i + 1, 0, item)
        return model
