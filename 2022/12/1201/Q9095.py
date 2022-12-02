T = int(input())
dp = [0 for _ in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n = int(input())
    for i in range(4, n + 1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[n])

# 1 > 1
# 2 > 11, 2
# 3 > 111, 12, 21, 3
# 4 > 1111 112 121 211 22 31 13
# 5 > 11111 1112 1121 1211 2111 221 212 122 311 131 113 32 23

# 1
# 2
# 4
# 7
# 13
