from .variables import variables
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QVBoxLayout, \
    QScrollArea, QLabel
from PyQt5.QtGui import QPixmap, QTextDocument
from PyQt5.QtCore import pyqtSignal, Qt
import os

PATH = os.path.dirname(os.path.abspath(__file__))


class StateGrid(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = QWidget(self)
        self.scroll_area = QScrollArea(self)
        self.vbox = QVBoxLayout(self)
        self.rows = []
        self.new_row()
        self.init_grid()

    def new_row(self):
        size = len(self.vbox)
        hbox = QHBoxLayout(self)
        self.vbox.addLayout(hbox, 1)
        if len(self.vbox) == size:
            hbox = QHBoxLayout(self)
            self.vbox.addLayout(hbox, 1)
        self.rows.append(hbox)

    def add_number(self, number_color):
        number, color = number_color
        if len(self.rows) == 0 or len(self.rows[-1]) >= 7:
            self.new_row()
        new_number = Number(self.scroll_area, number, color)
        new_number.number_clicked_signal.connect(self.on_number_clicked)
        self.rows[-1].addWidget(new_number)

    def pop_number(self):
        item = self.rows[-1].itemAt(len(self.rows[-1]) - 1)
        number = item.widget()
        self.rows[-1].removeItem(item)
        number.hide()
        number.deleteLater()
        if len(self.rows[-1]) == 0:
            self.vbox.removeItem(self.rows[-1])
            self.rows.pop()

    def init_grid(self):
        self.setFixedSize(400 * variables.SCALE, 500 * variables.SCALE)
        self.scroll_area.setFixedSize(400 * variables.SCALE,
                                      500 * variables.SCALE)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.central_widget.setLayout(self.vbox)
        self.scroll_area.setWidget(self.central_widget)
        self.scroll_area.setWidgetResizable(True)

    def on_number_clicked(self, number):
        variables.GAME_INTERFACE.click_number(number)


class Number(QWidget):
    number_clicked_signal = pyqtSignal(str)

    def __init__(self, parent, number, color):
        super().__init__(parent)
        if color == "red":
            text_color = "#ffffff"
        else:
            text_color = "#f9c31f"
        self.main_label = QLabel(self)
        self.number_label = QLabel(self)
        self.number_label.setText('<html><head/><body><p align="center">'
                                  '<span style=" font-size:12pt; '
                                  'font-weight:600; '
                                  'color:{};">'
                                  '{}'
                                  '</span>'
                                  '</p></body></html>'.format(text_color,
                                                              number))
        self.main_label.setFixedSize(35 * variables.SCALE,
                                     35 * variables.SCALE)
        self.number_label.setFixedSize(34 * variables.SCALE,
                                       34 * variables.SCALE)
        self.setFixedSize(35 * variables.SCALE, 35 * variables.SCALE)
        pixmap = QPixmap(
            PATH + os.sep + "assets" + os.sep + "{}_circle.png".format(color)
        ).scaled(35 * variables.SCALE, 35 * variables.SCALE)
        self.main_label.setPixmap(pixmap)
        self.main_label.setMouseTracking(True)
        self.number_label.setMouseTracking(True)
        self.setMouseTracking(True)
        self.show()

    def mousePressEvent(self, QMouseEvent):
        try:
            doc = QTextDocument()
            doc.setHtml(self.number_label.text())
            self.number_clicked_signal.emit(doc.toPlainText())
        except AttributeError:
            pass
        finally:
            QMouseEvent.accept()


if __name__ == "__main__":
    app = QApplication([])
    game = StateGrid()
    game.show()
    app.exec()
