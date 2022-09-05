import heapq, sys

inf = sys.maxsize
std = sys.stdin.readline


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp = [inf for _ in range(N + 1)]
    dp[v] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, tmp_cost in lst[node]:
            if dp[new_node] > tmp_cost + cost:
                dp[new_node] = tmp_cost + cost
                heapq.heappush(hq, [new_node, tmp_cost + cost])
    return dp


N, M, R = map(int, std().split())
item = list(map(int, std().split()))
lst = [[] for _ in range(N + 1)]
res = 0
for _ in range(R):
    a, b, s = map(int, std().split())
    lst[a].append([b, s])
    lst[b].append([a, s])
for idx in range(1, N + 1):
    distance = dijkstra(idx)
    tmp_sum = 0
    for i in range(1, N + 1):
        if distance[i] <= M:
            tmp_sum += item[i-1]
    res = res if res > tmp_sum else tmp_sum
print(res)
