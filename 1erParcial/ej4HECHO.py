"""Implementar un algoritmo que reciba un Grafo y un número k y devuelva un dominating set de dicho grafo de a lo
sumo k vértices (si existe)."""


def dominating_set_bt(grafo, actual, k, solucion_parcial):
    if len(solucion_parcial) == k:
        if cubre_todos(grafo, solucion_parcial):
            return solucion_parcial
        else:
            return None
    if len(solucion_parcial) < k and cubre_todos(grafo, solucion_parcial):
        return solucion_parcial
    if actual == len(grafo):
        return None

    # probamos agregando el vertice
    v = grafo.vertices()[actual]
    solucion_parcial.add(v)
    # Se podria agregar una poda donde si no cubrimos un nuevo vértice por agregar al vértice,
    # entonces obviamos esa alternativa
    solucion = dominating_set_bt(grafo, actual + 1, k, solucion_parcial)
    if solucion is not None:
        return solucion
    solucion_parcial.remove(v)
    return dominating_set_bt(grafo, actual + 1, k, solucion_parcial)


def dominating_set(grafo, k):
    return dominating_set_bt(grafo, 0, k, set())


def cubre_todos(grafo, domset):
    dominados = set()
    for v in domset:
        dominados.add(v)
        for w in grafo.adyacentes(v):
            dominados.add(w)
    return len(dominados) == len(grafo)