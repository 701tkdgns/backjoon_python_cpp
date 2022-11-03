import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline


def dfs(x, y, chk):
    global res
    res = res if res > len(chk) else len(chk)
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] not in chk:
            dfs(nx, ny, chk + [lst[nx][ny]])


R, C = map(int, input().split())
lst = []
res = 0
for _ in range(R):
    lst.append(list(map(str, input().rstrip())))
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dfs(0, 0, [lst[0][0]])
print(res)




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