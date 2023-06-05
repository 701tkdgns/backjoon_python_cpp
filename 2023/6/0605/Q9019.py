from collections import deque
import sys

input = sys.stdin.readline


def bfs(A, B):
    dq = deque()
    dq.append([A, ""])
    while dq:
        v, s = dq.popleft()
        if v == B:
            return s
        v2 = (2 * v) % 10000
        if dp[v2] == 0:
            dq.append([v2, s + "D"])
            dp[v2] = 1
        v2 = (v - 1) % 10000
        if dp[v2] == 0:
            dq.append([v2, s + "S"])
            dp[v2] = 1
        v2 = (v * 10 + (v // 1000)) % 10000
        if dp[v2] == 0:
            dq.append([v2, s + "L"])
            dp[v2] = 1
        v2 = (v // 10 + (v % 10) * 1000) % 10000
        if dp[v2] == 0:
            dq.append([v2, s + "R"])
            dp[v2] = 1


for _ in range(int(input())):
    a, b = map(int, input().split())
    dp = [0 for _ in range(10001)]
    res = bfs(a, b)
    print(res)
