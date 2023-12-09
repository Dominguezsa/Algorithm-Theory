def el_lunatico(valores):
    dp1 = [0] * (len(valores) - 1)
    dp1[0] = valores[0]
    dp1[1] = max(dp1[0], valores[1])

    dp2 = [0] * (len(valores))
    dp2[1] = valores[1]
    dp2[2] = max(dp2[1], valores[2])

    for i in range(2, len(valores) - 1):
        dp1[i] = max(valores[i] + dp1[i - 2], valores[i - 1])
    for j in range(3, len(valores)):
        dp2[j] = max(valores[j] + dp2[j - 2], valores[j - 1])
    return dp1, dp2


print(el_lunatico([5, 4, 7, 9]))
