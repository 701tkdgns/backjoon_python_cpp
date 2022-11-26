import heapq


def dijkstra(init_d, init_x, init_y):
    hq = []
    visit = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]
    visit[0][init_x][init_y] = True
    heapq.heappush(hq, [0, init_d, 0, init_x, init_y])
    while hq:
        v, d, c, x, y = heapq.heappop(hq)

        if x == door[0][0] and y == door[0][1]:
            return v

        if lst[x][y] == "!":
            nx, ny = direction[d][0] + x, direction[d][1] + y
            if 0 <= nx < N and 0 <= ny < N and not visit[c][nx][ny] and lst[nx][ny] != "*":
                heapq.heappush(hq, [v, d, c, nx, ny])
                visit[c][nx][ny] = True

            for i in range(1, 4, 2):
                nx, ny = direction[(d + i) % 4][0] + x, direction[(d + i) % 4][1] + y
                if 0 <= nx < N and 0 <= ny < N and not visit[0][nx][ny] and lst[nx][ny] != "*":
                    heapq.heappush(hq, [v + 1, d, 1, nx, ny])
                    visit[1][nx][ny] = True

        else:
            nx, ny = direction[d][0] + x, direction[d][1] + y
            if 0 <= nx < N and 0 <= ny < N and not visit[c][nx][ny] and lst[nx][ny] != "*":
                heapq.heappush(hq, [v, d, c, nx, ny])
                visit[c][nx][ny] = True

    return 2501


N = int(input())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
door = []
res = 2501
for i in range(N):
    lst.append(list(map(str, input().rstrip())))
    for j in range(len(lst[i])):
        if lst[i][j] == "#":
            door.append([i, j])
a, b = door.pop()
for i in range(4):
    res = min(res, dijkstra(i, a, b))
print(res)
