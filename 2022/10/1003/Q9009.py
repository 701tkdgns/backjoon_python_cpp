dp = [1, 2]
for i in range(2, 46):
    dp.append(dp[i-1]+dp[i-2])

t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    while n != 0:
        tmp = 0
        for k in range(46):
            if dp[k] <= n:
                tmp = dp[k]
        n -= tmp
        res.append(tmp)
    res.sort()
    print(*res)