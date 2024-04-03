import heapq

def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp[v] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, tmp_cost in lst[node]:
            new_cost = tmp_cost * Oil[new_node - 1] + cost * Oil[node - 1]
            if dp[new_node] > new_cost:
                dp[new_node] = new_cost
                heapq.heappush(hq, [new_node, new_cost])


N, M = map(int, input().split())
Oil = list(map(int, input().split()))
lst = [[] for _ in range(N + 1)]
dp = [10e9 for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
dijkstra(1)
res = 0
print(dp)