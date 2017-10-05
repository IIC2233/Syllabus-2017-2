from random import uniform, randint

# Estos parametros son algunos de los definidos en el enunciado.
WEIGHT_FACTOR = 1000  # se usa para sacar B
MAX_PERSON_SPEED = 3
MIN_PERSON_SPEED = 1
MAX_PERSON_WEIGHT = 200
MIN_PERSON_WEIGHT = 40

ANIMAL_SPAWN_MIN = 160
ANIMAL_SPAWN_MAX = 200
ANIMAL_RANGE = 90

PEOPLE = 500

MAX_SIMULATION_TIME = 10000
SIMULATIONS = 20


# Pueden modificar y crear las clases que se les antoje.
class Animal:
    # Identificador unico para cada animal.
    # No tiene niguna utilidad mas que para probar el programa
    id = 0

    def __init__(self, prob_ataque, prob_letal, prob_escape_ataque, especie):
        self.especie = especie
        self.prob_ataque = prob_ataque
        self.prob_escape_ataque = prob_escape_ataque
        self.prob_letal = prob_letal
        self.kills = 0

    def puede_atacar(self, persona):
        # Retorna True si la persona esta dentro del rango de ataque
        pass

    def tasa_ataque(self):
        # Retorna la tasa de ataques
        pass

    def __str__(self):
        pass


class Person:
    def __init__(self):
        self.pos_inicial = randint(0, 100)  # km
        self.pos_actual = self.pos_inicial
        self.sex = choice(["M", "F"])
        self.weight = uniform(40, 200)
        self.safe = False
        self.is_dead = False

        if self.sex == "M":
            self.coef = self.weight * randint(1, 3) / WEIGHT_FACTOR
        else:
            self.coef = self.weight / WEIGHT_FACTOR

        self.velocity = randint(MIN_PERSON_SPEED, MAX_PERSON_SPEED) * self.coef

    def has_survived(self):
        # Retorna True si la persona esta en un km mayor a 100
        pass

    def move(self, dist):
        # Metodo para avanzar
        pass

    def __repr__(self):
        pass
