def heapify(arr, n, i):
    # Assume the largest is the root
    largest = i
    # Index of the left child and right child
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a max heap
    i = n // 2 - 1
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

    # Extract elements from the heap one by one
    j = n - 1
    while j > 0:
        # Move current root to the end
        arr[j], arr[0] = arr[0], arr[j]
        # Heapify the reduced heap
        heapify(arr, j, 0)
        j -= 1

# Random Array
arr = [12, 11, 13, 5, 6, 12,234,-2, 7]
print("Random Array ", arr)
heapsort(arr)
print("Sorted array :", arr)
