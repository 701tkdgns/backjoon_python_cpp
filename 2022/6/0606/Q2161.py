from collections import deque

N = int(input())
dq = deque()
for i in range(1, N+1):
    dq.append(i)
while dq:
    print(dq.popleft(), end=" ")
    if dq:
        dq.append(dq.popleft())
