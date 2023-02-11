# https://mong9data.tistory.com/68

n, k = map(int, input().split())
lst, dp = [int(input()) for _ in range(n)], [0 for _ in range(k + 1)]
dp[0] = 1
for i in range(n):
    for j in range(lst[i], k + 1):
        if j >= lst[i]:
            dp[j] += dp[j - lst[i]]
        print(dp)
    print()