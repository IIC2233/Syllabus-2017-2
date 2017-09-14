

# 1 Ciudades por pais
def ciudad_por_pais(nombre_pais, paises, ciudades):
    '''
    :param nombre_pais: str
    :param paises: lista de Paises (instancias)
    :param ciudades: lista de Ciudades (instancias)
    :return: generador
    '''
    pass


# 2 Personas por pais
def personas_por_pais(nombre_pais, paises, ciudades, personas):
    '''
    :param nombre_pais: str
    :param paises: lista de Paises (instancias)
    :param ciudades: lista de Ciudades (instancias)
    :param personas: lista de Personas (instancias)
    :return: generador
    '''
    pass


# 3 Personas por ciudad
def personas_por_ciudad(nombre_ciudad, personas):
    '''
    filtramos a las personas por ciudad que queremos
    :param nombre_ciudad: str
    :param personas: lista de Personas (instancias)
    :return: generador
    '''
    pass


# 4 Personas con sueldo mayor a x
def personas_con_sueldo_mayor_a(personas, sueldo):
    '''
    :param personas: lista de Personas (instancias)
    :param sueldo: int
    :return: generador
    '''
    pass


# 5 Personas ciudad y sexo dado
def personas_por_ciudad_sexo(nombre_ciudad, sexo, personas):
    '''
    :param nombre_ciudad: str
    :param sexo: str
    :param personas: lista de Personas (instancias)
    :return: generador
    '''
    pass


# 6 Personas por pais sexo y profesion
def personas_por_pais_sexo_profesion(nombre_pais, paises, sexo, profesion,
                                     ciudades, personas):
    '''
    :param nombre_pais: str
    :param paises: lista de Paises (instancias)
    :param sexo: str
    :param profesion: str
    :param ciudades: lista de Ciudades (instancias)
    :param personas: lista de Personas (instancias)
    :return: generador
    '''
    pass


# 7 Sueldo promedio mundo
def sueldo_promedio(personas):
    '''
    :param personas: lista de Personas (lista de instancias)
    :return: promedio (int o float)
    '''
    pass


# 8 Sueldo promedio de una ciudad x
def sueldo_ciudad(nombre_ciudad, personas):
    '''
    :param nombre_ciudad: str
    :param personas: lista de Personas (instancias)
    :return: promedio (int o float)
    '''
    pass


# 9 Sueldo promedio de un pais x
def sueldo_pais(nombre_pais, paises, ciudades, personas):
    '''
    :param nombre_pais: str
    :param paises: lista de Paises (instancias)
    :param ciudades: lista de Ciudades (instancias)
    :param personas: lista de Personas (instancias)
    :return: promedio (int o float)
    '''
    pass

# 10 Sueldo promedio de un pais y profesion x
def sueldo_pais_profesion(nombre_pais, paises, profesion, ciudades, personas):
    '''
    :param nombre_pais: str
    :param paises: lista de Paises (instancias)
    :param profesion: str
    :param ciudades: lista de Ciudades (instancias)
    :param personas: lista de Personas (instancias)
    :return: promedio (int o float)
    '''
    pass


if __name__ == '__main__':


    """Abra los archivos y guarde en listas las instancias; paises, ciudades,
    personas"""
    with open('Ciudades.txt', 'r') as file1:
        pass

    with open('Informacion_personas.txt', 'r') as file2:
        pass

    with open('Paises.txt', 'r') as file3:
        pass

    """NO DEBE MODIFICAR CODIGO DESDE EL PUNTO (1) AL (10).
    EN (11) y (12) DEBEN ESCRIBIR SUS RESPUESTAS RESPECTIVAS."""

    # (1) Ciudades en Chile
    # ciudades_chile = ciudad_por_pais('Chile', paises, ciudades)
    # count = 0
    # for ciudad in ciudades_chile:
    #     print(ciudad.sigla_pais, ciudad.nombre)
    #     count += 1
    #     if count == 10:
    #         break

    # (2) Personas en Chile
    # personas_chile = personas_por_pais('Chile', paises, ciudades, personas)
    # count = 0
    # for p in personas_chile:
    #     print(p.nombre, p.ciudad_residencia)
    #     count += 1
    #     if count == 10:
    #         break

    # (3) Personas en Osorno, Chile
    # personas_stgo = personas_por_ciudad('Osorno', personas)
    # for p in personas_stgo:
    #     print(p.nombre, p.ciudad_residencia)

    # (4) Personas en el mundo con sueldo mayor a 600
    #p_sueldo_mayor_600 = personas_con_sueldo_mayor_a(personas, 600)
    # count = 0
    # for p in p_sueldo_mayor_600:
    #     print(p.nombre, p.sueldo)
    #     count += 1
    #     if count == 10:
    #         break

    # (5) Personas en ViñaDelMar, Chile de sexo femenino
    # pxcs = personas_por_ciudad_sexo('ViñaDelMar', 'Femenino', personas)
    # for p in pxcs:
    #     print(p.nombre, p.ciudad_residencia, p.sexo)

    # (6) Personas en Chile de sexo masculino y area Medica
    # pxpsp = personas_por_pais_sexo_profesion('Chile', paises, 'Masculino',
    #                                          'Medica', ciudades, personas)
    # for p in pxpsp:
    #     print(p.nombre, p.sigla_pais, p.sexo, p.area_de_trabajo)

    # (7) Sueldo promedio de personas del mundo
    # sueldo_mundo = sueldo_promedio(personas)
    # print('Sueldo promedio: ', sueldo_mundo)

    # (8) Sueldo promedio Osorno, Chile
    # sueldo_santiago = sueldo_ciudad('Osorno', personas)
    # print('Sueldo Osorno: ', sueldo_santiago)

    # (9) Sueldo promedio Chile
    # sueldo_chile = sueldo_pais('Chile', paises, ciudades, personas)
    # print('Sueldo Chile: ', sueldo_chile)

    # (10) Sueldo promedio Chile de un estudiante
    # sueldo_chile_estudiantes = \
    #     sueldo_pais_profesion('Chile', paises, 'Estudiante', ciudades,
    #                           personas)
    # print('Sueldo estudiantes Chile: ', sueldo_chile_estudiantes)

    # (11) Muestre a los 10 Chilenos con mejor sueldo con un indice de orden
    # desde 0.

    # (12) Se pide seleccionar 10 personas al azar y generar tuplas con sus:
    # nombres, apellidos y sueldos.
