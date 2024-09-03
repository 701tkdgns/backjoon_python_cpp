import heapq


def dijkstra(start, n, lst):
    hq = []
    heapq.heappush(hq, [start, 0])
    dp = [float('inf') for _ in range(n + 1)]
    dp[start] = 0
    while hq:
        node, fare = heapq.heappop(hq)
        if dp[node] < fare:
            continue
        for new_node, new_fare in lst[node]:
            best_fare = fare + new_fare
            if dp[new_node] > best_fare:
                dp[new_node] = best_fare
                heapq.heappush(hq, [new_node, best_fare])
    return dp


def solution(n, s, a, b, fares):
    answer = float('inf')
    lst = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        lst[c].append([d, f])
        lst[d].append([c, f])
    dp_s = dijkstra(s, n, lst)
    dp_a = dijkstra(a, n, lst)
    dp_b = dijkstra(b, n, lst)
    for i in range(1, n + 1):
        answer = min(answer, dp_s[i] + dp_a[i] + dp_b[i])
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3