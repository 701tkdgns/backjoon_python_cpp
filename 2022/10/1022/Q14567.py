N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
dp = [1 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)

for i in range(1, N + 1):
    for b in lst[i]:
        dp[b] = max(dp[b], dp[i] + 1)
print(*dp[1:])
