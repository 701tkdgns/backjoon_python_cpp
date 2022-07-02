# N = int(input())
# res = 0
# stk, lst = [], []
#
# for i in range(1, (N+1)):
#     h = int(input())
#     lst.append(h)
#
# for i in range(N):
#     while stk and stk[-1] <= lst[i]:
#         stk.pop()
#     stk.append(lst[i])
#     res += len(stk) - 1
# print(res)