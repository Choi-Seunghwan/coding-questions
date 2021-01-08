memo = {}


def fibo(n):
    if n <= 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibo(n - 2) + fibo(n - 1)
    return memo[n]


for i in range(1, 25 + 1):
    print(i, fibo(i))
