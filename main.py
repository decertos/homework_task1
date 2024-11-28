import sys


from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from PyQt6 import uic

import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        conn = sqlite3.connect("coffee.sqlite")
        cur = conn.cursor()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки", "Молотый/в зёрнах",
                                                    "Описание вкуса", "Цена", "Объём упаковки"])
        for i, values in enumerate(cur.execute("""SELECT * FROM Coffee""").fetchall()):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, value in enumerate(values):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())