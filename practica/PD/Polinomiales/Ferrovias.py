"""Un ramal ferroviaria pone en concesión los patios de comida en todas las estaciones. Son en total “n” estaciones.
Por cada estación se cuenta con el promedio de facturación de los últimos 5 años. Por normativa antimonopólica existe
como limitante que ninguna empresa puede explotar 3 o más estaciones contiguas. Pero ,no existe una cantidad máxima
de estaciones a explotar. Un oferente nos solicita que le digamos cuales son las estaciones que le conviene obtener
para maximizar sus ganancias. Plantee la solución mediante programación dinámica.
"""


def maximizar_ganancias(facturacion):
    n = len(facturacion)
    dp = [(0, 0)] * n  # (sin el anterior, con el anterior)
    dp[0] = (facturacion[0], facturacion[0])
    dp[1] = (facturacion[1], facturacion[0] + facturacion[1])
    for i in range(2, n):
        dp[i] = (
            facturacion[i] + max(dp[i - 2]),
            facturacion[i] + dp[i - 1][0]
        )
    return dp


# Ganancia máxima: [(10, 10, 0), (10, 20, 10), (30, 30, 20), (45, 55, 30), (60, 75, 55)]

# Ejemplo de uso
facturacion = [10, 10, 20, 25, 30]

ganancia_maxima = maximizar_ganancias(facturacion)
print("Ganancia máxima:", ganancia_maxima)
