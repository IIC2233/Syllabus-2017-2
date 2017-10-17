from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush, QPalette, QFont
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QSize, Qt, QThread
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.Qt import QTest
import time


class Character(QObject):


    def __init__(self, parent, x, y):
        super().__init__()