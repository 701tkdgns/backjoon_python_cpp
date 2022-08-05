import heapq, sys
std = sys.stdin


def dijkstra(start):
    dp[start] = 0
    hq = []
    heapq.heappush(hq, [start, 0])
    while hq:
        destination, cost = heapq.heappop(hq)
        if dp[destination] < cost:
            continue
        for tmp_destination, tmp_cost in lst[destination]:
            best_cost = cost + tmp_cost
            if dp[tmp_destination] > best_cost:
                dp[tmp_destination] = best_cost
                heapq.heappush(hq, [tmp_destination, best_cost])


V, E = map(int, std.readline().split())
S = int(std.readline())
lst = [[] for _ in range(V + 1)]
INF = 10**10
dp = [INF for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, std.readline().split())
    lst[u].append([v, w])
dijkstra(S)
for i in range(1, V + 1):
    if dp[i] == 10**10:
        print("INF")
    else:
        print(dp[i])