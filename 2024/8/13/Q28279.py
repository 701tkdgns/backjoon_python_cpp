from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dq = deque()
for _ in range(N):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        dq.appendleft(lst[1])
    elif lst[0] == 2:
        dq.append(lst[1])
    elif lst[0] == 3:
        print(-1 if len(dq) == 0 else dq.popleft())
    elif lst[0] == 4:
        print(-1 if len(dq) == 0 else dq.pop())
    elif lst[0] == 5:
        print(len(dq))
    elif lst[0] == 6:
        print(1 if len(dq) == 0 else 0)
    elif lst[0] == 7:
        print(-1 if len(dq) == 0 else dq[0])
    elif lst[0] == 8:
        print(-1 if len(dq) == 0 else dq[-1])


