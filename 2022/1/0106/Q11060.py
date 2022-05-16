N = int(input())
lst = list(map(int, input().split()))
dp = [-1 for _ in range(N)]
dp[0] = 0
for i in range(N-1):
    if dp[i] == -1:
        continue
    for j in range(1, lst[i]+1):
        if i + j < N:
            if dp[i+j] == -1 or dp[i+j] > dp[i] + 1:
                dp[i+j] = dp[i] + 1

print(dp[N-1])
