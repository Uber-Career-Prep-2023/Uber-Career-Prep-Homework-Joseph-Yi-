# Heap

# Time complexity is O(n log k) where there are n entries in k arrays
# The function uses a heap which processes in log k per opperation. There are
# a total of n opperations resulting in a O(n log k)

# Space complexity is O(n)
# The result matrix must store n entries

# This took me 24 min
import heapq

def MergeKSortedArrays(arrays):
    result = []
    heap = []

    # Initialize heap with the first element from each array
    for i, array in enumerate(arrays):
        if len(array) > 0:
            heap.append((array[0], i, 0))
    
    # Convert the list into a heap
    heapq.heapify(heap)
    
    while heap:
        val, array_index, element_index = heapq.heappop(heap)
        result.append(val)

        # Move to the next element in the array
        if element_index + 1 < len(arrays[array_index]):
            heapq.heappush(heap, (arrays[array_index][element_index + 1], array_index, element_index + 1))
    
    return result



print(MergeKSortedArrays([[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
