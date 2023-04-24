# def make_table():
#     tmp = [0 for _ in range(len(P))]
#     j = 0
#     for i in range(1, len(P)):
#         while j > 0 and P[i] != P[j]:
#             j = tmp[j - 1]
#         if P[i] == P[j]:
#             j += 1
#             tmp[i] = j
#     return tmp
#
#
# def KMP():
#     cnt = 0
#     pos = []
#     j = 0
#     for i in range(len(T)):
#         while j > 0 and T[i] != P[j]:
#             j = table[j - 1]
#         if T[i] == P[j]:
#             if j == len(P) - 1:
#                 cnt += 1
#                 pos.append(i - len(P) + 2)
#             else:
#                 j += 1
#     return cnt, pos
#
#
# T = input()
# P = input()
# table = make_table()
# ans, position = KMP()
# print(ans)
# print(position)
