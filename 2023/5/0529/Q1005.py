import heapq, sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    inDegree = [0 for _ in range(n + 1)]
    lst = [[] for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        lst[a].append(b)
        inDegree[b] += 1
    w = int(input())
    hq = []
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            dp[i] = time[i]
            heapq.heappush(hq, i)
    while hq:
        t = heapq.heappop(hq)
        for i in lst[t]:
            inDegree[i] -= 1
            dp[i] = max(dp[t] + time[i], dp[i])
            if inDegree[i] == 0:
                heapq.heappush(hq, i)
    print(dp[w])
