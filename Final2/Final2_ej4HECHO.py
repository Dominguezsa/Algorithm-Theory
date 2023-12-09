"""Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se
rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor
forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo
propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado
encuentra siempre la solución óptima? Justificar."""


def minimo_bolsas(bolsas, maximo):
    bolsas = sorted(bolsas, reverse=True)
    rta = []
    for bolsa in bolsas:
        placed = False
        for bag in rta:
            if sum(b + bolsa for b in bag) <= maximo:
                bag.append(bolsa)
                placed = True
                break
        if not placed:
            rta.append([bolsa])
    return rta


print(minimo_bolsas([4, 3, 3, 2, 2, 2, 1, 3, 2], 5))
