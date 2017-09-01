import os
from .grid import Grid
from .piece import Piece
from .state_grid import StateGrid
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QPushButton, \
    QLabel
from PyQt5.QtCore import Qt, pyqtSignal

from .variables import variables
from random import choice

PATH = os.path.dirname(os.path.abspath(__file__))


class Game(QWidget):
    add_number_signal = pyqtSignal(tuple)
    pop_number_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.move(20, 20)
        self.hbox = QHBoxLayout()
        self.grid = Grid(self)
        self.vbox = QVBoxLayout()
        self.actual_piece = Piece("blank", self)
        self.rotate_button = QPushButton('Rotar', self)
        self.end_game_button = QPushButton('Terminar Juego', self)
        self.back_button = QPushButton('Retroceder', self)
        self.save_button = QPushButton('Guardar', self)
        self.state_grid = StateGrid(self)
        self.p1_points = QLabel(self)
        self.p2_points = QLabel(self)
        self.set_points(1, 0)
        self.set_points(2, 0)

    def initUi(self):
        self.setWindowTitle('Best Tarea Ever :P')
        self.setMouseTracking(True)
        self.setLayout(self.hbox)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.grid)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(1)
        self.grid.show()
        self.piece_layout = QHBoxLayout(self)
        self.piece_layout.addStretch(1)
        self.piece_layout.addWidget(self.actual_piece)
        self.piece_layout.addStretch(1)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.piece_layout)
        self.vbox.addStretch(1)
        hlayout = QHBoxLayout(self)
        self.vbox.addLayout(hlayout, 1)
        hlayout.addWidget(self.save_button, 1)
        hlayout.addWidget(self.rotate_button, 1)
        hlayout.addWidget(self.end_game_button, 1)
        hlayout.addWidget(self.back_button, 1)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.state_grid, 1)
        hlayout_points = QHBoxLayout(self)
        self.vbox.addLayout(hlayout_points, 1)
        self.p1_points.show()
        self.p2_points.show()
        hlayout_points.addWidget(self.p1_points)
        hlayout_points.addWidget(self.p2_points)
        self.rotate_button.clicked.connect(self.rotate_piece)
        self.back_button.clicked.connect(self.back_move)
        self.end_game_button.clicked.connect(self.end_game)
        self.save_button.clicked.connect(self.save_game)
        self.add_number_signal.connect(self.state_grid.add_number)
        self.pop_number_signal.connect(self.state_grid.pop_number)
        self.grid.initUI()
        self.new_piece()

    @staticmethod
    def back_move():
        variables.GAME_INTERFACE.retroceder()

    @staticmethod
    def end_game():
        variables.GAME_INTERFACE.terminar_juego()

    @staticmethod
    def save_game():
        variables.GAME_INTERFACE.guardar_juego()

    def add_number(self, number, color):
        self.add_number_signal.emit((number, color))

    def pop_number(self):
        self.pop_number_signal.emit()

    def new_piece(self, color=None, piece_type=None):
        if piece_type is None:
            piece_type = choice(variables.TYPES)
        if color is None and piece_type != "hint":
            color = choice(variables.COLORS)
        self.piece_layout.removeItem(self.piece_layout.itemAt(2))
        self.piece_layout.removeWidget(self.actual_piece)
        self.actual_piece.hide()
        self.actual_piece.deleteLater()
        self.actual_piece = Piece(piece_type, color, self)
        self.piece_layout.addWidget(self.actual_piece)
        self.piece_layout.addStretch(1)

    def addPiece(self, i, j, color=None, piece_type=None, on_move_ended=None):
        if piece_type is None:
            self.grid.addPiece(i, j, self.actual_piece, on_move_ended)
        elif piece_type == 'blank' or piece_type == 'hint':
            self.grid.addPiece(i, j, Piece(piece_type, color, self.grid))
        else:
            raise TypeError('No es un tipo valido')

    def getPiece(self, i, j):
        return self.grid.getPiece(i, j)

    def popPiece(self, i, j):
        pop_piece = self.grid.popPiece(i, j)
        self.addPiece(i, j, piece_type='blank')
        return pop_piece

    def movePiece(self, i, j, piece, on_move_end=None):
        self.grid.movePiece(i, j, piece, on_move_end)

    def set_points(self, player_numb, points):
        # self.label_puntaje.setText(str(points))
        if player_numb == 1:
            self.p1_points.setText("Jugador 1: {}".format(points))
        elif player_numb == 2:
            self.p2_points.setText("Jugador 2: {}".format(points))

    def rotate_piece(self):
        self.actual_piece.rotate()
        variables.GAME_INTERFACE.rotar_pieza('Derecha')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            variables.GAME_INTERFACE.save_game()
        elif event.key() == Qt.Key_H:
            variables.GAME_INTERFACE.hint_asked()
