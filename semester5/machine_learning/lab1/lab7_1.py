def sum_1(n):
    res = 0
    for i in range(1, n + 1):
        res += 1 / (i**2)
    return res

def sum_2 (n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += j**i
    return res