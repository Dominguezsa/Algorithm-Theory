"""2. Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)). Cada vertice tiene un valor (positivo).
Implementar un algoritmo que, utilizando programación dinámica, obtenga el Set Independiente de suma máxima
dentro de un grafo de dichas características. Indicar y justificar la complejidad del algoritmo implementado.

Es el mismo que Juan el Vago:
"""


def juan_el_vago(graph):
    n = len(graph)
    if n == 0:
        return 0
    if n == 1:
        return graph[0]
    dp = [0] * n
    dp[0] = graph[0]
    dp[1] = max(graph[0], graph[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + graph[i])

    return dp[n - 1]


print(juan_el_vago([1, 3, 1, 5, 10]))
