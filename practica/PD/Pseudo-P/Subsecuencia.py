"""Se conoce como “Longest increasing subsequences” al problema de, dado un vector de numérico, encontrar la
subsecuencia más larga de números (no necesariamente consecutivos) donde cada elemento sea mayor a los anteriores.
Ejemplo: En la lista →  2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7. Podemos ver que la subsecuencia más larga es de longitud 6 y
corresponde a la siguiente “1, 2, 3, 4, 6, 7”.  Resolver el problema mediante programación dinámica."""


def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    # Calcular las longitudes de las subsecuencias crecientes más largas
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    # Encontrar la longitud máxima en el arreglo dp
    max_length = max(dp)

    # Reconstruir la subsecuencia más larga
    subsequence = []
    last_index = dp.index(max_length)
    for i in range(last_index, -1, -1):
        if dp[i] == max_length:
            subsequence.insert(0, arr[i])
            max_length -= 1

    return dp


# Ejemplo de uso
vector = [2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]
resultado = longest_increasing_subsequence(vector)
print("Subsecuencia más larga:", resultado)
print("Longitud de la subsecuencia:", len(resultado))
