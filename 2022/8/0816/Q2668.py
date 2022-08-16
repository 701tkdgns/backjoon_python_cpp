import sys

sys.setrecursionlimit(10 ** 6)


def dfs():
    pass


N = int(input())
lst = []
for i in range(1, N + 1):
    lst.append([i, int(input())])
for i in range(1, N + 1):
    dfs()