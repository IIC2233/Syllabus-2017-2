from metaclases import MetaChess
from pieces import PiezaAjedrez

class Tablero(metaclass=MetaChess):

    def __init__(self):
        self.tablero = []
        self.__init_tablero()

    def __init_tablero(self):
        for i in range(8):
            self.tablero.append(["-"] * 8)

    def add_piece(self, piece, moving=False):
        if not self.validate_letter(piece.letter):
            print("No es una letra valida")
        elif not self.validate_number(piece.number) :
            print("Numero ingresado no es correcto")
        elif not isinstance(piece, PiezaAjedrez):
            print("No ingresaste una pieza")
        else:
            if not moving:
                for row in self.tablero:
                    for old_piece in row:
                        if id(old_piece) == id(piece):
                            print("La pieza {} "
                                  "ya existe en el tablero".format(
                                piece.nombre))
                            return
            j = "abcdefgh".find(piece.letter.lower())
            i = 8 - piece.number
            self.tablero[i][j] = piece

    def get_piece(self, letter, number):
        if not self.validate_letter(letter):
            print("No es una letra valida")
        elif not self.validate_number(number) :
            print("Numero ingresado no es correcto")
        else:
            j = "abcdefgh".find(letter.lower())
            i = 8 - number
            return self.tablero[i][j]

    def row_elements(self, i):
        return [str(j) for j in self.tablero[i]]

    def __repr__(self):
        string = "\t\tA\t\tB\t\tC\t\tD\t\tE\t\tF\t\tG\t\tH\n"
        for i in range(len(self.tablero)):
            string += "{}\t\t{}\n".format(8 - i,
                                          "\t\t".join(self.row_elements(i)))
        return string

    def move_piece(self, *args):
        i, j, x, y = args[:4]
        if not self.validate_letter(i) or not self.validate_number(j):
            print("Coordenadas de inicio incorrectas")
        elif not self.validate_letter(x) or not self.validate_number(y):
            print("Coordenadas finales incorrectas")
        elif isinstance(self.get_piece(i, j), str):
            print("No hay pieza en las coordenas iniciales")
        elif not self.get_piece(i, j).valid_move(x, y):
            print("La pieza {} no puede "
                  "realizar ese movimiento".format(
                self.get_piece(i, j).nombre))
        elif not self.valid_move(i, j, x, y):
            print("Hay una pieza en el camino de {}".format(
                self.get_piece(i, j).nombre))
        else:
            initial_space = self.get_piece(i, j)
            final_space = self.get_piece(x, y)
            if isinstance(final_space, PiezaAjedrez):
                print("Te has comido a {}".format(final_space))
            initial_space.new_pos(x, y)
            self.add_piece(initial_space, True)
            self.remove_piece(i, j)
            print("Has movido correctamente {} a {}".format(initial_space,
                                                            (x, y)))
            print(self)

    def valid_move(self, i, j, x, y):
        return True

    def remove_piece(self, letter, number):
        if not self.validate_letter(letter):
            print("No es una letra valida")
        elif not self.validate_number(number) :
            print("Numero ingresado no es correcto")
        else:
            j = "abcdefgh".find(letter.lower())
            i = 8 - number
            self.tablero[i][j] = "-"

    def __call__(self, *args, **kwargs):
        print(self)

    @staticmethod
    def validate_letter(letter):
        return isinstance(letter, str) and letter.lower() in "abcdefgh"

    @staticmethod
    def validate_number(number):
        return isinstance(number, int) and 0 < number < 9

