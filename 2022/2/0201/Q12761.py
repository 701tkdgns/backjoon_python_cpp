from collections import deque


def bfs(n):
    dq = deque([n])
    while dq:
        n = dq.popleft()
        visit[n] = True
        for i in range(len(direction)):
            if i < 6:
                nx = n + direction[i]
                if 0 <= nx < 100001 and not visit[nx]:
                    dq.append(nx)
                    lst[nx] = lst[n] + 1
                    visit[nx] = True
            else:
                nx = n * direction[i]
                if 0 <= nx < 100001 and not visit[nx]:
                    dq.append(nx)
                    lst[nx] = lst[n] + 1
                    visit[nx] = True


A, B, N, M = map(int, input().split())
lst = [0 for _ in range(100001)]
visit = [False for _ in range(100001)]
direction = [1, -1, A, B, -A, -B, A, B]
bfs(N)
print(lst[M])
