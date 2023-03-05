








# # 합, 연산자, 다음 숫자, 순서, 표현식
# def dfs(_sum, sign, _num, cnt, s):
#     if cnt == N:
#         _sum = _sum + (sign * _num)
#         if _sum == 0:
#             print(s)
#     else:
#         dfs(_sum, sign, _num * 10 + (cnt + 1), cnt + 1, s + ' ' + str(cnt + 1))
#         dfs(_sum + sign * _num, 1, cnt + 1, cnt + 1, s + '+' + str(cnt + 1))
#         dfs(_sum + sign * _num, -1, cnt + 1, cnt + 1, s + '+' + str(cnt + 1))
#
#
# t = int(input())
# for _ in range(t):
#     N = int(input())
#     dfs(0, 1, 1, 1, '1')
#     print()
