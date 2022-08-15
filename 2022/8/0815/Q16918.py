from collections import deque
import sys


def lock_bomb():
    for i in range(R):
        for j in range(C):
            if lst[i][j] == 'O':
                BOMB.append([i, j])


def push_bomb():
    for i in range(R):
        for j in range(C):
            if lst[i][j] != 'O':
                lst[i][j] = 'O'


def bomb():
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while BOMB:
        x, y = BOMB.popleft()
        lst[x][y] = '.'
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] == 'O':
                lst[nx][ny] = '.'


R, C, N = map(int, input().split())
lst = []
for _ in range(R):
    lst.append(list(map(str, input().rstrip())))

N -= 1

while N:
    BOMB = deque()

    lock_bomb()

    push_bomb()

    N -= 1
    if N == 0:
        break

    bomb()
    N -= 1

for i in lst:
    print(''.join(i))