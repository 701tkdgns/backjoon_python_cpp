def tsp(visited: int, current_city: int):
    if visited == (1 << N) - 1:
        return W[current_city][0] if W[current_city][0] > 0 else float('inf')

    if dp[visited][current_city] != -1:
        return dp[visited][current_city]

    min_cost = float('inf')

    for next_city in range(N):
        if not visited & (1 << next_city) and W[current_city][next_city] > 0:
            cost = W[current_city][next_city] + tsp(visited | (1 << next_city), next_city)
            min_cost = min(min_cost, cost)
    dp[visited][current_city] = min_cost
    return min_cost

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(1 << N)]
tsp(1, 0)
for d in dp:
    print(*d)

