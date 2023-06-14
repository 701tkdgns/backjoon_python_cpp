from collections import deque


def bfs():
    visit[0][0][0] = 0
    dq = deque([[0, 0, 0]])
    while dq:
        x, y, z = dq.popleft()
        if z < K:
            for dx, dy in horse_d:
                hx, hy = dx + x, dy + y
                print(hx, hy, z, "hello")
                if (0 <= hx < H and 0 <= hy < W) and visit[hx][hy][z] == -1:
                    print("hellox")


K = int(input())
W, H = map(int, input().split())
lst = []
visit = [[[-1 for _ in range(W)] for _ in range(H)] for _ in range(K + 1)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
horse_d = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
for _ in range(H):
    lst.append(list(map(int, input().split())))
bfs()
