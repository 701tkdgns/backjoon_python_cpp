import heapq, sys

input = sys.stdin.readline
inf = sys.maxsize


def dijkstra(v):
    hq = []
    dp[v][0] = 0
    heapq.heappush(hq, [0, v, 0])
    while hq:
        cnt, node, cost = heapq.heappop(hq)
        if dp[node][cnt] < cost:
            continue
        for new_node, new_cost in road[node]:
            if cost + new_cost < dp[new_node][cnt]:
                dp[new_node][cnt] = cost + new_cost
                heapq.heappush(hq, [cnt, new_node, new_cost])

            if cnt < K and dp[new_node][cnt + 1] > cost:
                dp[new_node][cnt + 1] = cost
                heapq.heappush(hq, [cnt + 1, new_node, cost])


N, M, K = map(int, input().split())
road = [[] for _ in range(N + 1)]
dp = [[inf for _ in range(K + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append([b, c])
    road[b].append([a, c])
dijkstra(1)
print(min(dp[N]))