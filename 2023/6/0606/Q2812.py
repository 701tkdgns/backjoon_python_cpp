# from collections import deque
# def bfs(n, k, s):
#     dq = deque()
#     res = -1
#     for i in range(n):
#         dq.append([i, s[i]])
#         while dq:
#             idx, v = dq.popleft()
#             if len(v) == n - k and res < int(v):
#                 res = int(v)
#             for j in range(idx + 1, n):
#                 if len(v + s[j]) <= n - k:
#                     dq.append([j, v + s[j]])
#
#     return res

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().rstrip()
stk = []
for i in range(N):
    while stk and stk[-1] < num[i] and K > 0:
        stk.pop()
        K -= 1
    stk.append(num[i])
res = ''
for i in stk:
    res += i
if K > 0:
    print(res[:-K])
else:
    print(res)