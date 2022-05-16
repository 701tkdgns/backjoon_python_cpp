def bfs(x, y):
    queue = [[x, y]]
    check[x][y] = True
    direction = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        if x == end_x and y == end_y:
            return chess[x][y]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= i and 0 <= ny <= i and not check[nx][ny]:
                queue.append((nx, ny))
                check[nx][ny] = True
                chess[nx][ny] = chess[x][y] + 1


for _ in range(int(input())):
    i = int(input())  # 체스판 한 변 길이
    check = [[False] * i for _ in range(i)]
    chess = [[0] * i for _ in range(i)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y))
