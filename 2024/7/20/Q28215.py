N, K = map(int, input().split())
bags, dp = [], [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for _ in range(N):
    w, v = map(int, input().split())
    bags.append([w, v])
bags.sort(key=lambda x: (x[0], x[1]))
for i in range(1, N + 1):
    m, v = bags[i-1][0], bags[i-1][1]
    for k in range(1, K + 1):
        if m <= k:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-m] + v)
        else:
            dp[i][k] = dp[i-1][k]
for d in dp:
    print(*d)

# N, K = map(int, input().split())
# bags = []
# for _ in range(N):
#     m, v = map(int, input().split())
#     bags.append([m, v])
# bags.sort(key=lambda x: (x[0], -x[1]))
# dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# for idx in range(N):
#     w, v = bags[idx][0], bags[idx][1]
#     for k in range(1, K + 1):
#         if w <= k:
#             dp[idx][k] = max(dp[idx - 1][k], dp[idx - 1][k - w] + v)
#         else:
#             dp[idx][k] = dp[idx - 1][k]
# for d in dp:
#     print(*d)

# https://www.acmicpc.net/problem/12865
