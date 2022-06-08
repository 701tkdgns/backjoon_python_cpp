N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
for m in range(N):
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1 or (lst[i][m] == 1 and lst[m][j] == 1):
                lst[i][j] = 1

for i in lst:
    print(*i)
