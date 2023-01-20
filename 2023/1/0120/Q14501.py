def dynamic():
    dl = 0
    for i in range(N - 1, -1, -1):
        dl = i + T[i]
        if dl > N:
            dp[i] = dp[i + 1]
        else:
            dp[i] = dp[i + 1] if dp[i + 1] > dp[dl] + P[i] else dp[dl] + P[i]


N = int(input())
T, P = [], []
dp = [0 for _ in range(N + 1)]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dynamic()
print(dp[0])