def dfs(x, y, num):
    if len(num) == 6:
        if num not in res:
            res.append(num)
        return
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + fence[nx][ny])


res = []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
fence = [list(map(str, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        dfs(i, j, fence[i][j])
print(len(res))


# def dfs(x, y, number):
#     if len(number) == 6:  # 6자리 숫자가 만들어졌다면
#         if number not in result:  # result에 없다면
#             result.append(number)
#         return
#
#     dx = [1, -1, 0, 0]  # 상하좌우 확인 x
#     dy = [0, 0, 1, -1]  # 상하좌우 확인 y
#     for k in range(4):
#         ddx = x + dx[k]
#         ddy = y + dy[k]
#
#         if 0 <= ddx < 5 and 0 <= ddy < 5:  # 범위 내에 있다면
#             dfs(ddx, ddy, number + matrix[ddx][ddy])  # 6글자가 될 때 까지 재귀
#
#
# # 입력
# matrix = [list(map(str, input().split())) for _ in range(5)]
#
# result = []
# for i in range(5):
#     for j in range(5):
#         dfs(i, j, matrix[i][j])  # 0,0부터 4,4까지 모두 검사
# print(len(result))