def valid_anagram(s, t):
	tmp = 0
	for i in s:
		if i in t:
			tmp = t.index(i)
			t = t[:tmp] + t[tmp+1:]
		else:
			return False

	return True

a = "amma"
b = "mama"
c = "omom"

print(valid_anagram(a,b))
print(valid_anagram(b,c))
print(valid_anagram(c,a))