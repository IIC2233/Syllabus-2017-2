"""Basado en ejemplo de Mr.Patiwi de 2016-1"""
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import sys
import time


class MoveMyImageEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


class Character(QThread):
    trigger = pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv

    def __init__(self, parent, x, y):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.image = QLabel(parent)
        self.image.setGeometry(100, 100, 100, 100)
        self.image.setPixmap(QPixmap("green_boss"))
        self.image.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.actualizar_imagen)
        self.__position = (0, 0)
        self.position = (x, y)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su señal a la ventana cuando cambiamos la posición
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1]
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def run(self):
        while True:
            time.sleep(0.05)
            if self.position[1] <= 300:
                self.position = (self.position[0], self.position[1] + 10)
            else:
                self.position = (self.position[0], 0)


class Bastian(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pelota = Character(self, 130, 40)
        self.titulo = QLabel(self)
        self.titulo.setText("Ejemplo")
        self.titulo.move(160, 10)
        self.titulo.show()
        self.setGeometry(500, 500, 400, 300)
        self.show()

    @staticmethod
    def actualizar_imagen(myImageEvent):
        # Recibo el objeto con la información necesaria para mover a bastián
        # Hagamos un print para corroborar su posición?
        print(myImageEvent.x, myImageEvent.y)
        label = myImageEvent.image
        label.move(myImageEvent.x, myImageEvent.y)

if __name__ == '__main__':
    app = QApplication([])
    ex = Bastian()
    ex.pelota.start()  # Ojo con esto, no empiecen el thread antes de empezar nuestro thread principal!
    sys.exit(app.exec_())
