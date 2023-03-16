N, K = map(int, input().split())
dp = [0 for _ in range(K + 1)]
lst = []
dp[0] = 1
for _ in range(N):
    lst.append(int(input()))

for i in range(N):
    for j in range(lst[i], K + 1):
        if j >= lst[i]:
            dp[j] += dp[j - lst[i]]

    print(dp)

# n, k = map(int, input().split())
# lst = []
# dp = [0 for _ in range(k + 1)]
# dp[0] = 1
# for _ in range(n):
#     lst.append(int(input()))
#
# for i in range(n):
#     for j in range(lst[i], k + 1):
#         if j >= lst[i]:
#             dp[j] += dp[j - lst[i]]
