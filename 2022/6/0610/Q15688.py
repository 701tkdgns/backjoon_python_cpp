# sys.setrecursionlimit(100000)
#
#
# def qsort(L):
#     if len(L) <= 1:
#         return L
#     p = L[0]
#     l, r = [], []
#     for i in range(1, len(L)):
#         if p > L[i]:
#             l.append(L[i])
#         else:
#             r.append(L[i])
#     return qsort(l) + [p] + qsort(r)

import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
for i in sorted(lst):
    print(i)