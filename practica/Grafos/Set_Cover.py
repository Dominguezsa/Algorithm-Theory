def es_solucion(universo, parcial):
    res = []
    for valores in parcial:
        for valor in valores:
            if valor not in res:
                res.append(valor)
    return len(res) == len(universo)


def set_cover_backtracking(universe, sets):
    for i in range(1, len(sets)):
        asignacion_actual = []
        j = backtrack(i, 0, asignacion_actual, sets, universe)
        if j[0]:
            return i, asignacion_actual
    return len(sets), sets


def aporta_algo(parcial, nuevo):
    if len(parcial) == 0:
        return True
    for elemento in nuevo:
        for subset in parcial:
            if elemento not in subset:
                return True
    return False


def backtrack(max_n, grupo, asignacion_actual, sets, universe):
    if es_solucion(universe, asignacion_actual):
        return True, asignacion_actual
    if grupo == len(sets):
        return False, None
    if len(asignacion_actual) == max_n:
        return False, None
    if aporta_algo(asignacion_actual, sets[grupo]):
        asignar(sets[grupo], asignacion_actual)
        if backtrack(max_n, grupo + 1, asignacion_actual, sets, universe)[0]:
            return True, asignacion_actual
        desasignar(sets[grupo], asignacion_actual)
    if backtrack(max_n, grupo + 1, asignacion_actual, sets, universe)[0]:
        return True, asignacion_actual
    return False, None


def asignar(grupo, asignacion_actual):
    asignacion_actual.append(grupo)


def desasignar(grupo, asignacion_actual):
    asignacion_actual.remove(grupo)


# Ejemplo de uso
universe = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sets = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9,10]]

result = set_cover_backtracking(universe, sets)
print("Conjunto de cobertura (backtracking): ", result)
