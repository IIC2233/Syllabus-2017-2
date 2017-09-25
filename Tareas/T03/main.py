from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys


class T03Window(MyWindow):
    def __init__(self):
        super().__init__()

    def process_query(self, query_array):
        # Agrega en pantalla la solucion. Muestra los graficos!!
        print(query_array)
        text = "Probando funcion\nConsulta 01\n"
        self.add_answer(text)

    def save_file(self, query_array):
        # Crea un archivo con la solucion. NO muestra los graficos!!
        print(query_array)

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)


    sys.__excepthook__ = hook

    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
