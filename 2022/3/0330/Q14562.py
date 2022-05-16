from collections import deque


def bfs(S, T):
    dq = deque()
    dq.append((S, T, 0))
    chk = [-1] * 200
    while dq:
        node, t, c = dq.popleft()
        if node <= t and chk[node] == -1:
            dq.append((node * 2, t + 3, c + 1))
            dq.append((node + 1, t, c + 1))
            if node == t:
                return c


C = int(input())
for _ in range(C):
    s, t = map(int, input().split())
    print(bfs(s, t))
