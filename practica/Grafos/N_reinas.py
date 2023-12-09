def resolver_n_reinas(n):
    tablero = [["." for _ in range(n)] for _ in range(n)]
    if backtrack(0, n, tablero):
        return tablero, True
    return None, False


def backtrack(fila, n, tablero):
    if fila == n:
        return True
    for col in range(n):
        if es_valido(tablero, fila, col):
            tablero[fila][col] = "Q"
            if backtrack(fila + 1, n, tablero):
                return True
            tablero[fila][col] = "."
    return False


def es_valido(tablero, fila, col):
    n = len(tablero)
    for i in range(n):
        if tablero[fila][i] == "Q" or tablero[i][col] == "Q":
            return False
    for i in range(n):
        for j in range(n):
            if i + j == fila + col or i - j == fila - col:
                if tablero[i][j] == "Q":
                    return False
    return True


# Ejemplo de uso
n = 4  # Puedes cambiar el valor de N según lo necesites
solucion = resolver_n_reinas(n)

if solucion[1]:
    print("Solucion encontrada:")
    for fila in solucion[0]:
        print(" ".join(fila))
else:
    print(f"No se encontraron soluciones para N = {n}")
