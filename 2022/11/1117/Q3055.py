from collections import deque


def water():
    for _ in range(len(wat)):
        x, y = wat.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if not lst[nx][ny] == "X":
                    lst[nx][ny] = "*"
                    wat.append([nx, ny])


def bfs(init_x, init_y):
    bibi = deque()
    bibi.append([init_x, init_y])
    visit[init_x][init_y] = 0
    while bibi:
        x, y = bibi.popleft()
        if x == e[0] and y == e[1]:
            return True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and (lst[nx][ny] == "." or lst[nx][ny] == "S"):
                visit[nx][ny] = visit[x][y] + 1
                bibi.append([nx, ny])

        water()

    return False


R, C = map(int, input().split())
lst = []
B, wat = [], deque()
e = []
for i in range(R):
    lst.append(list(map(str, input().rstrip())))
    for j in lst[i]:
        if j == "D":
            B = [i, lst[i].index("D")]
        elif j == "*":
            wat.append([i, lst[i].index("*")])
        elif j == "S":
            e = [i, lst[i].index("S")]

visit = [[-1 for _ in range(C)] for _ in range(R)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

water()
res = bfs(B[0], B[1])

if res:
    print(visit[e[0]][e[1]])
else:
    print("KAKTUS")
