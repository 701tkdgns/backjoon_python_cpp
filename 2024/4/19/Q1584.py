import heapq


def check_space(x, y):
    if x == 0 and y == 0:
        return 0
    if lst[x][y] == -2:
        return 1
    else:
        return 2


def escape(_x, _y):
    visit[_x][_y] = 0
    hq = []
    heapq.heappush(hq, [_x, _y])
    while hq:
        x, y = heapq.heappop(hq)
        c = check_space(x, y)
        if c == 0:
            for dx, dy in direction:
                nx, ny = dx + x, dy + y
                if 0 <= nx < 501 and 0 <= ny < 501 and visit[nx][ny] == -1 and lst[nx][ny] != -3:
                    if lst[nx][ny] == -2:
                        visit[nx][ny] = visit[x][y] + 1
                        heapq.heappush(hq, [nx, ny])
                    else:
                        visit[nx][ny] = visit[x][y]
                        heapq.heappush(hq, [nx, ny])
        elif c == 1:
            for dx, dy in direction:
                nx, ny = dx + x, dy + y
                if 0 <= nx < 501 and 0 <= ny < 501 and visit[nx][ny] == -1 and lst[nx][ny] != -3:
                    visit[nx][ny] = visit[x][y] + 1
                    heapq.heappush(hq, [nx, ny])
        else:
            for dx, dy in direction:
                nx, ny = dx + x, dy + y
                if 0 <= nx < 501 and 0 <= ny < 501 and visit[nx][ny] == -1 and lst[nx][ny] != -3:
                    if lst[nx][ny] == -2:
                        visit[nx][ny] = visit[x][y] + 1
                        heapq.heappush(hq, [nx, ny])
                    else:
                        visit[nx][ny] = visit[x][y]
                        heapq.heappush(hq, [nx, ny])


lst = [[0 for _ in range(501)] for _ in range(501)]
visit = [[-1 for _ in range(501)] for _ in range(501)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

danger = int(input())
for _ in range(danger):
    x1, y1, x2, y2 = map(int, input().split())
    lst[x1][y1] = -2
    lst[x2][y2] = -2
death = int(input())

for _ in range(death):
    x1, y1, x2, y2 = map(int, input().split())
    lst[x1][y1] = min(lst[x1][y1], -2)
    lst[x2][y2] = min(lst[x2][y2], -3)
escape(0, 0)
print(visit[500][500])
