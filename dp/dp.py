def dp(n):
    if n <= 1:
        return n
    list = [0]*(n+1)
    list[1] = 1
    for i in range(2, n+1):
        list[i] = list[i-1] + list[i-2]

    return list

print(dp(10))


