# Hash the elements

# Time complexity is O(n)
# we itterate through the entire array once
# and all opperations are dependent on the length of the array

# Space complexity is O(n)
# the number of mappings depend on the number of independent sums
# within the entire subarray. This is grows proportionally to the
# size of the entire array. 

# 	Approach
# 	1. 
# 

# This took me 21 min


def ZeroSumSubArrays(arr):

	# initialize a has table to keep track of cumulative sums
	all_sums = {}

	cur_sum = 0
	count = 0

	# iterates through all integers of the list
	for num in arr:

		# tallys concurrent sum
		cur_sum += num

		# increments when the sum is zero
		if cur_sum == 0:
			count += 1


		if cur_sum in all_sums:
			# increments by the tally of current sum
			count += all_sums[cur_sum]
			# increments the current sum by 1
			all_sums[cur_sum] += 1

		# creates a mapping for the new sum
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
