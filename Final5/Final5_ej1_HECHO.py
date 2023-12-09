"""Implementar un algoritmo que, por backtracking, obtenga todos los posibles ordenamientos topológicos de un grafo
dirigido y acíclico."""


def obtener_ordenamientos_topologicos_dag(grafo):
    def es_valido(nodo):
        for sucesor in grafo[nodo]:
            if not asignado[sucesor]:
                return False
        return True

    def asignar(nodo):
        asignado[nodo] = True

    def antiasignar(nodo):
        asignado[nodo] = False

    def backtrack():
        if len(ordenamiento) == len(grafo):
            ordenamientos_topologicos.append(list(reversed(ordenamiento)))
            return

        for nodo in range(len(grafo)):
            if not asignado[nodo] and es_valido(nodo):
                asignar(nodo)
                ordenamiento.append(nodo)
                backtrack()
                ordenamiento.pop()
                antiasignar(nodo)

    ordenamientos_topologicos = []
    asignado = [False] * len(grafo)
    ordenamiento = []

    for nodo in range(len(grafo)):
        if not asignado[nodo] and es_valido(nodo):
            asignar(nodo)
            ordenamiento.append(nodo)
            backtrack()
            ordenamiento.pop()
            antiasignar(nodo)

    return ordenamientos_topologicos


# Ejemplo de uso:
grafo = {
    0: [2, 3],
    1: [3],
    2: [3],
    3: [4],
    4: [],
}

ordenamientos = obtener_ordenamientos_topologicos_dag(grafo)
for ordenamiento in ordenamientos:
    print(ordenamiento)
