"""
Copyright (c) 2017, Bad Bunny (el 🐰 malo)
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.

Nota: el código no está tan pitonesco como quisiera.
"""

from collections import namedtuple
import itertools
import random
import string

PLAYER_ONE = 'P1'
PLAYER_TWO = 'P2'
VOID_SYMBOL = '-'
SHIP_SYMBOL = 'O'
MISS_SYMBOL = '@'
HIT_SYMBOL = 'X'

Player = namedtuple('Player', ['board', 'ships', 'attacks'])


def checker(_get_set_square):
    def wrapper(self, square, *args):
        if not self.is_valid_square(square):
            message = '{} es una casilla inválida.'
            raise Exception(message.format(square))
        return _get_set_square(self, square, *args)
    return wrapper


class Battleship:
    """
    Esta clase representa el juego con ambos jugadores.
    """

    def __init__(self, boardsize=5, max_ships=9, loaded=False):
        """
        Inicializador de una batalla naval con dos jugadores.

        :boardsize <int> --> tamaño de cada tablero
        :max_ships <int> --> número máximo de barcos permitidos por jugador
        :loaded   <bool> --> si es True, asignará los barcos aleatoriamente
        """

        self.players = {
            PLAYER_ONE: Player(Board(boardsize, max_ships),
                               set(), set()),
            PLAYER_TWO: Player(Board(boardsize, max_ships),
                               set(), set())
        }

        if loaded:
            for player in self.players:
                squares = self._get_random_squares(boardsize, max_ships)
                self.add_ships(player, squares)

    @property
    def p1(self):
        """
        Devuelve al primer jugador.
        """

        return self.players[PLAYER_ONE]

    @property
    def p2(self):
        """
        Devuelve al segundo jugador.
        """

        return self.players[PLAYER_TWO]

    def add_ships(self, player, squares):
        """
        Agrega barcos al tablero de un jugador.

        :player <str>   --> identificador del jugador (e.g. 'P1')
        :squares <list> --> lista con casilleros      (e.g. ['a3', 'd2'])
        """

        self.players[player].ships.update(squares)
        self.players[player].board.add_ships(squares)

    def attack(self, player, square):
        """
        Dado un jugador y una casilla, provoca un ataque.

        :player <str> --> el jugador atacante (e.g. 'P2')
        :square <str> --> la casilla atacada  (e.g. 'b4')
        """

        if square in self.players[player].attacks:
            message = 'Ya existe un ataque en {}.'
            raise Exception(message.format(square))

        self.players[player].attacks.add(square)
        return self._get_enemy_board(player).attacked_on(square)

    def view_from(self, player):
        """
        Devuelve los dos tableros vistos desde un mismo jugador:
        - el primer tablero es el propio (con sus barcos, hundidos o no)
        - el segundo tablero muestra los ataques realizados (fallidos o no)

        :player <str> --> jugador que recibirá sus dos tableros (e.g. 'P2')
        """

        print('Mirando desde {}:'.format(player))
        print('======= ===== ===\n')

        my_title = ('Mi tablero\n'
                    '-- -------\n')
        my_board = self.players[player].board

        enemy_board = self._get_enemy_board(player).hidden()
        enemy_title = ('Tablero enemigo\n'
                       '------- -------\n')

        return '\n'.join([my_title, str(my_board), '\n',
                          enemy_title, str(enemy_board)])

    def game_over(self):
        """
        Devuelve un booleano que indica si la partida finalizó.
        """

        return self.p1.board.has_no_ships() or self.p2.board.has_no_ships()

    def get_winner(self):
        """
        Devuelve, como string, el nombre del ganador de la partida.
        Y si todavía no existe un bando victorioso, entregará None.
        """

        if self.p1.board.has_no_ships(): return PLAYER_TWO
        if self.p2.board.has_no_ships(): return PLAYER_ONE
        return None

    # Private API
    # ======= ===

    def _get_enemy_board(self, player):
        enemy = 'P{}'.format(3 - int(player[1]))  # (P1, P2) <--> (P2, P1)
        return self.players[enemy].board

    @staticmethod
    def _get_random_squares(size, how_many):
        product = itertools.product(string.ascii_lowercase[:size], range(size))
        squares = [file + str(rank + 1) for (file, rank) in product]
        return random.sample(squares, how_many)


class Board:
    """
    La terminología fue obtenida principalmente del ajedrez.
    Más información en <https://en.wikipedia.org/wiki/Chess>
    """

    def __init__(self, size, max_ships):
        self.board = [[VOID_SYMBOL] * size for _ in range(size)]
        self.max_ships = max_ships
        self.size = size

        # Jesus Christ, this is so meta...
        for file in string.ascii_lowercase[:size]:
            for rank in range(size):
                self._add_property(file + str(rank + 1))

    def add_ships(self, squares):
        for square in squares:
            self._set_square(square, SHIP_SYMBOL)

    def attacked_on(self, square):
        new_value = HIT_SYMBOL if self._has_ship_on(square) else MISS_SYMBOL
        self._set_square(square, new_value)
        return new_value

    def has_no_ships(self):
        return not self._how_many_ships()

    def is_valid_square(self, square):
        file, rank = self._to_indices(square)
        return (0 <= file < self.size) and (0 <= rank < self.size)

    def hidden(self):
        hidden = [[square.replace(SHIP_SYMBOL, VOID_SYMBOL)
                   for square in rank] for rank in self.board]
        return self._board_to_ascii(hidden)

    def __str__(self):
        return self._board_to_ascii(self.board)

    # Private API
    # ======= ===

    def _add_property(self, square):
        fget = lambda self:        self._get_square(square)
        fset = lambda self, value: self._set_square(square, value)

        setattr(self.__class__, square, property(fget, fset))

    @checker
    def _get_square(self, square):
        file, rank = self._to_indices(square)
        return self.board[rank][file]

    @checker
    def _set_square(self, square, value):
        if value != SHIP_SYMBOL or self._how_many_ships() < self.max_ships:
            file, rank = self._to_indices(square)
            self.board[rank][file] = value
        else:
            message = 'No puedes colocar más de {} barcos.'
            raise Exception(message.format(self.max_ships))

    def _has_ship_on(self, square):
        return self._get_square(square) == SHIP_SYMBOL

    def _how_many_ships(self):
        return sum(rank.count(SHIP_SYMBOL) for rank in self.board)

    def _board_to_ascii(self, board):
        prepend_index = lambda index, rank: [str(index + 1)] + rank
        board = [prepend_index(*rank) for rank in enumerate(board)]
        board.insert(0, ' ' + string.ascii_lowercase[:self.size])

        return '\n'.join(map('  '.join, reversed(board)))

    @staticmethod
    def _to_indices(square):
        return ord(square[0]) - 97, int(square[1]) - 1
