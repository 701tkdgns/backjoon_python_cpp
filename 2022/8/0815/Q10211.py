T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = lst[0]
    for i in range(1, N):
        if dp[i - 1] + lst[i] > lst[i]:
            dp[i] = dp[i - 1] + lst[i]
        else:
            dp[i] = lst[i]
    print(max(dp))
