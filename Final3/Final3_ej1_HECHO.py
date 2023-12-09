"""Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
y justificar la complejidad del algoritmo."""


def obtener_mesa(grupos, maximo):
    dp = [[0 for _ in range(maximo + 1)] for _ in range(len(grupos))]
    for i in range(len(grupos)):
        for j in range(1, maximo + 1):
            if grupos[i] <= j:
                usando = grupos[i]
            else:
                usando = 0
            if 0 <= j - grupos[i] < j:
                dp[i][j] = max(usando + dp[i - 1][j - grupos[i]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    fila = len(grupos) - 1
    columna = dp[fila].index(max(dp[-1]))
    return reconstruir(dp, fila, columna, grupos, [])


def reconstruir(matriz, fila, columna, grupos, rta):
    if columna <= 0 or fila == 0:
        if len(rta) < len(matriz):
            if matriz[fila][columna] != 0:
                rta.append("Si")
            else:
                rta.append("No")
        return list(reversed(rta))
    if matriz[fila][columna] == matriz[fila - 1][columna]:
        rta.append("No")
        return reconstruir(matriz, fila - 1, columna, grupos, rta)
    else:
        rta.append("Si")
        return reconstruir(matriz, fila - 1, columna - grupos[fila], grupos, rta)


j = obtener_mesa([1, 3, 4, 5], 10)
for fila in j:
    print(fila)
