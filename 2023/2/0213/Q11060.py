# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
#
# def dfs(v):
#     direction = [i for i in range(lst[v] + 1)]
#     print(direction)
#     for i in direction:
#         if v + i < n and dp[v + i] == -1:
#             dp[v + i] = dp[v] + 1
#             dfs(v + i)

from collections import deque


def bfs(v):
    dq = deque([v])
    dp[v] = 0
    while dq:
        v = dq.popleft()
        for i in range(lst[v] + 1):
            if i + v < n and dp[v + i] == -1:
                dp[v + i] = dp[v] + 1
                dq.append(v + i)


n = int(input())
lst = list(map(int, input().split()))
dp = [-1 for _ in range(n)]
bfs(0)
print(dp[n - 1])
