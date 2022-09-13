import heapq, sys

inf = sys.maxsize


def dijkstra(start):
    hq = []
    dp[start] = 0
    heapq.heappush(hq, (start, 0))
    while hq:
        node, cost = heapq.heappop(hq)

        if node == g:
            break

        if dp[node] < cost:
            continue
        for new_node, tmp_cost in lst[node]:
            new_cost = tmp_cost + cost
            if dp[new_node] > new_cost:
                dp[new_node] = new_cost
                heapq.heappush(hq, [new_node, new_cost])


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    e = []
    dp = [inf for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        lst[a].append([b, d])
        lst[b].append([a, d])
    for _ in range(t):
        x = int(input())
        e.append(x)
    dijkstra(s)
    print(dp)