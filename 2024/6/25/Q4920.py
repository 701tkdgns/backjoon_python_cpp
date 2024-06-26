I_direction = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]]
]

S_direction = [
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 1], [0, 2], [1, 0], [1, 2]]
]

L_direction = [
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 1], [1, 1], [2, 1], [2, 0]]
]

Square_direction = [
    [[0, 0], [0, 1], [1, 1], [1, 0]]
]

T_direction = [
    [[0, 0], [1, 0], [1, 1], [2, 0]],
    [[0, 1], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]]
]


def check(x, y, directions):
    tmp = -4000004
    for direction in directions:
        chk = True
        tmp_sum = 0
        for dx, dy in direction:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N:
                tmp_sum += lst[new_x][new_y]
            else:
                chk = False
                break
        if chk:
            tmp = max(tmp, tmp_sum)
    return tmp


while True:
    N = int(input())
    idx = 1
    if N == 0:
        break
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    res = -4000004

    for i in range(N):
        for j in range(N):
            res = max(res, check(i, j, T_direction))
            res = max(res, check(i, j, Square_direction))
            res = max(res, check(i, j, L_direction))
            res = max(res, check(i, j, S_direction))
            res = max(res, check(i, j, I_direction))

    print('{}. {}'.format(idx, res))
    idx += 1