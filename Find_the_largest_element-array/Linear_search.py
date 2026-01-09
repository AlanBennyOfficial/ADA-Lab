# Min time: O(1)
# Max time: O(n)

# arr = [12, 34312,3,423,432,1,2,3123,12]
arr = list(map(int, input("Enter your number seperated my spaces: ").split()))

max = 0
for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]

print(max)