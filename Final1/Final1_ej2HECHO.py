"""Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden
iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las
directamente adyacentes a estas (es decir, un “radio de 2 celdas”)."""

import copy


def min_faro(matriz, submarinos):
    if submarinos == 0:
        return 0
    for i in range(1, submarinos):
        m = copy.deepcopy(matriz)
        q = [0]
        j = backtracking(m, i, q, 0, 0)
        if j:
            return i
    return submarinos  # Si no se encuentra una solución, devuelve numero de submarinos


def es_solucion(matriz):
    for fila in matriz:
        if -1 in fila:
            return False
    return True


def ilumina_algo(matriz, x, y):
    for i in range(1, 3):
        if x - i >= 0:
            for j in range(1, 3):
                if y - j >= 0 and matriz[x - i][y - j] == -1:
                    return True
                if y + j < len(matriz[x]) and matriz[x - i][y + j] == -1:
                    return True
                if x + i < len(matriz):
                    if y - j >= 0 and matriz[x + i][y - j] == -1:
                        return True
                    if y + j < len(matriz[x]) and matriz[x + i][y + j] == -1:
                        return True
    return False


def backtracking(matriz, cantidad, actuales, m, k):
    if es_solucion(matriz):
        return True
    if cantidad == actuales[0]:
        return False
    for i in range(m, len(matriz)):
        for j in range(k, len(matriz[i])):
            if not ilumina_algo(matriz, i, j):
                continue
            asignar(matriz, i, j, 1)
            actuales[0] += 1
            if backtracking(matriz, cantidad, actuales, i, j):
                return True
            asignar(matriz, i, j, -1)
            actuales[0] -= 1
    return False


def asignar(matriz, x, y, h):
    for i in range(1, 3):
        for j in range(1, 3):
            if x - i >= 0:
                if y - j >= 0:
                    matriz[x - i][y - j] += h
                if y + j < len(matriz[x]):
                    matriz[x - i][y + j] += h
            if x + i < len(matriz):
                if y - j >= 0:
                    matriz[x + i][y - j] += h
                if y + j < len(matriz[x]):
                    matriz[x + i][y + j] += h


# Ejemplo de uso:
matriz = [
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1]
]

resultado = min_faro(matriz, 3)  # Cambiar el segundo argumento a 5
if resultado is not None:
    print("Cantidad mínima de faros necesarios:", resultado)
else:
    print("No se encontró una solución.")
