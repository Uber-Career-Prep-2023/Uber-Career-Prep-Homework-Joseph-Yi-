# fixed size sliding window

# space complexity is O(1) the only extra space that is created is a constant 
# amount of variables which is independent of the size of the array

# time complexity is O(n) with n being the number of entires in the array

#   Notes
#   used kadane algorithm for this approach
#   1. itterate through the list keeping track of local max
#   2. update the global max when found

# this problem took me about 10 min to write

def MaxMeanSubArray(arr, k):
    if k > len(arr):
        return -1

    max_mean = float("-inf")
    total = 0
    first = 0
    second = 0

    # itterates through the 
    while second < len(arr):
        total += arr[second]

        # once window is correct size
        if second - first + 1 == k:
            # calculate mean
            curr_mean = total / k

            # calculate new max mean
            max_mean = max(max_mean, curr_mean)

            # decrease total by the first element in window
            total -=arr[first]
            first += 1
        second += 1

    return max_mean

def main():
    arr = [4, 5, -3, 2, 6, 1]
    k = 2
    print(MaxMeanSubArray(arr, k))

    arr = [4, 5, -3, 2, 6, 1]
    k = 3
    print(MaxMeanSubArray(arr, k))

    arr = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
    k = 3
    print(MaxMeanSubArray(arr, k))

    arr = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
    k = 4
    print(MaxMeanSubArray(arr, k))

if __name__ == "__main__":
    main()
