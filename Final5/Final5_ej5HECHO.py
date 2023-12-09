"""El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1, P2,
..., Pc de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que
ningún par de ellos compartan ningún nodo?

Demostrar que Path Selection es un problema NP-Completo. Ayuda: este problema tiene mucha semejanza con
Independent Set. Recomandamos reducir dicho problema a Path Selection.


RESPUESTA:

Para reducirlo a Independent Set cada pedido, que es un conjunto de nodos, se lo debe tomar como un super nodo,
y va a tener como arista todos aquellos supernodos con los que compartaa por lo menos un nodo.
"""