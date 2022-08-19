import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v):



N = int(input())
lst = []
res = []
for i in range(1, N + 1):
    lst.append([i, int(input())])
for i in range(1, N + 1):

