import heapq

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
lst = [list(map(str, input().rstrip())) for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]
hq = []
heapq.heappush(hq, [x1, y1])
visit[x1][y1] = 0
while hq:
    x, y = heapq.heappop(hq)
    if x == x2 and y == y2:
        break
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == -1:
            if lst[nx][ny] == "1" or lst[nx][ny] == "#":
                visit[nx][ny] = visit[x][y] + 1
                heapq.heappush(hq, [nx, ny])
                # break
            if lst[nx][ny] == "0":
                visit[nx][ny] = visit[x][y] + 1
                heapq.heappush(hq, [nx, ny])
print(visit[x2][y2])
