from collections import deque


def emoji(N):
    dp[1][0] = 0
    dq = deque([[1, 0]])
    while dq:
        s, c = dq.popleft()
        if dp[s][s] == -1:
            dp[s][s] = dp[s][c] + 1
            dq.append([s, s])
        if s + c <= N and dp[s + c][c] == -1:
            dp[s + c][c] = dp[s][c] + 1
            dq.append([s + c, c])
        if s - 1 >= 0 and dp[s - 1][c] == -1:
            dp[s - 1][c] = dp[s][c] + 1
            dq.append([s - 1, c])


S = int(input())
dp = [[-1 for _ in range(S + 1)] for _ in range(S + 1)]
res = -1
emoji(S)
for i in range(S + 1):
    if dp[S][i] != -1:
        if res == -1 or res > dp[S][i]:
            res = dp[S][i]
print(res)
