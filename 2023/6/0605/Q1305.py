# #review 1786
#
# def makePi(p):
#     j = 0
#     tmp = [0 for _ in range(p)]
#     for i in range(1, len(p)):
#         while j > 0 and p[i] != p[j]:
#             j = tmp[j - 1]
#         if p[i] == p[j]:
#             j += 1
#             tmp[i] = j
#     return tmp
#
# def kmp(s, p):
#     cnt, j = 0, 0
#     pos = []
#     for i in range(len(s)):
#         while j > 0 and s[i] != p[j]:
#             j = pi[j - 1]
#         if s[i] == p[j]:
#             if j == len(p) - 1:
#                 cnt += 1
#                 pos.append(i - len(p) + 2)
#                 j = pi[j]
#             else:
#                 j += 1
#
#
# T = input()
# P = input()
# pi = makePi(P)

def makePI(p):
    tmp = [0 for _ in range(len(p))]
    j = 0
    for i in range(1, len(p)):
        while j > 0 and P[i] != P[j]:
            j = tmp[j - 1]
        if P[i] == P[j]:
            j += 1
            tmp[i] = j
    return tmp


L = int(input())
P = input()
pi = makePI(P)
print(len(P) - pi[-1])