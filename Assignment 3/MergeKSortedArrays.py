# Heap

# Time complexity is O(n log k) where there are n entries in k arrays
# 

# Space complexity is 
import heapq

def merge_k_sorted_arrays(arrays):
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
