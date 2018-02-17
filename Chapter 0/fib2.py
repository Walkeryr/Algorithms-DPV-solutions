def fib2(n):
    if n == 0:
        return 0

    f = list()

    f.append(0)
    f.append(1)

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    print(f)

    return f[n]
