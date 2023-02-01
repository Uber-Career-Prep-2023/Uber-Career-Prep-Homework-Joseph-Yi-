# fixed size sliding window
# space complexity is O()
# time complexity is O()


def MaxMeanSubArray(arr, k):
    if k > len(arr):
        return -1

    max_mean = float("-inf")
    total = 0
    first = 0
    second = 0
    

    while second < len(arr):
        total += arr[second]

        if second - first + 1 == k:
            curr_mean = total / k
            max_mean = max(max_mean, curr_mean)
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
