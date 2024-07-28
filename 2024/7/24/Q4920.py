I_directions = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]]
]
Z_directions = [
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 1], [1, 1], [1, 0], [2, 0]]
]
L_directions = [
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]]
]
T_directions = [
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 1]],
    [[1, 0], [0, 1], [1, 1], [2, 1]]
]
B_directions = [
    [[0, 0], [0, 1], [1, 0], [1, 1]]
]


def checkSum(init_x, init_y, directions):
    ret_sum = -4000001
    for direction in directions:
        chk = True
        tmp_sum = 0
        for dx, dy in direction:
            nx, ny = init_x + dx, init_y + dy
            if 0 <= nx < T and 0 <= ny < T:
                tmp_sum += graph[nx][ny]
            else:
                chk = False
                break
        if chk:
            ret_sum = max(ret_sum, tmp_sum)
    return ret_sum


idx = 1
while True:
    T = int(input())
    if T == 0:
        break
    graph = []
    res = -4000001
    for _ in range(T):
        tmp = list(map(int, input().split()))
        graph.append(tmp)
    for x in range(T):
        for y in range(T):
            res = max(res, checkSum(x, y, I_directions))
            res = max(res, checkSum(x, y, L_directions))
            res = max(res, checkSum(x, y, Z_directions))
            res = max(res, checkSum(x, y, T_directions))
            res = max(res, checkSum(x, y, B_directions))
    print('{}. {}'.format(idx, res))
    idx += 1