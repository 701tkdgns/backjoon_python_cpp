import sys

N = int(input())
M = int(input())
lst = [[sys.maxsize for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    i, j, c = map(int, input().split())
    if lst[i][j] > c:
        lst[i][j] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i!=j and lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if lst[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(lst[i][j], end=" ")
    print()
