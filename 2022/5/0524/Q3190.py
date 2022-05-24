from collections import deque


def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def snake_game():
    direction = 1
    time = 1
    y, x = 0, 0
    visited = deque([[y, x]])
    graph[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and graph[y][x] != 2:
            if not graph[y][x] == 1:
                tmp_y, tmp_x = visited.popleft()
                graph[tmp_y][tmp_x] = 0
            graph[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:
            return time


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a - 1][b - 1] = 1
    L = int(input())
    times = dict()
    for _ in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(snake_game())
