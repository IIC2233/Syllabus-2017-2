from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from .piece import Piece
from .variables import variables

class Deploy(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(200, 200)

        self.show()
        vlayout = QVBoxLayout(self)
        piece = Piece("red", self)
        vlayout.addWidget(piece)

        vlayout.addLayout(hlayout)
        self.rotate_button = QPushButton('rotar', self)
        self.discard_button = QPushButton('descartar', self)
        self.select_button = QPushButton('seleccionar', self)
        hlayout.addWidget(self.rotate_button, 1)
        hlayout.addWidget(self.discard_button, 1)
        hlayout.addWidget(self.select_button, 1)


