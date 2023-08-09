from heapq import *
# Main two heaps

# Time Complexity is O(N log N)
# 

# Space Complexity is O(N)
# 

# This took me 17 min

# this function takes in an array as the strean
def runningMedian(arr, n):

    # max heap to store the smaller half elements
    s = []

    # min heap to store the greater half elements
    g = []
 
    heapify(s)
    heapify(g)
 
    med = arr[0]
    heappush(s, arr[0])
 
    print(med)
 
    for i in range(1, n):
        x = arr[i]
 
        # left side heap has more elements
        if len(s) > len(g):
            if x < med:
                heappush(g, heappop(s))
                heappush(s, x)
            else:
                heappush(g, x)
            med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2
 
        # both heaps are balanced
        elif len(s) == len(g):
            if x < med:
                heappush(s, x)
                med = nlargest(1, s)[0]
            else:
                heappush(g, x)
                med = nsmallest(1, g)[0]
 
		# right side heap has more elements
        else:
            if x > med:
                heappush(s, heappop(g))
                heappush(g, x)
            else:
                heappush(s, x)
            med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2
 
        print(med)



arr = [1, 11, 4, 15, 12]

runningMedian(arr,len(arr))