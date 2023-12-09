"""

3. Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
(en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.

Ejemplos:

n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)"""


def max_product_cut(n):
    if n < 2:
        return 0

    # Inicializamos un arreglo dp de longitud n + 1 con valores 1
    dp = [0] * (n + 1)

    # El valor para n=2 es 1, ya que no hay cortes.
    dp[1] = 1
    dp[2] = 1
    # Calculamos dp usando programación dinámica
    for i in range(1, n + 1):
        maximo = 1
        for j in range(1, i):
            y = j * (i - j)
            z = j * dp[i - j]
            if y > maximo:
                maximo = y
            if z > maximo:
                maximo = z
            # El resultado se encuentra en dp[n]
        dp[i] = maximo
    return dp


# Ejemplo de uso
n = 14
max_prod = max_product_cut(n)
print(f"El producto máximo al cortar una soga de longitud {n} es: {max_prod}") # [0, 1, 1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108, 162]
