from collections import deque


def bfs(init_x, init_y):
    dq = deque()
    dq.append([init_x, init_y])
    visit[init_x][init_y] = True
    cnt = 0
    while dq:
        x, y = dq.popleft()
        if x == node[1][0] and y == node[1][1]:
            return cnt
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            while True:
                print(dx, dy)
                if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] != "*" and not visit[nx][ny]:
                    if lst[nx][ny] == "!":
                        dq.append([nx, ny])
                        visit[nx][ny] = True
                        break
                    visit[nx][ny] = True
                else:
                    break
                nx = dx + x
                ny = dy + y
            # nx, ny = dx + nx, ny + dy

                for i in visit:
                    print(*i)
                print()
        # print("까꿍")


n = int(input())
lst = []
node = []
visit = [[False for _ in range(n)] for _ in range(n)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(n):
    lst.append(list(map(str, input().rstrip())))
    for j in range(len(lst[i])):
        if lst[i][j] == "#":
            node.append([i, j])
bfs(node[0][0], node[0][1])
