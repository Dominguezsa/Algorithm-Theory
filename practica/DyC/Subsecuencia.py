"""
Resolver el problema de subarreglo de suma máxima por división y conquista. Calcular la complejidad del algoritmo.
Entrada: Un arreglo A[1..N] de enteros (de cualquier signo)
Salida: Un subarreglo A[i .. j] de A cuya suma es mayor o igual que la de cualquier otro subarreglo de A.

Ejemplo:
Array: [-2, -5, 6, -2, -3, 1, 5, -6]
Solución: [6, -2, -3, 1, 5]"""


def suma_subsecuencia_arreglo(arr):
    """debe devolver el arreglo, NO el numero"""
    if len(arr) == 1:
        return arr
    medio = len(arr) // 2
    izq = suma_subsecuencia_arreglo(arr[:medio])
    der = suma_subsecuencia_arreglo(arr[medio:])
    s3 = suma_al_medio_arreglo(arr)
    return max(izq, der, s3, key=sum)


def suma_al_medio_arreglo(arr):
    medio = len(arr) // 2
    s1 = suma_centro_arreglo(arr[:medio], -1)
    s2 = suma_centro_arreglo(arr[medio:], 1)
    s2.reverse()
    return s1 + s2


def suma_centro_arreglo(arr, direccion):
    """Debe devolver un arreglo, Hay que arreglarlo"""
    max_suma = []
    suma = []
    if direccion == -1:
        for i in range(len(arr) - 1, -1, direccion):
            suma = [arr[i]] + suma
            max_suma = max(max_suma, suma, key=sum)
        return max_suma
    else:
        for i in range(0, len(arr), direccion):
            suma = [arr[i]] + suma
            max_suma = max(suma, max_suma, key=sum)
    return max_suma


print(suma_subsecuencia_arreglo((3, 30, 400, 8, -2, 2, -7, -50)))
print("-----------------")
print(suma_subsecuencia_arreglo((-2, -5, 6, -2, -3, 1, 50, -6)))
print("-----------------")
print(suma_subsecuencia_arreglo([400, -30, -40, -8, -2, 2, -7, 550]))

"""
[30]
[8]
[400]
[8, 400]
[2]
[-50]
[-7]
[-50, -7]
[-2]
[2, -2]
[-7, 2, -2]
[-50, -7, 2, -2]
[3, 30, 400, 8]
"""
