"""Implementar un algoritmo usando PD que devuelva la minima cantidad de operacion si
solo se puede multiplicar por 2 o sumar 1"""


def llegar_a_k(k):
    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for i in range(1, k + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 2)

    # Recuperar las operaciones realizadas
    operations = []
    i = k
    while i > 0:
        operations.append(i)
        if i % 2 == 0 and dp[i // 2] + 1 == dp[i]:
            i //= 2
        else:
            i -= 1
    return dp, list(reversed(operations))


# Ejemplo de uso

K = 10
min_ops, operations_list = llegar_a_k(K)
print(f"Mínima cantidad de operaciones para llegar a {K}: {min_ops}")
print("Operaciones realizadas:", operations_list)
