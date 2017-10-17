from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.Qt import QTest
import time
from Eventos import IngresoEvent
from Eventos import MoveEvent


class Character(QObject):
    '''
    Este será nuestro BackEnd, ya que no solo manejará el movimiento de la
    imagen, sino que todo el procedimiento que ocurre por detrás del
    código que muestra la ventana

    Tiene como parámetros:
    trigger_move: señal que hace que la imagen se mueva
    trigger_respuesta_ingreso: señal que hace que aparezca la imagen y se
                                seteen nuevos valores
    '''

    trigger_move = pyqtSignal(MoveEvent)
    trigger_respuesta_ingreso = pyqtSignal(IngresoEvent)

    def __init__(self, parent, x, y):
        '''
        Inicio los triggers
        :param parent: se le da el "self" de la clase madre para que se sepa
        que pertenece a ella
        :param x: posición x de la imagen
        :param y: posición y de la imagen
        '''
        super().__init__()

        self.nombre = ""

        self.position = (x, y)

        self.trigger_respuesta_ingreso.connect(parent.comenzar)
        self.trigger_move.connect(parent.actualizarImagen)

    def ingreso(self, event):
        '''
        Desencadena el evento de ingreso
        :param event: evento ingreso
        '''

        self.nombre = event.nombre_usuario

        #Confirmar que el nombre es valido

        self.trigger_respuesta_ingreso.emit(IngresoEvent(self.nombre))

    def mover(self, event):
        '''
        Avisa que la imagen se tiene que mover
        :param event: evento mover_imagen
        '''

        #Confirmar que la posicion es valida

        if event.x == 1:
            self.position = (self.position[0] + 10, self.position[1])
        else:
            self.position = (self.position[0] - 10, self.position[1])

        self.trigger_move.emit(MoveEvent(self.position[0]))



