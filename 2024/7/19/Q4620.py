I_direction = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]]
]
S_direction = [
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 1], [1, 1], [1, 0], [2, 0]]
]
L_direction = [
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]]
]
T_direction = [
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 1], [1, 0], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [1, 1]]
]
box_direction = [
    [[0, 0], [0, 1], [1, 1], [1, 0]]
]

idx = 1


def check(x, y, directions):
    ret = -50000004
    for direction in directions:
        chk = True
        tmp = 0
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                tmp += lst[nx][ny]
            else:
                chk = False
                break
        if chk:
            ret = max(ret, tmp)
    return ret


while True:
    N = int(input())
    if N == 0:
        break
    res = -50000004
    lst = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res = max(res, check(i, j, I_direction))
            res = max(res, check(i, j, L_direction))
            res = max(res, check(i, j, S_direction))
            res = max(res, check(i, j, T_direction))
            res = max(res, check(i, j, box_direction))
    print('{}. {}'.format(idx, res))
    idx += 1
