import sys, heapq

inf = sys.maxsize


def dijkstra(v):
    hq = []
    heapq.heappush(hq, [v, 0])
    dp = [inf for _ in range(n + 1)]
    dp[v] = 0
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for new_node, new_cost in lst[node]:
            best_cost = new_cost + cost
            if dp[new_node] > best_cost:
                dp[new_node] = best_cost
                heapq.heappush(hq, [new_node, best_cost])
    return dp


T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    des = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        lst[a].append([b, d])
        lst[b].append([a, d])
    for _ in range(t):
        des.append(int(input()))
    _s = dijkstra(s)
    _g = dijkstra(g)
    _h = dijkstra(h)
    res = []
    for b in des:
        if _s[g] + _g[h] + _h[b] == _s[b] or _s[h] + _h[g] + _g[b] == _s[b]:
            res.append(b)
    res.sort()
    for w in res:
        print(w, end=" ")
    print()
