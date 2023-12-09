"""problema de la mochila"""


def problema_mochila(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
    #return reconstruir_solucion(dp, n)
    return dp

def reconstruir_solucion(dp, w):
    selected_items = []
    i, j = len(dp)-1, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.insert(0, i - 1)
            j -= weights[i - 1]
        i -= 1
    return selected_items


# Ejemplo de uso
values = [6, 10, 12, 7, 5, 3, 1, 8, 2, 11, 4, 9]
weights = [2, 4, 5, 2, 4, 5, 3, 6, 1, 3, 2, 5]
capacity = 15
result = problema_mochila(values, weights, capacity)
print(result)
