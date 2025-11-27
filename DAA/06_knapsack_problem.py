class Item:
    """Class to represent an item with weight and value"""
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # Value-to-weight ratio

def knapsack_greedy(items, capacity):
    """
    0/1 Knapsack using Greedy Method: Sort by value/weight ratio
    Time Complexity: O(n log n) for sorting | Space Complexity: O(n)
    Note: Greedy gives approximate solution, DP gives optimal
    """
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0  # Track total value
    total_weight = 0  # Track total weight
    selected_items = []  # Store selected items
    
    # Greedily select items with best ratio that fit
    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
            selected_items.append(item)
    
    return total_value, total_weight, selected_items

def knapsack_dp(weights, values, capacity):
    """
    0/1 Knapsack using Dynamic Programming: OPTIMAL SOLUTION
    Time Complexity: O(n * W) where W is capacity | Space Complexity: O(n * W)
    """
    n = len(weights)
    # Create DP table: dp[i][w] = max value with i items and capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Current item's weight and value
            current_weight = weights[i - 1]
            current_value = values[i - 1]
            
            # If current item can fit in knapsack
            if current_weight <= w:
                # Take maximum of including or excluding current item
                dp[i][w] = max(
                    current_value + dp[i - 1][w - current_weight],  # Include
                    dp[i - 1][w]  # Exclude
                )
            else:
                # Cannot fit, exclude current item
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Driver code
if __name__ == "__main__":
    # Greedy approach example
    items = [Item(2, 10), Item(3, 20), Item(4, 30), Item(5, 40)]
    capacity = 8
    
    value, weight, selected = knapsack_greedy(items, capacity)
    print("Greedy Knapsack:")
    print(f"Max Value: {value}, Total Weight: {weight}")
    
    # DP approach example
    weights = [2, 3, 4, 5]
    values = [10, 20, 30, 40]
    max_value = knapsack_dp(weights, values, capacity)
    print(f"\nDP Knapsack (Optimal): Max Value = {max_value}")
