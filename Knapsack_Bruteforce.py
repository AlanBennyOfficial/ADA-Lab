from itertools import combinations

weights = [7,3,4,5]
values = [42,12,40,25]
capacity = 10
n = len(weights)

best_value = 0
best_subset = None

print("Subset\t\tTotal Value")
print("-"*45)

for r in range(n+1):
    for subset in combinations(range(n),r):
        total_weight = sum(weights[i] for i in subset)
        total_value = sum(values[i] for i in subset)

        subset_display = "{" + ",".join(str(i+1) for i in subset) + "}"

        if total_weight <= capacity:
            print(f"{subset_display:<15}{total_weight:<15}${total_value}")
            
            if total_value > best_value:
                best_value = total_value
                best_subset = subset
            
        else:
            print(f"{subset_display:<15}{total_weight:<15}not feasible")

print("Optimal Solution:")
print("Items selected:", {i+1 for i in best_subset})
print("Maximum value: $", best_value)


# OUTPUT:

# Subset          Total Value
# ---------------------------------------------
# {}             0              $0
# {1}            7              $42
# {2}            3              $12
# {3}            4              $40
# {4}            5              $25
# {1,2}          10             $54
# {1,3}          11             not feasible
# {1,4}          12             not feasible
# {2,3}          7              $52
# {2,4}          8              $37
# {3,4}          9              $65
# {1,2,3}        14             not feasible
# {1,2,4}        15             not feasible
# {1,3,4}        16             not feasible
# {2,3,4}        12             not feasible
# {1,2,3,4}      19             not feasible
# Optimal Solution:
# Items selected: {3, 4}
# Maximum value: $ 65