from collections import deque


def bfs():
    while dq:
        x = dq.popleft()
        for i in range(8):
            if i < 6:
                nx = x + direction[i]
                if 0 <= nx < 100001 and visit[nx] == 0:
                    dq.append(nx)
                    visit[nx] = 1
                    s[nx] = s[x] + 1
            else:
                nx = x * direction[i]
                if 0 <= nx < 100001 and visit[nx] == 0:
                    dq.append(nx)
                    visit[nx] = 1
                    s[nx] = s[x] + 1


s = [0 for _ in range(100001)]
visit = [0 for _ in range(100001)]
A, B, N, M = map(int, input().split())  # n,m 두 사람이 n,m 각각 위치, a,b만큼 이동 가능
direction = [1, -1, A, -A, B, -B, A, B]
dq = deque()
dq.append(N)
visit[N] = 1
bfs()
print(s[M])