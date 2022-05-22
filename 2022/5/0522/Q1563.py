# import sys
#
# sys.setrecursionlimit(100000)
#
#
# # 개근상을 받을 수 없는 경우 : 지각(L) 2번 이상, 결석(A) 3번 연속
#
# def dp(n, S):
#     global res
#     if n == 0:
#         res = (res + 1) % 1000000
#         return
#
#     for i in case:
#         if (i == 'L' and i in S) or (i == 'A' and len(S) >= 2 and S[-2] == S[-1] == 'A'):
#             continue
#         else:
#             dp(n - 1, S + i)
#
#
# if __name__ == "__main__":
#     N = int(input())
#     case = ['O', 'A', 'L']
#     res = 0
#     dp(N, '')
#     print(res)


import sys

sys.setrecursionlimit(100000)
std = sys.stdin.readline()


def dfs(day, late, absent):
    if late == 2 or absent == 3:
        return 0
    if day == n:
        return 1
    if dp[day][late][absent] == -1:
        attend = dfs(day + 1, late, 0) + dfs(day + 1, late + 1, 0) + dfs(day + 1, late, absent + 1)
        dp[day][late][absent] = attend
        return attend
    else:
        return dp[day][late][absent]


if __name__ == "__main__":
    n = int(std)
    dp = [[[-1 for absent in range(3)] for late in range(2)] for day in range(n + 1)]
    print(dfs(0, 0, 0)%1000000)