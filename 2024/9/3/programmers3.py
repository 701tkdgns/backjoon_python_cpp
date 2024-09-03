def solution(n):
    answer = []
    dp = [[0 for _ in range(n)] for _ in range(n)]
    directions = [[1, 0], [0, 1], [-1, -1]]
    cnt = 1
    x, y, d = 0, 0, 0
    dp[x][y] = cnt
    chk = True
    while chk:
        nx, ny = directions[d][0] + x, directions[d][1] + y
        if 0 <= nx < n and 0 <= ny < n:
            if dp[nx][ny] == 0:
                cnt += 1
                dp[nx][ny] = cnt
                x, y = nx, ny
            else:
                d = (d + 1) % 3
                tx, ty = directions[d][0] + x, directions[d][1] + y
                if 0 <= tx < n and 0 <= ty < n and dp[tx][ty] == 0:
                    cnt += 1
                    dp[tx][ty] = cnt
                    x, y = tx, ty
                else:
                    chk = False
        else:
            d = (d + 1) % 3
            tx, ty = directions[d][0] + x, directions[d][1] + y
            if 0 <= tx < n and 0 <= ty < n and dp[tx][ty] == 0:
                cnt += 1
                dp[tx][ty] = cnt
                x, y = tx, ty
            else:
                chk = False

    for i in range(n):
        answer += dp[i][:i + 1]

    # for d in dp:
    #     print(*d)

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/68645?language=python3