from pieces import PiezaAjedrez, Peon, Caballo, Alfil, Rey, Reina, Torre
from chessboard import Tablero

def init_tab():
    """
    Esta funcion creara todas las piezas, luego comprobara que en fake_pieces
    solo existan piezas que estan en pieces, ya que estas se instanciaron
    cuando un juegador ya tenia todas las piezas de un color listas

    :return: pieces, que son las piezas que se agregaran al tablero
    """
    pieces = []
    fake_pieces = []
    for i in range(8):
        pos_1 = (chr(i + 65), 2)
        pos_2 = (chr(i + 65), 7)
        pieces.append(Peon(*pos_1))
        pieces.append(Peon(*pos_2, allied=False))
    pieces.append(Alfil("C", 1))
    pieces.append(Alfil("C", 8))
    fake_pieces.append(Alfil("E", 1))
    pieces.append(Alfil("F", 1, allied=False))
    pieces.append(Alfil("F", 8, allied=False))
    pieces.append(Torre("A", 1))
    pieces.append(Torre("A", 8))
    fake_pieces.append((Torre("E", 1)))
    pieces.append(Torre("H", 1, allied=False))
    pieces.append(Torre("H", 8, allied=False))
    pieces.append(Caballo("B", 1))
    pieces.append(Caballo("B", 8))
    fake_pieces.append(Caballo("E", 1))
    pieces.append(Caballo("G", 1, allied=False))
    pieces.append(Caballo("G", 8, allied=False))
    pieces.append(Rey("D", 1))
    fake_pieces.append(Rey("E", 8))
    pieces.append(Rey("D", 8, allied=False))
    pieces.append(Reina("E", 1))
    fake_pieces.append(Reina("D", 1))
    pieces.append(Reina("E", 8, allied=False))
    for piece in fake_pieces:
        if piece not in pieces:
            print("La pieza {} no respeto "
                  "el numero máximo de piezas de un mismo color".format(
                piece.nombre))
    return pieces


if __name__ == "__main__":
    # No se deberia instanciar
    tablero_1 = Tablero()
    # deberia tirar un error
    try:
        tablero_1()
    except TypeError:
        print("Felicitaciones no se instancio el tablero")

    # Luego de esto no se deberia impirmir nada
    pieces = init_tab()

    # Si se deberia instanciar el tablero con todas las piezas en él
    tablero_1 = Tablero(*pieces)
    tablero_1()

    # Las siguientes piezas deberian retornar alguna ya existente
    # en el pieces y no crear una nueva:
    peon = Peon("A", 5)
    alfil = Alfil("B", 5)
    rey = Rey("C", 5)
    reina = Reina("D", 5)
    torre = Torre("E", 5)
    caballo = Caballo("F", 5)

    # Por lo anterior los siguientes comandos
    # deberian imprimir "Esta pieza ya existe en el tablero"
    tablero_1.add_piece(peon)
    tablero_1.add_piece(alfil)
    tablero_1.add_piece(rey)
    tablero_1.add_piece(reina)
    tablero_1.add_piece(torre)
    tablero_1.add_piece(caballo)

    # Estos movmientos si se deberian ejecutar
    tablero_1.move_piece("B", 2, "B", 3)
    tablero_1.move_piece("C", 2, "C", 3)
    tablero_1.move_piece("B", 8, "C", 6)

    # No se deberia realizar ninguno de estos movimientos
    # movimiento del caballo
    tablero_1.move_piece("B", 1, "B", 4)
    # movimiento de la torre
    tablero_1.move_piece("A", 1, "B", 2)
    # movimiento del alfil
    tablero_1.move_piece("C", 1, "C", 2)
    # movimiento del peon
    tablero_1.move_piece("H", 2, "E", 6)
    # movimiento de la reina
    tablero_1.move_piece("E", 1, "F", 3)
    # movimiento del rey
    tablero_1.move_piece("D", 8, "D", 6)

    # No se deberia poder pasar por sobre una pieza
    tablero_1.move_piece("H", 8, "H", 6)
    tablero_1.move_piece("E", 1, "E", 3)

    # Esto deberia mostrar el mismo tablero
    tablero_1 = Tablero()
    tablero_1()
