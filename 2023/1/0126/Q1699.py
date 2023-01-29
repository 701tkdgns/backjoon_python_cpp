N = int(input())
dp = [0 for _ in range(N + 1)]
for i in range(N + 1):
    dp[i] = i
for i in range(1, N + 1):
    for j in range(1, i + 1):
        if j ** 2 > i:
            break
        dp[i] = min(dp[i], dp[i - (j * j)] + 1)

print(dp[N])
