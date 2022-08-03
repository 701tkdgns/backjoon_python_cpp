import heapq


def dijkstra(k):
    dp[k] = 0
    hq = []
    heapq.heappush(hq, [k, 0])
    while hq:
        destination, cost = heapq.heappop(hq)
        if dp[destination] < cost:
            continue
        for tmp_destination, tmp_cost in lst[destination]:
            best_cost = tmp_cost + cost
            if dp[tmp_destination] > best_cost:
                dp[tmp_destination] = best_cost
                heapq.heappush(hq, [tmp_destination, best_cost])


V, E = map(int, input().split())
lst = [[] for _ in range(V + 1)]
inf = 10 ** 10
dp = [inf for _ in range(V + 1)]
K = int(input())  # start
for _ in range(E):
    u, v, w = map(int, input().split())
    lst[u].append([v, w])
for I in lst:
    I.sort()
dijkstra(K)
for i in range(1, V + 1):
    if dp[i] == 10**10:
        print("INF")
    else:
        print(dp[i])