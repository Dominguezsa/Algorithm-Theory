"""Ejercicio 1 con backtraking"""


def encontrar_mejor_asignacion(p, w):
    n = len(p)
    w = [w]
    mejor_asignacion = [0] * n
    mejor_espacios_vacios = [float('inf')]
    asignacion_actual = [0] * n
    backtrack(w, 0, asignacion_actual, mejor_asignacion, mejor_espacios_vacios, n, p)
    return mejor_asignacion


def backtrack(espacios_disponibles, grupos, asignacion_actual, mejor_asignacion, mejor_espacios_vacios, longitud_p, p):
    if grupos == longitud_p:
        return False
    if es_preciso(espacios_disponibles[0]):
        return True
    if not es_posible(espacios_disponibles[0]):
        return False
    asignar(grupos, asignacion_actual, espacios_disponibles, mejor_asignacion, mejor_espacios_vacios, p)
    if backtrack(espacios_disponibles, grupos + 1, asignacion_actual, mejor_asignacion, mejor_espacios_vacios, longitud_p, p):
        return True
    anti_asignar(espacios_disponibles, p, grupos, asignacion_actual)
    backtrack(espacios_disponibles, grupos + 1, asignacion_actual, mejor_asignacion, mejor_espacios_vacios, longitud_p, p)


def anti_asignar(espacios_disponibles, p, grupos, asignacion_actual):
    asignacion_actual[grupos] = 0
    e = espacios_disponibles[0]
    espacios_disponibles.clear()
    e += p[grupos]
    espacios_disponibles.extend([e])


def asignar(grupos, asignacion_actual, espacios_disponibles, mejor_asignacion, mejor_espacios_vacios, p):
    asignacion_actual[grupos] = 1
    e = espacios_disponibles[0]
    espacios_disponibles.clear()
    e -= p[grupos]
    espacios_disponibles.extend([e])
    if es_posible(espacios_disponibles[0]):
        if espacios_disponibles[0] < mejor_espacios_vacios[0]:
            mejor_asignacion.clear()
            mejor_asignacion.extend(asignacion_actual)
            mejor_espacios_vacios.clear()
            mejor_espacios_vacios.extend(espacios_disponibles)


def es_preciso(espacios_disponibles):
    return espacios_disponibles == 0


def grupo_puede_sentarse(personas_grupo, espacios_disponibles):
    return personas_grupo <= espacios_disponibles


def es_posible(e):
    return e >= 0


Lu = [4, 4, 20, 20, 5]
W = 7
mej = encontrar_mejor_asignacion(Lu, W)
print(mej)
