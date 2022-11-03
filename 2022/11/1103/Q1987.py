r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny])
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)


# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline
#
# def dfs(x, y, cnt):
#     global res
#     res = res if res > cnt  else cnt
#     for dx, dy in direction:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] not in chk:
#             chk.add(lst[nx][ny])
#             dfs(nx, ny, cnt + 1)
#             chk.remove(lst[nx][ny])
#
# R, C = map(int, input().split())
# lst = []
# res = 0
# chk = set()
# for _ in range(R):
#     lst.append(list(map(str, input().rstrip())))
# direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# chk.add(lst[0][0])
# dfs(0, 0, 1)
# print(res)




# from collections import deque


# def bfs(x, y):
#     dq = deque([[x, y, [lst[x][y]]]])
#     _max = 0
#     while dq:
#         x, y, tmp = dq.popleft()
#         _max = _max if _max > len(tmp) else len(tmp)
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] not in tmp:
#                 dq.append([nx, ny, tmp + [lst[nx][ny]]])
#     return _max