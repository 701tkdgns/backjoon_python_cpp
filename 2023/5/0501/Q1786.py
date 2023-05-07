# # # https://bowbowbow.tistory.com/6
# # # https://hooongs.tistory.com/305
# #
# #
# # def make_table(_p):
# #     tmp = [0] * len(_p)
# #     j = 0
# #     for i in range(1, len(_p)):
# #         while j > 0 and _p[i] != _p[j]:
# #             j = tmp[j - 1]
# #         if _p[i] == _p[j]:
# #             j += 1
# #             tmp[i] = j
# #     return tmp
# #
# #
# # def kmp(_s, _p):
# #     cnt = 0
# #     pos = []
# #     j = 0
# #     for i in range(len(_s)):
# #         while j > 0 and _s[i] != _p[j]:
# #             j = table[j - 1]
# #         if _s[i] == _p[j]:
# #             if j == len(p) - 1:
# #                 cnt += 1
# #                 pos.append(i - len(p) + 2)
# #                 j = table[j]
# #             else:
# #                 j += 1
# #     return cnt, pos
# #
# #
# # s = input()
# # p = input()
# # table = make_table(p)
# # res, positions = kmp(s, p)
# # print(res)
# # print(*positions)
#
# def makeTable(p):
#     tmp = [0 for _ in range(len(p))]
#     j = 0
#     for i in range(1, len(p)):
#         while j > 0 and p[i] != p[j]:
#             j = tmp[j - 1]
#         if p[i] == p[j]:
#             j += 1
#             tmp[i] = j
#
#     return tmp
#
# def kmp(s, p):
#     pass
#
#
# s = input()
# p = input()
# table = makeTable(p)
# print(table)
# # res, positions = kmp(s, p)
# # print(res)
# # print(*positions)















