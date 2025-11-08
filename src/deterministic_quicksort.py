def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i - 1

def deterministic_quicksort(arr, low, high):
    while low < high:
        p = deterministic_partition(arr, low, high)

        # Recurse on smaller side first to limit recursion depth
        if p - low < high - p:
            deterministic_quicksort(arr, low, p - 1)
            low = p + 1
        else:
            deterministic_quicksort(arr, p + 1, high)
            high = p - 1


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original:", arr)
    deterministic_quicksort(arr, 0, len(arr)-1)
    print("Sorted:", arr)
