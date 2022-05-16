from collections import deque


def bfs(v):
    dq = deque()
    dq.append(v - 1)
    chk = [-1] * N
    chk[v - 1] = 0
    while dq:
        v = dq.popleft()
        for i in range(N):
            if (i - v) % lst[v] == 0 and chk[i] == -1:
                dq.append(i)
                chk[i] = chk[v] + 1
                if i == b - 1:
                    return chk[i]


N = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a))

# from collections import deque
#
#
# def bfs(v):
#     dq = deque()
#     dq.append(v - 1)
#     chk = [-1] * N
#     chk[v - 1] = 0
#     while dq:
#         v = dq.popleft()
#         for n in range(N):
#             if (n - v) % lst[v] == 0 and chk[n] == -1:
#                 dq.append(n)
#                 chk[n] = chk[v] + 1
#                 if n == b - 1:
#                     return chk[n]
#     return -1
#
#
# N = int(input())
# lst = list(map(int, input().split()))
# a, b = map(int, input().split())
# print(bfs(a))
