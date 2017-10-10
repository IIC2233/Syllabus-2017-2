__author__ = 'joaquin'
# Modificado por Alejandro Kaminetzky y Gabriel Lyon

import threading
import time
import random


class NodoLaberinto:

    def __init__(self, numero):
        self.id = numero
        self.hijos = []
        # Con esto podemos bloquear (o loquear) un pedazo de código, es decir,
        # una acción.
        self.lock = threading.Lock()

    @property
    def next_room(self):
        # Retorna una conexión aleatoria.
        return random.choice(self.hijos)


class Laberinto:
    def __init__(self, file_name=''):
        with open(file_name, 'r') as file:
            # Guardamos la información del archivo en un generador.
            data = map(lambda x: x.strip().split(','), file)
            # ¿Por qué no podemos sacar este pedazo de código?
            # Para el nodo inicial y final usaremos '*' ya que next de data
            # está retornando "una lista" así: ['1'] y ['60'].
            self.inicio = NodoLaberinto(*next(data))
            self.final = NodoLaberinto(*next(data))
            # Hacer pregunta después de explicar cómo funciona el código.
            # ¿Esto está bien? -- > ¿Por qué?
            # Teóricamente no deberíamos guardar dos veces los nodos, estamos
            # guardando las conexiones en cada nodo y acá (en 'self.rooms').
            # Se debería hacer un método recursivo para recorrer los nodos que
            # ya existen.

            # Se guarda en una lista los nodos.
            self.rooms = [self.inicio, self.final]
            # ¿Por qué esto funciona? --> data está retornando una "lista" así:
            # ['num1', 'num2']
            for node_number_1, node_number_2 in data:
                # Si no existe un nodo con el número 'node_number_1' -> lo crea.
                if not self.has_room(node_number_1):
                    self.add_room(node_number_1)
                # Si no existe un nodo con el número 'node_number_2' -> lo crea.
                if not self.has_room(node_number_2):
                    self.add_room(node_number_2)
                # Se obtienen los nodos y agrega dentro de los nodos
                # hijos el nodo2
                node1 = self.get_node(node_number_1)
                node2 = self.get_node(node_number_2)
                node1.hijos.append(node2)
        self.personas = []
        self.sobrevivencias = []
        self.new_humans = threading.Thread(target=Laberinto.human_generator,
                                           args=(self,), daemon=True)

    def get_node(self, number):
        # Este método retorna un nodo dentro de 'self.rooms' o None en caso de
        # que no exista.
        for node in self.rooms:
            if node.id == number:
                return node
        return None

    def add_room(self, room):
        # Este método crea un nuevo nodo con el número que se le entrega (room)
        # y lo agrega a 'self.room'.
        new_node = NodoLaberinto(room)
        self.rooms.append(new_node)
        return new_node

    def has_room(self, room_number):
        # Este método verifica si un nodo está dentro de 'self.rooms'.
        for room in self.rooms:
            if room.id == room_number:
                return True
        return False

    def human_generator(self):
        # Este será el thread encargado de la llegada de personas.
        while True:
            # El tiempo entre apariciones distribuye Exp(1/5).
            time.sleep(random.expovariate(1 / 3))
            persona = Persona(self.inicio, self.final.id)
            self.personas.append(persona)
            poison_thread = threading.Thread(target=Laberinto.damage_person,
                                             args=(persona,))
            poison_thread.start()

    @staticmethod
    def damage_person(persona):
        while persona.hp > 0 and not persona.finish:
            time.sleep(1)
            if persona.hp - 6 + persona.resistance <= 0:
                persona.hp = 0
            else:
                persona.hp -= 6 - persona.resistance

    def ver_ganadores(self):
        while len(list(filter(lambda p: p.finish, self.personas))) < 3:
            pass
        print('\nGanadores!')
        ganadores = filter(lambda p: p.finish, self.personas)
        print('Primer Lugar: {}'.format(next(ganadores).name))
        print('Segundo Lugar: {}'.format(next(ganadores).name))
        print('Tercer Lugar: {}'.format(next(ganadores).name))


class Persona(threading.Thread):
    count = 1

    def __init__(self, pieza, meta):
        super().__init__()
        self.name = 'Persona {}'.format(Persona.count)
        Persona.count += 1
        self.pieza_actual = pieza
        self.meta = meta
        self.hp = random.randint(80, 120)
        self.setDaemon(True)
        self.finish = False
        self.resistance = random.randint(1, 3)
        self.start()

        print('Ha aparecido {}.'.format(self.name))

    def run(self):
        # Si sigue vivo va a tratar de entrar a otra pieza.
        while self.hp > 0 and not self.finish:
            self.entrar_pieza(self.pieza_actual.next_room)
        if self.hp <= 0:
            print('{} ha muerto. :('.format(self.name))
        else:
            print('{} ha llegado!'.format(self.name))

    def entrar_pieza(self, pieza):
        if pieza.id == self.meta:
            self.finish = True
        else:
            with pieza.lock:
                waiting_time = random.randint(1, 3)
                time.sleep(waiting_time)
                print('{} entró a la pieza {} con vida {}.'
                      .format(self.name, pieza.id, self.hp))
                self.pieza_actual = pieza


if __name__ == '__main__':
    laberinto = Laberinto('laberinto.txt')
    # Comenzamos el generador de personas.
    new_humans = threading.Thread(target=laberinto.human_generator, daemon=True)
    new_humans.start()
    # Comenzamos el thread que revisa si hay ganadores.
    watch = threading.Thread(target=laberinto.ver_ganadores)
    watch.start()