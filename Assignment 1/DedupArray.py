
def dedup_array(arr):
    if not arr:
        return []
    last_unique = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] == last_unique:
            del arr[i]
        else:
            last_unique = arr[i]
            i += 1
    return arr
