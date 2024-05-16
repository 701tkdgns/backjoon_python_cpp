from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
dq = deque([])
for i in range(N):
    if A[i] == 0:
        dq.appendleft(B[i])
if dq is []:
    print(*C)
    sys.exit()
for i in range(M):
    dq.append(C[i])
    print(dq.popleft(), end=" ")
