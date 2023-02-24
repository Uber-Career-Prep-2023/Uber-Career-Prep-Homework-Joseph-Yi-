# Given an array of integers, count the number of subarrays that sum to zero.



def ZeroSumSubArrays(arr):

	# initialize a has table to keep track of cumulative sums
	# intialize zero to a value of 1 bc empty subarray has sum zero
	all_sums = {}

	cur_sum = 0
	count = 0

	for num in arr:
		cur_sum += num

		if cur_sum == 0:
			count += 1

		if cur_sum in all_sums:
			count += all_sums[cur_sum]
			all_sums[cur_sum] += 1

		else: 
			all_sums[cur_sum] = 1


	return count


print(ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7])) 
# 2


print(ZeroSumSubArrays([1, 8, 7, 3, 11, 9]))
# 0

print(ZeroSumSubArrays([8, -5, 0, -2, 3, -4]))
# 2

print('\n')


print(ZeroSumSubArrays([1, 2, -3, 3, -2, 1])) 
# 4

print(ZeroSumSubArrays([1, 2, 3, 4, 5])) 
# 0

print(ZeroSumSubArrays([0, 0, 0, 0, 0]))
# 15

print(ZeroSumSubArrays([2, 3, -2, 1, -3, 5, 6, -2, -1]))
# 7

print(ZeroSumSubArrays([-1, -1, 1, 1, -1, -1, 1, 1]))
# 10
