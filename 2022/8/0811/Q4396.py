n = int(input())
mine = []
lst = []
res = [['.' for _ in range(n)] for _ in range(n)]
chk = True
direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for _ in range(n):
    mine.append(list(map(str, input().rstrip())))
for _ in range(n):
    lst.append(list(map(str, input().rstrip())))

for x in range(n):
    for y in range(n):
        if mine[x][y] == '.' and lst[x][y] == 'x':
            cnt = 0
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx <n and 0 <= ny < n and mine[nx][ny] == "*":
                    cnt += 1
            res[x][y] = cnt
        if mine[x][y] == "*" and lst[x][y] == "x":
            for i in range(n):
                for j in range(n):
                    if mine[i][j] == "*":
                        res[i][j] = "*"

for i in range(n):
    for j in range(n):
        print(res[i][j], end='')
    print()