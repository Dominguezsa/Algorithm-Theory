"""
Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m”
números naturales ordenados en forma creciente (m >= n). En el vector no hay números repetidos.
Se desea obtener el menor número no incluido.

Ejemplo:
Array: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
Solución: 6

Proponer un algoritmo de tipo división y conquista que resuelva el problema en
tiempo inferior a lineal. Expresar su relación de recurrencia y calcular su complejidad temporal."""


def menor_no_incluido(arr):
    return buscar_minimo(arr, 0, len(arr) - 1) + 1


def buscar_minimo(arr, inicio, fin):
    if inicio > fin:
        return -1
    if inicio == fin:
        return arr[inicio]
    medio = (inicio + fin) // 2
    if arr[medio] == medio + 1 and arr[medio + 1] != medio + 2:
        return arr[medio]
    if arr[medio] == medio + 1:
        return buscar_minimo(arr, medio + 1, fin)
    return buscar_minimo(arr, inicio, medio - 1)


print(menor_no_incluido([1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]))
