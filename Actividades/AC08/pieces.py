from metaclases import MetaPiece

class PiezaAjedrez:
    def __init__(self, letter, number, allied=True):
        self.letter = letter
        self.number = number
        self.allied = allied

    def valid_move(self, letter, number):
        return True

    def new_pos(self, letter, number):
        self.letter = letter
        self.number = number

    def piece_path(self, i, j):
        return i, True, j


class Peon(PiezaAjedrez, metaclass=MetaPiece):
    def __init__(self, letra, num, allied=True):
        super().__init__(letra, num, allied)
        self.nombre = "Peon"

    def valid_move(self, letter, number):
        if letter.lower() != self.letter.lower():
            print("Error 1")
            return False
        elif abs(number - self.number) > 1:
            print("Error 2")
            return False
        else:
            return True

    def __repr__(self):
        return "P"


class Caballo(PiezaAjedrez, metaclass=MetaPiece):
    def __init__(self, letra, num, allied=True):
        super().__init__(letra, num, allied)
        self.nombre = "Caballo"

    def valid_move(self, letter, number):
        x = ord(self.letter.upper()) - 65
        op_1 = chr(x + 67)  # +2
        op_2 = chr(x + 63)  # -2

        if letter.lower() == op_2.lower() and (number == self.number - 1
                                               or number == self.number + 1):
            return True
        elif letter.lower() == op_1.lower() and (number == self.number - 1
                                                 or number == self.number + 1):
            return True

        elif letter == chr(x + 64) and (number == self.number + 2
                                        or number == self.number - 2):
            return True
        elif letter == chr(x + 66) and (number == self.number + 2
                                        or number == self.number - 2):
            return True
        elif letter.lower() == self.letter.lower():
            print("No estas moviendo la pieza {}".format(self.nombre))
        else:
            return False

    def __repr__(self):
        return "C"


class Torre(PiezaAjedrez, metaclass=MetaPiece):
    def __init__(self, letra, num, allied=True):
        super().__init__(letra, num, allied)
        self.nombre = "Torre"

    def valid_move(self, letter, number):
        if self.letter != letter and number != self.number:
            return False
        elif self.letter == letter and number == self.number:
            return False
        return True

    def piece_path(self, i, j):
        if self.letter == i and self.number < j:
            return i, "num", self.number + 1
        elif self.letter == i and self.number > j:
            return i, "num", self.number - 1
        elif self.number == j and ord(self.letter) - 65 > ord(i) - 65:
            x = ord(self.letter) - 65
            return chr(x + 66), "let", j
        elif self.number == j and ord(self.letter) - 65 < ord(i) - 65:
            x = ord(self.letter) - 65
            return chr(x + 64), "let", j

    def __repr__(self):
        return "T"


class Alfil(PiezaAjedrez, metaclass=MetaPiece):
    def __init__(self, letra, num, allied=True):
        super().__init__(letra, num, allied)
        self.nombre = "Alfil"

    def valid_move(self, letter, number):
        if abs(ord(self.letter) - ord(letter)) == abs(self.number - number):
            return True
        return False

    def piece_path(self, i, j):  # letra, numero
        x = ord(self.letter.upper()) - 65
        if ord(i) < x:
            if j > self.number:
                return i, "num", self.number + 1
            elif j < self.number:
                return i, "num", self.number - 1

        elif ord(i) > x:
            if j > self.number:
                return i, "let", self.number + 1
            elif j < self.number:
                return i, "let", self.number - 1

    def __repr__(self):
        return "A"


class Reina(PiezaAjedrez, metaclass=MetaPiece):
    def __init__(self, letra, num, allied=True):
        super().__init__(letra, num, allied)
        self.nombre = "Reina Flo"

    def valid_move(self, letter, number):
        if abs(ord(self.letter) - ord(letter)) == abs(self.number - number):
            return True
        elif self.letter == letter and self.number != number:
            return True
        elif self.number == number and self.letter != letter:
            return True
        else:
            return False

    def piece_path(self, i, j):
        x = ord(self.letter.upper()) - 65
        if self.letter == i and self.number < j:
            return i, "num", self.number + 1
        elif self.letter == i and self.number > j:
            return i, "num", self.number - 1
        elif self.number == j and ord(self.letter) - 65 > ord(i) - 65:
            x = ord(self.letter) - 65
            return chr(x + 66), "let", j
        elif self.number == j and ord(self.letter) - 65 < ord(i) - 65:
            x = ord(self.letter) - 65
            return chr(x + 64), "let", j

        elif ord(i) < x:
            if j > self.number:
                return i, "num", self.number + 1
            elif j < self.number:
                return i, "num", self.number - 1
        elif ord(i) > x:
            if j > self.number:
                return i, "let", self.number + 1
            elif j < self.number:
                return i, "let", self.number - 1

    def __repr__(self):
        return "F"


class Rey(PiezaAjedrez, metaclass=MetaPiece):
    def __init__(self, letra, num, allied=True):
        super().__init__(letra, num, allied)
        self.nombre = "Rey"

    def valid_move(self, letter, number):
        x = ord(self.letter.upper()) - 65
        if letter.lower() == self.letter.lower() \
                and (self.number + 1 == number or self.number -1 == number):
            return True
        elif number == self.number and (letter == chr(x + 66) or letter == chr(
                x + 64)):
            return True
        elif letter == chr(x + 66) and (number == self.number + 1
                                        or number == self.number - 1):
            return True
        elif letter == chr(x + 64) and (number == self.number + 1
                                        or number == self.number - 1):
            return True
        else:
            return False

    def piece_path(self, i, j):
        x = ord(self.letter.upper()) - 65
        if self.letter == i and self.number < j:
            return i, "num", self.number + 1
        elif self.letter == i and self.number > j:
            return i, "num", self.number - 1
        elif self.number == j and ord(self.letter) - 65 > ord(i) - 65:
            x = ord(self.letter) - 65
            return chr(x + 66), "let", j
        elif self.number == j and ord(self.letter) - 65 < ord(i) - 65:
            x = ord(self.letter) - 65
            return chr(x + 64), "let", j

        elif ord(i) < x:
            if j > self.number:
                return i, "num", self.number + 1
            elif j < self.number:
                return i, "num", self.number - 1
        elif ord(i) > x:
            if j > self.number:
                return i, "let", self.number + 1
            elif j < self.number:
                return i, "let", self.number - 1

    def __repr__(self):
        return "R"
