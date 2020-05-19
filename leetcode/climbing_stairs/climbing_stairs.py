def climbing_stairs(n):
    s = [1, 1, 2]
    for i in range(n - 2):
        s.append(s[-1] + s[-2])
    return s[n]