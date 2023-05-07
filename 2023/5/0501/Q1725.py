# # n = int(input())
# # lst = [int(input()) for _ in range(n)]
# # lst.append(0)
# # res = -1
# # stk = [[0, lst[0]]]
# # for i in range(1, n + 1):
# #     left = i
# #     while stk and stk[-1][1] > lst[i]:
# #         left, h = stk.pop()
# #         res = max(res, (i - left) * h)
# #     stk.append([left, lst[i]])
# # print(res)
#
# n = int(input())
# lst = [int(input()) for _ in range(n)]
# lst.append(0)
# res = -1
# stk = [[0, lst[0]]]
# for i in range(1, n + 1):
#     left = i
#     while stk and stk[-1][1] > lst[i]:
#         left, h = stk.pop()
#         res = max(res, (i - left) * h)
#     stk.append([left, lst[i]])
# print(res)


n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.append(0)
stk = [[0, lst[0]]]
res = -1
for i in range(1, n + 1):
    left = i
    while stk and stk[-1][1] > lst[i]:
        left, height = stk.pop()
        res = max(res, (i - left) * height)
    stk.append([left, lst[i]])
print(res)