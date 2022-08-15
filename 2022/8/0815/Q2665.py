import heapq


N = int(input())
lst = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
hq = []
heapq.heappush(hq, [0, 0, 0])
visit[0][0] = 1
while hq:
    a, x, y = heapq.heappop(hq)
    if x == N -1 and y == N -1:
        print(a)
        break
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if lst[nx][ny] == 0:
                heapq.heappush(hq, [a + 1, nx, ny])
            else:
                heapq.heappush(hq, [a, nx, ny])