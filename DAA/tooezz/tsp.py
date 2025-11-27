# Traveling Salesperson (TSP) using DP + Bitmask
from functools import lru_cache

def tsp(cost):
    n = len(cost)

    @lru_cache(None)
    def visit(mask, pos):
        if mask == (1 << n) - 1:         # all cities visited
            return cost[pos][0]          # return to start

        ans = float('inf')
        for nxt in range(n):
            if not mask & (1 << nxt):    # if city not visited
                ans = min(ans, cost[pos][nxt] + visit(mask | (1 << nxt), nxt))
        return ans

    return visit(1, 0)                   # start at city 0

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

print(tsp(graph))
