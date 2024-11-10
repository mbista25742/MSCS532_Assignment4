import random
import timeit

# Heapsort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure time for each sorting algorithm
def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr.copy())
    return timeit.default_timer() - start_time

# Run comparisons
sizes = [1000, 5000, 10000]
input_types = ["random", "sorted", "reverse-sorted"]

for size in sizes:
    print(f"\nArray size: {size}")
    for input_type in input_types:
        # Generate the array based on input type
        if input_type == "random":
            arr = [random.randint(1, 10000) for _ in range(size)]
        elif input_type == "sorted":
            arr = list(range(size))
        elif input_type == "reverse-sorted":
            arr = list(range(size, 0, -1))

        # Measure and print time taken for each algorithm
        time_heapsort = measure_time(heapsort, arr)
        time_quicksort = measure_time(quicksort, arr)
        time_mergesort = measure_time(merge_sort, arr)

        print(f"{input_type.capitalize()} data:")
        print(f"Heapsort: {time_heapsort:.5f} seconds")
        print(f"Quicksort: {time_quicksort:.5f} seconds")
        print(f"Merge Sort: {time_mergesort:.5f} seconds")
