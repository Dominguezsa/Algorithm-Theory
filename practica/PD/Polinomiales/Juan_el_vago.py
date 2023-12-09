"""Juan el vago no trabaja 2 días seguidos"""


def juan_el_vago(dias):
    dp = [0] * len(dias)
    dp[0] = dias[0]
    dp[1] = max(dias[0], dias[1])
    for i in range(2, len(dias)):
        dp[i] = max(dias[i] + dp[i - 2], dp[i - 1])
    return construir_elecciones(dp,dias)


def construir_elecciones(dp, dias):
    elecciones = []
    d = len(dp) - 1
    while (d > 1):
        if dias[d] + dp[d - 2] >= dp[d - 1]:
            elecciones.insert(0, d)
            d -= 2
        else:
            d -= 1
    if dp[1] == dias[1]:
        elecciones.insert(0, 1)
    else:
        elecciones.insert(0, 0)
    return elecciones


dia = [10, 2, 8, 10, 15]


print(juan_el_vago(dia))
