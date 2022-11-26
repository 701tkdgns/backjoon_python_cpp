import heapq


def dijkstra(init_x, init_y):
    hq = []
    heapq.heappush(hq, [0, 0, init_x, init_y])
    visit[init_x][init_y] = 0
    while hq:
        val, d, x, y = heapq.heappop(hq)
        if x == door[0][0] and y == door[0][1]:
            return val

        if lst[x][y] == "!":
            for i in range(1, 4, 2):
                nx, ny = x + direction[(d + i) % 4][0], y + direction[(d + i) % 4][1]
                if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and lst[nx][ny] != "*":
                    visit[nx][ny] = visit[x][y] + 1
                    heapq.heappush(hq, [val + 1, (d + i) % 4, nx, ny])

        else:
            nx, ny = direction[d][0] + x, direction[d][1] + y
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and lst[nx][ny] != "*":
                visit[nx][ny] = visit[x][y] + 1
                heapq.heappush(hq, [val, d, nx, ny])

            else:
                for i in range(4):
                    nx, ny = direction[(d + i) % 4][0] + x, direction[(d + i) % 4][1] + y
                    if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and lst[nx][ny] != "*":
                        visit[nx][ny] = visit[x][y] + 1
                        heapq.heappush(hq, [val, (d + i) % 4, nx, ny])


N = int(input())
lst = []
visit = [[-1 for _ in range(N)] for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 0, 1, 2, 3
door, mirror = [], []
for i in range(N):
    lst.append(list(map(str, input().rstrip())))
    for j in range(len(lst[i])):
        if lst[i][j] == "#":
            door.append([i, j])
a, b = door.pop()
res = dijkstra(a, b)
print(res)
