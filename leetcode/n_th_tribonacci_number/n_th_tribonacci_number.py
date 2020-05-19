def n_th_tribonacci_number(n):
    s = [0, 1, 1]
    for i in range(n-2):
        s.append(s[-1] + s[-2] + s[-3])
    return s[n]

print(n_th_tribonacci_number(4))
print(n_th_tribonacci_number(25))