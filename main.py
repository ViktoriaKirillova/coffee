import enum
import operator
import sys

from PyQt5.QtWidgets import *
import sqlite3

FILEPATH = "coffee.sqlite"
from main1 import Ui_Form
from addEditCoffeeForm import Ui_Dialog


def unwrap(data):
    return list(map(operator.itemgetter(0), data))


class Action(enum.Enum):
    Edit = 1
    Add = 2


class AddWidget(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_values(self, values):
        self.sort.setText(values[0])
        self.roast.setText(values[1])
        self.ground.setChecked(values[2])
        self.taste.setText(values[3])
        self.price.setValue(values[4])
        self.volume.setValue(values[5])

        return self

    def get_values(self):
        self.exec_()

        return self.sort.text(), self.roast.text(), self.ground.isChecked(), \
               self.taste.text(), self.price.value(), self.volume.value()


class AppWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect(FILEPATH)
        self.cur = self.db.cursor()

        self.setupUi(self)
        self.initUI()

    def __del__(self):
        self.db.close()

    def initUI(self):
        self.table.setRowCount(1)
        columns = unwrap(self.cur.execute("SELECT * FROM coffee").description)
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)

        self.bAdd.clicked.connect(lambda: self.action(Action.Add))
        self.bEdit.clicked.connect(lambda: self.action(Action.Edit))

        self.display_data()

    def action(self, action):
        if action == Action.Add:
            values = AddWidget().get_values()
            max_id = max(unwrap(self.cur.execute("SELECT ID FROM coffee").fetchall()))
            self.cur.execute(f"""INSERT INTO coffee VALUES 
            ({max_id + 1}, '{values[0]}', '{values[1]}', {int(values[2])}, '{values[3]}', {values[4]}, {values[5]})""")
            self.db.commit()
            self.display_data()
        elif action == Action.Edit:
            current_row = self.table.currentRow()
            values = [self.table.item(current_row, i).text() for i in range(7)]
            values[0] = int(values[0])
            values[3] = int(values[3])
            values[5] = float(values[5])
            values[6] = float(values[6])
            current_id = values[0]
            values = AddWidget().set_values(values[1:]).get_values()
            self.cur.execute(f"DELETE FROM coffee WHERE id = {current_id}")
            self.cur.execute(f"""INSERT INTO coffee VALUES 
            ({current_id}, '{values[0]}', '{values[1]}', {int(values[2])}, '{values[3]}', {values[4]}, {values[5]})""")
            self.db.commit()
            self.display_data()

    def display_data(self):
        request = "SELECT * FROM coffee"

        data = self.cur.execute(request).fetchall()
        self.table.setRowCount(len(data))
        for i, it in enumerate(data):
            for j, v in enumerate(it):
                self.table.setItem(i, j, QTableWidgetItem(str(v)))
        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    sys.excepthook = lambda cls, exception, traceback: sys.__excepthook__(cls, exception, traceback)

    app = QApplication([])
    wdg = AppWidget()
    wdg.show()
    sys.exit(app.exec_())
