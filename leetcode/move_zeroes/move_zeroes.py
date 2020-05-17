def move_zeroes(nums):
	c = nums.count(0)
	for i in range(c):
		nums.remove(0)
		nums.append(0)
	return nums