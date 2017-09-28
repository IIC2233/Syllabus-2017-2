def chess_valid_move(self, i, j, x, y):
    if self.get_piece(x, y) != "-" and self.get_piece(x, y).allied:
        return False

    while (i != x and j != y) or (i == x and j != y) or (
                    i != x and j == y):
        let, tip, num = self.get_piece(i, j).piece_path(x, y)
        if tip == "num":  # Cambio en el numero de la posicion
            return self.get_piece(let, num) == "-"
        elif tip:  # Permite el termino de la busqueda al ya no tener mas camino
            return tip
        else:  # Cambio en la letra de la posicion
            if self.get_piece(let, num) != "-":
                return False
    return True


def peon_valid_move(self, letter, number):
    return letter.lower() == self.letter.lower() and abs(
        number - self.number) == 1


def alfil_valid_move(self, letter, number):
    return abs(ord(self.letter) - ord(letter)) == abs(self.number - number)


def caballo_valid_move(self, letter, number):
    letter_diff = abs(ord(letter.lower()) - ord(self.letter.lower()))
    number_diff = abs(self.number - number)

    return (letter_diff == 2 and number_diff == 1) or (
    letter_diff == 1 and number_diff == 2)


def torre_valid_move(self, letter, number):
    return (self.letter == letter and number != self.number) or (
    self.letter != letter and number == self.number)


def rey_valid_move(self, letter, number):
    return abs(ord(self.letter.lower()) - ord(letter.lower())) <= 1 and abs(
        self.number - number) <= 1


def reina_valid_move(self, letter, number):
    return abs(ord(self.letter) - ord(letter)) == abs(
        self.number - number) or (
               self.letter == letter and self.number != number) or (
               self.number == number and self.letter != letter)
