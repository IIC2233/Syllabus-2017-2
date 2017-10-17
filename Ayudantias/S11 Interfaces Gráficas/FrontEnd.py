
from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.Qt import QTest
import time
from BackEnd import Character
from Eventos import IngresoEvent
from Eventos import MoveEvent


class Ventana(QWidget):

    trigger_ingreso = pyqtSignal(IngresoEvent)
    trigger_mover = pyqtSignal(MoveEvent)

    def __init__(self):
        '''
        Hacemos funcionar el programa con la función self.__setUp()
        '''
        super().__init__()
        self.__setUp()

    def __setUp(self):
        '''
        Crea los elementos básicos de la ventana y conecta los trigger
        '''

        self.back_end = Character(self, 100, 30)

        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Ejemplo")

        # Box vertical principal en el cual se almacenan todos los otros box
        self.vbox = QVBoxLayout(self)

        # Box hoizontal para almacenar el editor de texto y el boton necesarios para el ingreso de usuario
        self.ingreso_layout = QHBoxLayout(self)

        self.ingreso_usuario = QLineEdit(self)

        self.boton_ingreso = QPushButton(self)
        self.boton_ingreso.clicked.connect(self.ingresar)

        # Se agregan los elementos a los layout
        self.ingreso_layout.addWidget(self.ingreso_usuario)
        self.ingreso_layout.addWidget(self.boton_ingreso)

        self.vbox.addLayout(self.ingreso_layout)

        # Hace visible la ventana
        self.show()

        self.trigger_ingreso.connect(self.back_end.ingreso)
        self.trigger_mover.connect(self.back_end.mover)


    def ingresar(self):
        '''
        Envía la señal de que se agrega un nombre al usuario
        '''

        self.ingreso_usuario.hide()
        self.boton_ingreso.hide()
        self.trigger_ingreso.emit(IngresoEvent(self.ingreso_usuario.text()))

    def comenzar(self, event):
        '''
        Es la respuesta al evento que ocurre
        :param event: señal del evento
        '''

        self.nombre = QLabel(self)

        self.nombre.setText(event.nombre_usuario)

        self.vbox.addWidget(self.nombre)

        # Box horizontal para almacenar los botones derecha e izquierda
        self.botones_layout = QHBoxLayout(self)

        self.derecha = QPushButton("->", self)
        self.izquierda = QPushButton("<-", self)
        self.derecha.clicked.connect(self.mover)
        self.izquierda.clicked.connect(self.mover)

        self.botones_layout.addWidget(self.izquierda)
        self.botones_layout.addWidget(self.derecha)

        self.vbox.addLayout(self.botones_layout)
        self.vbox.addStretch(10)

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("car.jpg").scaled(450/3, 300/3))
        self.image.setFixedSize(160, 130)
        self.image.move(100, 100)
        self.image.show()
        #self.vbox.addWidget(self.image)
        self.vbox.addStretch(5)
        #self.image.move(100, 30)

        self.setLayout(self.vbox)

        #self.show()

    def mover(self):
        '''
        Envía la señal al trigger para hacer que se mueva la imagen
        '''

        izquierda_derecha = self.sender()

        if izquierda_derecha.text() == "->":
            self.trigger_mover.emit(MoveEvent(1))
        else:
            self.trigger_mover.emit(MoveEvent(0))

    def actualizarImagen(self, event):
        '''
        Recibe el evento de mover la imagen y la actualiza
        :param event: evento mover imagen
        '''
        self.image.move(event.x, self.image.y())

if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()

    app.exec_()