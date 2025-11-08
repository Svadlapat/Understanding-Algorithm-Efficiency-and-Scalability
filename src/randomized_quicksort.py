import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, p-1)
        randomized_quicksort(arr, p+1, high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original:", arr)
    randomized_quicksort(arr, 0, len(arr)-1)
    print("Sorted:", arr)
