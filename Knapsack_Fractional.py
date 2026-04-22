# Time Complexity: O(n log n)

items = []
n = int(input("Enter number of items: "))

for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))
    items.append((value, weight))

capacity = int(input("Enter knapsack capacity: "))

items.sort(key=lambda x: x[0] / x[1], reverse=True)

total_value = 0
for value, weight in items:
    if capacity >=  weight:
        capacity -= weight
        total_value += value
    else:
        total_value += value * (capacity / weight)
        break

print("Maximum value:", total_value)


