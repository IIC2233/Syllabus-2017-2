import math
import os
import random
import sip
from math import ceil

from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QTimer
from .variables import variables
from math import sqrt

PATH = os.path.dirname(os.path.abspath(__file__))


class Piece(QWidget):
    def __init__(self, type, color=None, parent=None):
        super().__init__(parent)
        self.angle = 0
        self._type = type
        self._color = color
        self.setFixedSize(101 * variables.SCALE, 91 * variables.SCALE)
        self.__section = 7
        self.main_label = QLabel(self)
        self._pixmap = None
        self._selected_pixmap = None
        self.__timer = None
        self.__selected = False
        self.setMouseTracking(True)
        self.main_label.setMouseTracking(True)
        self.__init_main_label()

    def __init_main_label(self):
        if not self._color:
            self._original = QPixmap(
                PATH + os.sep + "assets" + os.sep + "{}.png".format(
                    self._type)).scaled(
                100 * variables.SCALE, 100 * variables.SCALE,
                Qt.KeepAspectRatio)
            self._selected_pixmap = QPixmap(
                PATH + os.sep + "assets" + os.sep + "{}.png".format(
                    self._type)).scaled(
                100 * variables.SCALE, 100 * variables.SCALE,
                Qt.KeepAspectRatio)
        else:
            self._original = QPixmap(
                PATH + os.sep + "assets" + os.sep + "{}".format(
                    self._color) + os.sep + "{}.png".format(
                    self._type)).scaled(100 * variables.SCALE,
                                        100 * variables.SCALE,
                                        Qt.KeepAspectRatio)
            self._selected_pixmap = QPixmap(
                PATH + os.sep + "assets" + os.sep + "{}".format(
                    self._color) + os.sep + "{}.png".format(
                    self._type)).scaled(100 * variables.SCALE,
                                        91 * variables.SCALE,
                                        Qt.KeepAspectRatio)
        self._pixmap = self._original
        self.main_label.setPixmap(self._pixmap)
        self.main_label.setGeometry(
            (101 - 100 * sqrt(2)) * variables.SCALE / 2,
            (93 - 100 * sqrt(2)) * variables.SCALE / 2,
            100 * sqrt(2) * variables.SCALE, 100 * sqrt(2) * variables.SCALE)
        self.main_label.show()
        self.main_label.setMouseTracking(True)
        self.main_label.setAlignment(Qt.AlignCenter)

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, value):
        self.__set_selected(value)

    def rotate(self):
        self.angle += 60
        self._pixmap = self._original
        self._pixmap = self._pixmap.transformed(
            QTransform().rotate(self.angle))
        self.main_label.setPixmap(self._pixmap)
        self.main_label.setGeometry(
            (100 - 100 * sqrt(2)) * variables.SCALE / 2,
            (93 - 100 * sqrt(2)) * variables.SCALE / 2,
            100 * sqrt(2) * variables.SCALE, 100 * sqrt(2) * variables.SCALE)

        self.main_label.setAlignment(Qt.AlignCenter)

    def update_state(self):
        self._pixmap = self._original
        self._pixmap = self._pixmap.transformed(
            QTransform().rotate(self.angle))
        self.main_label.setPixmap(self._pixmap)
        self.main_label.setGeometry(
            (100 - 100 * sqrt(2)) * variables.SCALE / 2,
            (93 - 100 * sqrt(2)) * variables.SCALE / 2,
            100 * sqrt(2) * variables.SCALE, 100 * sqrt(2) * variables.SCALE)
        self.main_label.setAlignment(Qt.AlignCenter)

    def __set_selected(self, selected):
        self.__selected = selected
        if selected:
            self.main_label.setPixmap(self._selected_pixmap)
        else:
            self.main_label.setPixmap(self._pixmap)

    def leaveEvent(self, event):
        self.__section = 7

    def mousePressEvent(self, QMouseEvent):
        try:
            self.parent().pieceClickedSignal.emit(
                PieceClickedEvent(self.column, self.row))
        except AttributeError:
            pass
        finally:
            QMouseEvent.accept()

    def animated_move(self, final_pos, on_move_end=None):
        if variables.ANIMATIONS:
            if self.__timer is None:
                self.__timer = MovePieceTimer(self, final_pos, self.parent(),
                                              on_move_end)
                self.__timer.start()
            else:
                if not sip.isdeleted(self.__timer):
                    self.__timer.deleteLater()
                self.__timer = MovePieceTimer(self, final_pos, self.parent(),
                                              on_move_end)
                self.__timer.start()
        else:
            self.move(*final_pos)


class PieceClickedEvent:
    def __init__(self, column, i):
        self.column = column
        self.row = i


class RotateEvent:
    def __init__(self, piece):
        self.piece = piece


class MovePieceTimer(QTimer):
    def __init__(self, hexagon, final_pos, parent=None, on_move_end=None):
        super().__init__(parent)
        self.hexagon = hexagon
        self.delta_x = final_pos[0] - self.hexagon.x()
        self.delta_y = final_pos[1] - self.hexagon.y()
        self.first_x = hexagon.x()
        self.first_y = hexagon.y()
        self.ticks = 0
        self.on_move_end = on_move_end
        self.timeout.connect(self.tick)

    def start(self, p_int=None):
        if p_int is None:
            super().start(variables.TICKS_INTERVAL[variables.QUALITY])
        else:
            super().start(p_int)

    def tick(self):
        if self.ticks <= variables.TOTAL_TICKS[
            variables.QUALITY] and not sip.isdeleted(self.hexagon):
            new_x = self.first_x + (self.delta_x * (
                self.ticks / variables.TOTAL_TICKS[variables.QUALITY]))
            new_y = self.first_y + (self.delta_y * (
                self.ticks / variables.TOTAL_TICKS[variables.QUALITY]))
            self.hexagon.move(new_x, new_y)
            self.ticks += 1
        else:
            self.deleteLater()
            self.hexagon.timer = None
            if self.on_move_end is not None:
                self.on_move_end()
