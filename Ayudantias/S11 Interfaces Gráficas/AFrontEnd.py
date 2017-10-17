from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.Qt import QTest
import time


class Ventana(QWidget):
    def __init__(self):
        super().__init__()



if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()

    app.exec_()