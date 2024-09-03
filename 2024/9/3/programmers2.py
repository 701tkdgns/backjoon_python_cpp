answer = [0, 0]


def dfs(x, y, n, arr):
    current = arr[x][y]
    same = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != current:
                same = False
                break
        if not same: break
    if same:
        answer[current] += 1
    else:
        half = n // 2
        dfs(x, y, half, arr)
        dfs(x, y + half, half, arr)
        dfs(x + half, y, half, arr)
        dfs(x + half, y + half, half, arr)


def solution(arr):
    dfs(0, 0, len(arr), arr)

    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=python3