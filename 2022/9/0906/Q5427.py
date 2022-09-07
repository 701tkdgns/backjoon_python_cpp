import sys
from collections import deque

std = sys.stdin.readline

def escape():
    pass

def fire():
    pass

for _ in range(int(std())):
    w, h = map(int, std().split())
    lst = []
    start_x, start_y = 0, 0
    fire_dq = deque()
    visit = [[False for _ in range(w)] for _ in range(h)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(h):
        lst.append(list(map(str, std().rstrip())))
    for x in range(h):
        for y in range(w):
            if lst[x][y] == '*':
                fire_dq.append([x, y])
            if lst[x][y] == '@':
                start_x, start_y = x, y

    while start_x < w and start_y < h:


        escape()

        fire()