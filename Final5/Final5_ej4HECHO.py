"""Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
Implementar un algoritmo que Greedy que dé la cantidad mínima de faros que se necesitan para que todos los
submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las
diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la
complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?

Se podria tratar de colocar los submarinos en las celdas que iluminan más submarinos, aunque no siempre da el optimo.
Si tengo una matriz de n x m, con s submarinos la complejidad es T(n) = O(n x m x s)
"""