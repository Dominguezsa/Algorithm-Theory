def max_classes(classes):
    # Ordenar las clases por el tiempo de finalización
    classes.sort(key=lambda x: x[1])

    n = len(classes)
    selected_classes = []

    # Seleccionar clases no superpuestas
    selected_classes.append(classes[0])
    last_class_index = 0

    for i in range(1, n):
        if classes[i][0] >= classes[last_class_index][1]:
            selected_classes.append(classes[i])
            last_class_index = i

    return selected_classes


# Ejemplo de uso
clases = [(2, 3), (2, 4), (5, 6), (4, 7), (8, 9)]
clases_seleccionadas = max_classes(clases)
cantidad_clases = len(clases_seleccionadas)


def max_ganancia(classes):
    # Ordenar las clases por el tiempo de finalización
    classes.sort(key=lambda x: x[1])

    n = len(classes)
    dp = [0] * n

    # Inicializar la tabla de programación dinámica
    dp[0] = classes[0][2]  # El valor de la primera clase

    # Llenar la tabla de programación dinámica
    for i in range(1, n):
        incluido = classes[i][2]  # Valor de la clase actual
        for j in range(i - 1, -1, -1):
            if classes[i][0] >= classes[j][1]:
                incluido += dp[j]
                break
        dp[i] = max(dp[i - 1], incluido)
    return dp[n - 1], encontrar_solucion(dp, classes)


def encontrar_solucion(dp, classes):
    n = len(dp)
    clases_optimas = []
    i = n - 1
    while i > 1:
        if classes[i][2] + dp[i - 2] >= dp[i - 1]:
            clases_optimas.insert(0, i)
            i -= 2
        else:
            i -= 1
    if dp[1] == classes[1][2]:
        clases_optimas.insert(0, 1)
    else:
        clases_optimas.insert(0, 0)
    return clases_optimas


# Ejemplo de uso
clases = [(2, 3, 10), (2, 4, 20), (5, 6, 15), (4, 7, 5), (8, 9, 25)]
ganancia_total = max_ganancia(clases)

print("Clases:", clases)
print(f"La mayor ganancia posible es: {ganancia_total}")
