def min_coins(sistema, dinero):
    dp = [0] * (dinero + 1)
    dp[0] = 0
    for i in range(1, dinero + 1):
        minimo = i  # usar todas monedas de 1
        for moneda in sistema:
            if moneda > i:
                continue
            cantidad = 1 + dp[i - moneda]
            if cantidad < minimo: minimo = cantidad
        dp[i] = minimo
    return dp[dinero]


# Ejemplo de uso
denominaciones = [1, 2, 5]
cantidad = 11
resultado = min_coins(denominaciones, cantidad)

print(resultado)
