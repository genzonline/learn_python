def array_partition_i(nums):
	nums.sort()
	sum = 0
	for i in nums:
		sum += i
		nums.remove(i)
	return sum

a = [100, 123, 2222, 1]
print(array_partition_i(a))