
class IngresoEvent:
    def __init__(self, nombre_usuario):
        '''
        Ayuda a hace más eficiente el imgreso de usuario
        :param nombre_usuario: str
        '''
        self.nombre_usuario = nombre_usuario


class MoveEvent:
    def __init__(self, x):
        '''
        Ayuda a actualizar el parámetro x de la imagen de manera más eficiente
        :param x: int
        '''
        self.x = x
