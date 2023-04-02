n, k = map(int, input().split())
lst = [0 for _ in range(n + 1)]
dp = [10001 for _ in range(k + 1)]
dp[0] = 0
for i in range(1, n + 1):
    lst[i] = int(input())
for i in range(1, n + 1):
    for j in range(lst[i], k + 1):
        if lst[i] <= j:
            dp[j] = min(dp[j - lst[i]] + 1, dp[j])

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])