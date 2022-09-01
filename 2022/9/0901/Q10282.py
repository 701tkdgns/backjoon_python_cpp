import heapq


def dijkstra(node):
    hq = []
    dp[node] = 0
    heapq.heappush(hq, [node, 0])
    while hq:
        now, wei = heapq.heappop(hq)
        if wei > dp[now]:
            continue
        for next_node, tmp_wei in lst[now]:
            next_wei = wei + tmp_wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(hq, [next_node, next_wei])


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        lst[a].append([b, s])
    dijkstra(c)
    print(sum(dp), max(dp))