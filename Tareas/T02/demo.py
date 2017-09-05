import gui
import sys
from random import choice


def get_next_number():
    num = 1
    while True:
        yield num
        num += 1


a = get_next_number()


class MyInterface(gui.GameInterface):
    def __init__(self):
        pass

    def colocar_pieza(self, i, j):
        print("Presionaste", (i, j))
        # comenta la siguiente linea y descomenta la que sigue para ver como se destaca un espacio
        gui.add_piece(i, j)
        gui.nueva_pieza() #Ojo con esto si no utilizan una nueva pieza obtendran un error
        # gui.add_hint(i, j)

    def rotar_pieza(self, orientation):
        print(orientation)

    def retroceder(self):
        print("Presionaste retroceder")

    def terminar_juego(self):
        print("Presionaste terminar juego")

    def hint_asked(self):
        print("Me pediste una pista y no te la dare :P")

    def click_number(self, number):
        print(number)

    def guardar_juego(self):
        gui.add_number(next(a), choice(["red", "blue"]))
        print("Presionaron guardar")


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)


    sys.__excepthook__ = hook

    gui.set_scale(False)  # Any float different from 0
    gui.init()
    gui.set_quality("ultra")  # low, medium, high ultra
    gui.set_animations(False)
    gui.init_grid()
    gui.set_game_interface(MyInterface())  # GUI Listener
    gui.run()
