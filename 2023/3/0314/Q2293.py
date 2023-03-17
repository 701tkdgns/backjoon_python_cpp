N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
dp = [0 for _ in range(K + 1)]
dp[0] = 1
for i in range(N):
    for j in range(lst[i], K + 1):
        if j >= lst[i]:
            dp[j] += dp[j - lst[i]]
print(dp[K])