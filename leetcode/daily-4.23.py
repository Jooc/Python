def waysToChange(n: int) -> int:
    coins = [25, 10, 5, 1]

    f = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            f[i] += f[i - coin]

    return f[n] % 1000000007


print(waysToChange(5))
