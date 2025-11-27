def tsp_dp(distance_matrix):
    """
    Traveling Salesman Problem using Dynamic Programming: Find minimum cost tour
    Time Complexity: O(n² * 2^n) | Space Complexity: O(n * 2^n)
    Bitmask DP approach
    """
    n = len(distance_matrix)
    # dp[mask][i] = minimum cost to visit all cities in mask, ending at city i
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    
    # Base case: starting from city 0
    dp[1][0] = 0
    
    # Iterate through all possible subsets of cities
    for mask in range(1 << n):
        # For each city as current position
        for u in range(n):
            # If city u is not in mask or cost is infinity, skip
            if dp[mask][u] == INF:
                continue
            
            # Try going to each unvisited city
            for v in range(n):
                # If city v not yet visited
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)  # Add v to visited set
                    # Update minimum cost to reach v
                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + distance_matrix[u][v]
                    )
    
    # Find minimum cost to visit all cities and return to city 0
    all_visited = (1 << n) - 1
    ans = INF
    
    for i in range(n):
        # Cost to visit all cities ending at i + return to city 0
        ans = min(ans, dp[all_visited][i] + distance_matrix[i][0])
    
    return ans

def tsp_brute_force(distance_matrix):
    """
    TSP Brute Force: Try all permutations (for verification with small n)
    Time Complexity: O(n!) | Space Complexity: O(n)
    """
    from itertools import permutations
    
    n = len(distance_matrix)
    min_cost = float('inf')
    best_tour = None
    
    # Generate all permutations of cities (excluding first city 0)
    for perm in permutations(range(1, n)):
        # Calculate cost of tour: 0 -> perm -> 0
        cost = distance_matrix[0][perm[0]]
        
        for i in range(len(perm) - 1):
            cost += distance_matrix[perm[i]][perm[i + 1]]
        
        cost += distance_matrix[perm[-1]][0]  # Return to city 0
        
        # Update if this tour is better
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(perm) + [0]
    
    return min_cost, best_tour

# Driver code
if __name__ == "__main__":
    # Distance matrix (symmetric)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    # DP approach
    min_cost_dp = tsp_dp(distance_matrix)
    print(f"TSP DP - Minimum cost: {min_cost_dp}")
    
    # Brute force approach
    min_cost_bf, tour = tsp_brute_force(distance_matrix)
    print(f"TSP Brute Force - Minimum cost: {min_cost_bf}")
    print(f"Best tour: {' -> '.join(map(str, tour))}")
