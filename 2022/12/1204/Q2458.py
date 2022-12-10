import sys

N, M = map(int, input().split())
lst = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if lst[i][j] == 1 or (lst[i][k] == 1 and lst[k][j] == 1):
                lst[i][j] = 1

res = 0
for i in range(1, N + 1):
    h = 0
    for j in range(1, N + 1):
        h += lst[i][j] + lst[j][i]
    if h == N - 1:
        res += 1
print(res)