import heapq, sys


def dijkstra(start):
    dp[start] = 0
    hq = []
    heapq.heappush(hq, [start, 0])
    while hq:
        destination, cost = heapq.heappop(hq)
        if dp[destination] < cost:
            continue
        for tmp_cost, tmp_destination in lst[destination]:
            best_cost = cost + tmp_cost
            if dp[tmp_destination] > best_cost:
                dp[tmp_destination] = best_cost
                heapq.heappush(hq, [tmp_destination, best_cost])


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
inf = 10 ** 10
lst = [[] for _ in range(N + 1)]
dp = [inf for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    lst[a].append([c, b])
start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(dp[end])
