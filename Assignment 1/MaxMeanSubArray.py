# fixed size sliding window
# space complexity is O()
# time complexity is O()


def MaxMeanSubArray(arr, k):
    if k > len(arr):
        return -1

    total = 0

    first = 0
    second = 0
    
