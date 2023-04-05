N = int(input())
lst = []
dp = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break
        if j + lst[i][j] < N:
            dp[i][j + lst[i][j]] = dp[i][j + lst[i][j]] + dp[i][j]

        if i + lst[i][j] < N:
            dp[i + lst[i][j]][j] = dp[i + lst[i][j]][j] + dp[i][j]

