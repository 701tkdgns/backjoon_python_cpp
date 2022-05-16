from collections import deque


def bfs():
    dq = deque()
    dq.append([h_x, h_y])
    while dq:
        x, y = dq.popleft()
        if abs(x - r_x) + abs(y - r_y) <= 1000:
            return "happy"
        for i in range(n):
            if not chk[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    dq.append([nx, ny])
                    chk[i] = 1

    return "sad"


for _ in range(int(input())):
    n = int(input())
    conv = []
    h_x, h_y = map(int, input().split())
    for _ in range(n):
        c_x, c_y = map(int, input().split())
        conv.append([c_x, c_y])
    r_x, r_y = map(int, input().split())
    chk = [0 for i in range(n+1)]
    print(bfs())
