"""Realizar un seguimiento de aplicar el Algoritmo de Huffman al texto “PRETERINTENCIONALIDAD”, indicando el
binario resultante de comprimirlo.

PASOS HUFFMAN:

1. Anotar cantidad de apariciones de las letras:

P -> 1
R -> 2
E -> 3
T -> 2
I -> 3
N -> 3
C -> 1
O -> 1
A -> 2
L -> 1
D -> 2


2. Hacer arbolito de Huffman


                         21
                        /  \
                      /     \
                    /        \
                   /          \
                 /             \
               /                \
            8                    \
          /   \                  13
        4      \              /    \
       / \      \            7      \
     /    \      \         /  \      \
   2      2       4       4    \      6
  / \   /  \    /  \    /  \    \   /  \
P1  C1 O1  L1  R2  T2  A2  D2  E3  I3  N3


3. Si es a la derecha es un 1, izquierda es 0

4. Las letras quedan:

"P": "0000",
"C": "0001",
"O": "0010",
"L": "0011",
"R": "010",
"T": "011",
"A": "1000",
"D": "1001",
"E": "101",
"I": "110",
"N": "111"

5. Binario queda:
0000 010 101 011 101 010 110 111 011 101 111 0001 110 0010 111 1000 0011 110 1001 1000 1001
"""


def preter(palabra):
    dic = {}
    for letra in palabra:
        dic[letra] = dic.get(letra, 0) + 1
    return dic


def huffman():
    palabra = "PRETERINTENCIONALIDAD"
    dic = {"P": "0000", "C": "0001", "O": "0010", "L": "0011", "R": "010", "T": "011", "A": "1000", "D": "1001",
           "E": "101", "I": "110", "N": "111"}
    rta = ""
    for letra in palabra:
        rta += str(dic.get(letra))
        rta += " "
    return rta


print(huffman())
