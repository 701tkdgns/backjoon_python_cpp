from collections import deque

n = int(input())
dq = deque(enumerate(map(int, input().split())))
res = []
while dq:
    idx, paper = dq.popleft()
    res.append(idx + 1)
    if paper > 0:
        dq.rotate(-(paper - 1))
    else:
        dq.rotate(-paper)
print(' '.join(map(str, res)))