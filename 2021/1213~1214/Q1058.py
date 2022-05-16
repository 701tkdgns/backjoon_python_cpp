N = int(input())
lst, visited = [], [[0] * N for _ in range(N)]
for _ in range(N):
    lst.append(list(''.join(input())))

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            if lst[j][k] == 'Y' or (lst[j][i] == 'Y' and lst[i][k] == 'Y'):
                visited[j][k] = 1

res = 0

for i in visited:
    res = max(res, sum(i))
print(res)
