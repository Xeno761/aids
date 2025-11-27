# Fractional Knapsack (Greedy)
def fractional_knapsack(values, weights, capacity):
    ratio = [(values[i]/weights[i], values[i], weights[i]) for i in range(len(values))]
    ratio.sort(reverse=True)  # sort by value/weight ratio

    total = 0
    for r, val, wt in ratio:
        if capacity == 0:
            break
        if wt <= capacity:             # take whole item
            total += val
            capacity -= wt
        else:                          # take fraction
            total += r * capacity
            capacity = 0

    return total

print(fractional_knapsack([60,100,120], [10,20,30], 50))
