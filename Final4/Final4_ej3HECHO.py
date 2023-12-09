"""Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1^2, por lo que siempre existe solución.

Sin embargo, la expresión 10 = 3^2 + 1^2 es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
necesaria."""


def suma_cuadrados_minima(n):
    # Crear una lista para almacenar la cantidad mínima de términos para cada número
    dp = [0] * (n + 1)

    # Inicializar la lista con un valor grande
    for i in range(1, n + 1):
        dp[i] = i

    # Calcular la cantidad mínima de términos para cada número
    for i in range(2, n + 1):
        for j in range(1, i):
            if i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp


# Ejemplo de uso
n = 100
resultado = suma_cuadrados_minima(n)
print(f"La cantidad mínima de términos cuadráticos para representar {n} es {resultado}")
