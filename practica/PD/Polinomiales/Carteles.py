"""Contamos con una carretera de longitud M km que tiene distribuidos varios carteles publicitarios. Cada cartel ”i”
está ubicado en un “ki” kilómetro determinado (pueden ubicarse en cualquier posición o fracción de kilómetro) y a
quien lo utiliza le asegura una ganancia “gi”. Por una regulación no se puede contratar más de 1 cartel a 5km de
otros. Queremos determinar qué carteles conviene contratar de tal forma de maximizar la ganancia a obtener."""


def maximizar_ganancia(carteles):
    carteles_ordenados = sorted(carteles, key=lambda x: x[0])  # Ordenar carteles por posición kilométrica
    n = len(carteles_ordenados)
    dp = [0] * n  # Lista para almacenar la ganancia acumulativa máxima hasta cada posición
    for i in range(n):
        incluido = carteles_ordenados[i][1]  # Inicializar con la ganancia del cartel actual
        for j in range(i - 1, -1, -1):
            if carteles_ordenados[i][0] - carteles_ordenados[j][0] >= 5:
                incluido += dp[j]
                break
        dp[i] = max(dp[i - 1], incluido)
    # ganancia_maxima = max(dp)f
    return dp


# Ejemplo de uso:
carteles = [(2, 20), (5, 10), (7, 15),
            (11, 25)]  # Ejemplo de entrada con posiciones y ganancias Ganancia máxima: [20, 10, 35, 45]
resultado = maximizar_ganancia(carteles)
print("Ganancia máxima:", resultado)
