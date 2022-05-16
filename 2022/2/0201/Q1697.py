from collections import deque


def bfs(n):
    dq = deque([n])
    while dq:
        n = dq.popleft()
        direction = [-1, 1, 2]
        visit[n] = True
        for i in range(len(direction)):
            if i < 2:
                idx = direction[i] + n
                if 0 <= idx < 100001 and not visit[idx]:
                    dq.append(idx)
                    lst[idx] = lst[n] + 1
                    visit[idx] = True
            else:
                idx = direction[i] * n
                if 0 <= idx < 100001 and not visit[idx]:
                    dq.append(idx)
                    lst[idx] = lst[n] + 1
                    visit[idx] = True


N, K = map(int, input().split())
lst = [0 for _ in range(100001)]
visit = [False for _ in range(100001)]
bfs(N)
print(lst[K])
