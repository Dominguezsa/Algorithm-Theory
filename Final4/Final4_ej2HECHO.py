"""Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una
misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso
está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, sólo
pueden pintar los colectivos de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren
parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber si es posible
cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color
coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué
líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
el problema. Indicar la complejidad del algoritmo implementado.

Parecido al problema del k-coloreo:


Función kColoreo(grafo, k):
    Si todos los vértices están coloreados:
        Retornar "Solución encontrada"

    Para cada vértice v en el grafo:
        Si v no está coloreado:
            Para cada color c de 1 a k:
                Si esSeguro(grafo, v, c):
                    AsignarColor(grafo, v, c)
                    Si kColoreo(grafo, k) retorna "Solución encontrada":
                        Retornar "Solución encontrada"
                    DesasignarColor(grafo, v)  # Retroceder si no se encontró una solución
    Retornar "No se encontró solución"

Función esSeguro(grafo, v, color):
    Para cada vértice adyacente u de v:
        Si u está coloreado y tiene el mismo color que v:
            Retornar Falso
    Retornar Verdadero

Función AsignarColor(grafo, v, color):
    Asignar el color 'color' al vértice v en el grafo

Función DesasignarColor(grafo, v):
    Desasignar el color del vértice v en el grafo
"""

def backtracking(vertices, pos_actual, grafo, guardados, k):
    if len(guardados) == len(grafo):
        return es_compatible(grafo, guardados)
    for i in range(k):
        guardado[vertices[pos_actual]] = i
        if not es_compatible_actual(grafo, actual, guardados):
            continue
        if backtrack(vertices, actual+1, grafo, guardados, k):
            return True
    guardados.pop(vertices[pos_actual])
    return False