from PyQt5.QtWidgets import QApplication
from .game_interface import GameInterface
from .variables import variables
from .game import Game

__game = None
""" :type: Game"""

__app = None


def set_quality(quality):
    if quality in ["low", "medium", "high", "ultra"]:
        variables.QUALITY = quality
    else:
        raise Exception("Valores validos: low, medium, high y ultra")


def set_animations(animations):
    if isinstance(animations, bool):
        variables.ANIMATIONS = animations
    else:
        raise TypeError("bool expected")


def set_scale(scale):
    if (isinstance(scale, float) or isinstance(scale, int)) and not isinstance(
            scale, bool):
        variables.SCALE = scale
    elif isinstance(scale, bool) and not scale:
        pass
    else:
        raise TypeError("float expected")


def set_points(player_numb, points):
    __game.set_points(player_numb, points)


def add_piece(i, j, color=None, piece_type=None, on_move_ended=None):
    __game.addPiece(i, j, color, piece_type, on_move_ended)


def get_piece(i, j):
    return __game.getPiece(i, j)


def pop_piece(i, j):
    return __game.popPiece(i, j)


def add_number(number, color):
    return __game.add_number(number, color)


def pop_number():
    return __game.pop_number()


def move_piece(i, j, piece, on_move_ended=None):
    __game.movePiece(i, j, piece, on_move_ended)


def nueva_pieza(color=None, piece_type=None):
    __game.new_piece(color, piece_type)


def add_hint(i, j):
    __game.addPiece(i, j, piece_type='hint')


def set_game_interface(_game_interface):
    if isinstance(_game_interface, GameInterface):
        variables.GAME_INTERFACE = _game_interface
    else:
        raise TypeError("GameInterface class expected")


def init_grid():
    for i in range(variables.SIZE):
        for j in range(variables.SIZE):
            add_piece(i, j, piece_type='blank')


def init():
    global __game, __app
    __app = QApplication([])
    __screen_resolution = __app.desktop().screenGeometry()
    __width = __screen_resolution.width()
    variables.SCALE = __width / 1920
    __game = Game()
    __game.initUi()


def run():
    global __game, __app
    __game.show()
    __app.exec()
