from collections import deque


def bfs(v):
    dq = deque()
    dq.append(v)
    cnt = 1
    chk[v] = True
    while dq:
        v = dq.popleft()
        direction = [-lst[v], lst[v]]
        for d in direction:
            jump = v + d
            if 0 <= jump < N and not chk[jump]:
                dq.append(jump)
                chk[jump] = True
                cnt += 1
    return cnt


N = int(input())
lst = list(map(int, input().split()))
s = int(input())
chk = [False for _ in range(N)]
print(bfs(s-1))