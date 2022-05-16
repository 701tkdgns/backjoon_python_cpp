from collections import deque


def bfs(idx):
    dq = deque([idx])
    while dq:
        idx = dq.popleft()
        for i in range(8):
            if i < 6:
                nx = idx + direction[i]
                if 0 <= nx < len(lst) - 1 and not visit[nx]:
                    dq.append(nx)
                    lst[nx] = lst[idx] + 1
                    visit[nx] = True
            else:
                nx = idx * direction[i]
                if 0 <= nx < len(lst) - 1 and not visit[nx]:
                    dq.append(nx)
                    lst[nx] = lst[idx] + 1
                    visit[nx] = True


A, B, N, M = map(int, input().split())
direction = [1, -1, A, -A, B, -B, A, B]
lst = [0 for _ in range(100001)]
visit = [False for _ in range(100001)]
visit[N] = True
bfs(N)
print(lst[M])
