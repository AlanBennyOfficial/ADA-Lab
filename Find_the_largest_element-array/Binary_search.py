# Min time: O(1)
# Max time: O(log n)

arr = [1, 2, 3, 12, 423, 432, 3123, 34312]
# arr = list(map(int, input("Enter your number seperated my spaces: ").split()))

def binary_search(target, arr, i, j):
    mid = i+(j-i)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        return binary_search(target, arr, i, mid-1)
    else:
        return binary_search(target, arr, mid+1, j)

print(binary_search(12, sorted(arr), 0 , len(arr)))
print(sorted(arr))
