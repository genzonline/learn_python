#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
	counter = 0
	found = False
	a = None
	b = None
	while found == False:
		a = nums.pop(0)
		try:
			b = nums.index(target - a)
			return [counter, counter + b + 1]
			found = True
		except(ValueError):
			counter += 1