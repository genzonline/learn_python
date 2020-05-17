def single_number(s):
	for i in s:
		if s.count(i) == 1:
			return i