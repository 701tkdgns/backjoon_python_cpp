import sys, heapq

std = sys.stdin


def dijkstra(start):
    dp[start] = 0
    hq = []
    heapq.heappush(hq, [start, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_destination, new_cost in lst[node]:
            best_cost = cost + new_cost
            if dp[new_destination] > best_cost:
                dp[new_destination] = best_cost
                heapq.heappush(hq, [new_destination, best_cost])


N, M = map(int, std.readline().split())
inf = 10 ** 10
lst, dp = [[] for _ in range(N + 1)], [inf for _ in range(N + 1)]
for _ in range(M):
    a_node, b_node, c = map(int, std.readline().split())
    lst[a_node].append([b_node, c])
    lst[b_node].append([a_node, c])
dijkstra(1)
print(dp[N])
