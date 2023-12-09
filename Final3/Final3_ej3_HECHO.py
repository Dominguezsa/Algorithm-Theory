"""Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir
sangre tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede
recibir sangre de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las
cantidades de bolsas de sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB,
PO). Implementar un algoritmo greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede
hacerse). Indicar el orden del algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.

Prmero usamos bolsa AB, despues la A, despues la B, por ultimo la 0
"""