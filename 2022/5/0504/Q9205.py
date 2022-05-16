# from collections import deque
#
#
# def bfs(x, y):
#     dq = deque()
#     dq.append([x, y])
#     while dq:
#         x, y = dq.popleft()
#         if abs(x - destination[0]) + abs(y - destination[1]) <= 1000:
#             return True
#         for i in range(N):
#             if not visited[i]:
#                 nx, ny = lst[i]
#                 if abs(x - nx) + abs(y - ny) <= 1000:
#                     dq.append([nx, ny])
#                     visited[i] = True
#     return False
#
#
# for _ in range(int(input())):
#     N = int(input())
#     lst = []
#     home = list(map(int, input().split()))
#     for _ in range(N):
#         lst.append(list(map(int, input().split())))
#     destination = list(map(int, input().split()))
#     visited = [False for _ in range(N + 1)]
#     chk = bfs(0, 0)
#     if chk:
#         print('happy')
#     else:
#         print('sad')


from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        if abs(x - destination[0]) + abs(y - destination[1]) <= 1000:
            return True
        for idx in range(n):
            if not visited[idx]:
                nx, ny = lst[idx]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    dq.append([nx, ny])
                    visited[idx] = True
    return False


for _ in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().split())))
    destination = list(map(int, input().split()))
    visited = [False for _ in range(n)]
    chk = bfs(home[0], home[1])
    if chk:
        print('happy')
    else:
        print('sad')
