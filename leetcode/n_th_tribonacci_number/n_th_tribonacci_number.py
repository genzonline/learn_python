def n_th_tribonacci_number(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return n_th_tribonacci_number(n - 3) + n_th_tribonacci_number(n - 2) + n_th_tribonacci_number(n - 1)

print(n_th_tribonacci_number(4))
print(n_th_tribonacci_number(25))