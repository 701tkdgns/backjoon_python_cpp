import copy, sys
sys.setrecursionlimit(10**6)


N = int(input())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
res = 0
for i in range(N):
    lst.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        res = max(res, dfs(i, j))
print(res)