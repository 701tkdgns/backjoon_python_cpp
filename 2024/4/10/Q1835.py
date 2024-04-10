from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dq = deque()
while N >= 1:
    dq.appendleft(N)
    for i in range(1, N + 1):
        dq.appendleft(dq.pop())
    N -= 1
print(*dq)

