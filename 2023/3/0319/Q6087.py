import heapq


def dijkstra(sx, sy):
    visit[sx][sy] = -1
    hq = []
    heapq.heappush(hq, [0, sx, sy])
    while hq:
        wei, x, y = heapq.heappop(hq)
        for idx in range(4):
            nx, ny = x + direction[idx][0], y + direction[idx][1]


W, H = map(int, input().split())
lst = []
inf = W * H + 1
visit = [[inf for _ in range(W)] for _ in range(H)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
C = []
for i in range(H):
    tmp = list(input().rstrip())
    for j in range(W):
        if tmp[j] == "C":
            C.append([i, j])
    lst.append(tmp)
