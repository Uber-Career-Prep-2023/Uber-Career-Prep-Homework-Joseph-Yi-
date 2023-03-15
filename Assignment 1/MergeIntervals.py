# Sort then solve

# Time complexity is O(n)
# this function itterates through the list once and all 
# steps are bounded to that one itteration

# space complexity is O(n)
# Since the function returns a new array wiht the merged
# intervals, the size of that new array is dependent on the input
# and the upper bound is O(n)

# 	Aprroach
#	1. sort the list
#	2. check for any overlapping intervals and merge them and write over
#	   the old value
#	3. append any non overlapping intervals

# problem took me about 25 minutes

def mergeInterval(lst):
	if not lst:
		return []
    
    # sort the list
	lst.sort(key = lambda x : x[0])
	
	# set the starting interval
	merged = [lst[0]]

	for interval in lst[1:]:

		# compare if there is overlap
		if interval[0] <= merged[-1][1]:
			# merge the two intervals
			merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
		# append no overlap intervals
		else:
			merged.append(interval)
	return merged





# [(4, 8), (1, 3), (9, 12)]
print(mergeInterval([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))

# [(2, 10)]
print(mergeInterval([(5, 8), (6, 10), (2, 4), (3, 6)]))

# [(10, 12), (5, 6), (7, 9), (1, 3)]
print(mergeInterval([(10, 12), (5, 6), (7, 9), (1, 3)]))