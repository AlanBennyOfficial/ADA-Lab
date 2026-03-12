def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # The last i elements are already in place, so we skip them
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr