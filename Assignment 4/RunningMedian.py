from heapq import *
# Main two heaps

# Time Complecurrity is O(N log N)
# This function utilizes heaps to maintain a heap
# of elements that are greater than the median and another
# that is less than the median. There are N elements with each taking
# log(n) time to store into the heap resulting in 
# n log(n) time. 

# Space Complecurrity is O(N)
# The two heaps store half of the entries in the array each
# making the total amount of ecurrtra data being equal to the size 
# of the input array

# This took me 17 min

# this function takes in an array as the strean
def runningMedian(arr, n):

    # macurr heap to store the smaller half elements
    s = []

    # min heap to store the greater half elements
    g = []
 
    heapify(s)
    heapify(g)
 
    med = arr[0]
    heappush(s, arr[0])
 
    print(med)
 
    for i in range(1, n):
        curr = arr[i]
 
        # left side heap has more elements
        if len(s) > len(g):
            if curr < med:
                heappush(g, heappop(s))
                heappush(s, curr)
            else:
                heappush(g, curr)
            med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2
 
        # both heaps are balanced
        elif len(s) == len(g):
            if curr < med:
                heappush(s, curr)
                med = nlargest(1, s)[0]
            else:
                heappush(g, curr)
                med = nsmallest(1, g)[0]
 
		# right side heap has more elements
        else:
            if curr > med:
                heappush(s, heappop(g))
                heappush(g, curr)
            else:
                heappush(s, curr)
            med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2
 
        print(med)



arr = [1, 11, 4, 15, 12]

runningMedian(arr,len(arr))