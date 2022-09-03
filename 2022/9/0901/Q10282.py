import heapq


def dijkstra(start):
    hq = []
    dp = [inf for _ in range(n + 1)]
    dp[start] = 0
    heapq.heappush(hq, [start, 0])
    while hq:
        node, cost = heapq.heappop(hq)
        if dp[node] < cost:
            continue
        for next_node, tmp_cost in lst[node]:
            next_cost = tmp_cost + cost
            if dp[next_node] > next_cost:
                dp[next_node] = next_cost
                heapq.heappush(hq, [next_node, next_cost])
    return dp


T = int(input())
inf = 10 ** 8
for _ in range(T):
    n, d, c = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        lst[b].append([a, s])
    dp = dijkstra(c)
    max_dp, cnt = 0, 0
    for i in dp:
        if i != inf:
            if max_dp < i:
                max_dp = i
            cnt += 1
    print(cnt, max_dp)