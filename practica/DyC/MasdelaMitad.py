"""Implementar, por división y conquista, una función que dado un arreglo de enteros, devuelva
True si existe un elemento que se repite más de la mitad de las veces en el arreglo, y False
en caso contrario."""


def mas_de_la_mitad(arr):
    candidato = _mdm(arr, 0, len(arr) - 1)
    contador = 0
    for i in range(len(arr)):
        if arr[i] == candidato:
            contador += 1
    return contador > len(arr) / 2


def _mdm(arreglo, inicio, fin):
    if inicio > fin:
        return -1
    elif inicio == fin:
        return arreglo[inicio]
    medio = (inicio + fin) // 2
    izq = _mdm(arreglo, inicio, medio)
    der = _mdm(arreglo, medio + 1, fin)
    contador_izq, contador_der = 0, 0
    for val in arreglo:
        if val == izq:
            contador_izq += 1
        if val == der:
            contador_der += 1
    if contador_izq > contador_der:
        return izq
    return der


print(mas_de_la_mitad([2, 3, 1, 1, 1]))
