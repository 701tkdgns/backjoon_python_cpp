import sys
from collections import deque

N = int(sys.stdin.readline())

lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort(key=lambda x: -x)
dq = deque(lst)
val = 0
while dq:
    if len(dq) >= 3:
        a, b, c = dq.popleft(), dq.popleft(), dq.popleft()
        val += a + b
    else:
        while dq:
            val += dq.pop()

print(val)