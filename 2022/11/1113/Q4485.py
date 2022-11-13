import heapq


def dijkstra(init_x, init_y):
    hq = []
    heapq.heappush(hq, [lst[init_x][init_y], init_x, init_y])
    visit[init_x][init_y] = 1
    while hq:
        val, x, y = heapq.heappop(hq)
        if x == N - 1 and y == N - 1:
            return val
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1:
                nv = val + lst[nx][ny]
                visit[nx][ny] = 1
                heapq.heappush(hq, [nv, nx, ny])


direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        lst = []
        visit = [[-1 for _ in range(N)] for _ in range(N)]
        for _ in range(N):
            lst.append(list(map(int, input().split())))
        res = dijkstra(0, 0)
        print("Problem {}: {}".format(cnt, res))
        cnt += 1
