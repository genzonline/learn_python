def fizz_buzz(n):
	for i in range(n):
		if (i + 1) % 3 == 0:
			if (i + 1) % 5 == 0:
				print("FizzBuzz")
			else:
				print("Fizz")
		elif (i + 1) % 5 == 0:
			print("Buzz")
		else:
			print(i + 1)

fizz_buzz(15)