# # N = int(input())
# # lst = []
# # for _ in range(N):
# #     a, b = map(int, input().split())
# #     lst.append([a, b])
# # lst.sort(reverse=True)
# # max_x, max_y = lst[0][0], lst[0][1]
# # res = 1
# # for i in range(1, N):
# #     if lst[i][0] <= max_x and lst[i][1] <= max_y:
# #         res += 1
# #         max_x, max_y = lst[i][0], lst[i][1]
# #     elif lst[i][1] <= max_x and lst[i][0] <= max_y:
# #         res += 1
# #         max_x, max_y = lst[i][0], lst[i][1]
# # print(res)
#
# N = int(input())
# lst = []
# dp = [1 for _ in range(N)]
# for _ in range(N):
#     lst.append(sorted(list(map(int, input().split()))))
# lst.sort()
# for i in range(1, N):
#     for j in range(i):
#         if lst[i][1] >= lst[j][1]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

N = int(input())
lst = []
dp = [1 for _ in range(N)]
for _ in range(N):
    lst.append(sorted(list(map(int, input().split()))))
lst.sort()
for i in range(1, N):
    for j in range(i):
        if lst[i][1] >= lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))