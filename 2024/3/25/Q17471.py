from itertools import combinations
from collections import deque


def bfs(arr):
    start = arr[0]
    dq = deque([start])
    visited = set([start])
    num = 0
    while dq:
        value = dq.popleft()
        num += people[value]
        for i in link[value]:
            if i not in visited and i in arr:
                dq.append(i)
                visited.add(i)
    return num, len(visited)


N = int(input())
people = [0] + list(map(int, input().split()))
link = [0 for _ in range(N + 1)]
res = float('inf')

for i in range(1, N + 1):
    link[i] = list(map(int, input().split()))
    link[i] = link[i][1:]

for i in range(1, N // 2 + 1):
    combis = list(combinations(range(1, N + 1), i))
    for combi in combis:
        sum1, node1 = bfs(combi)
        sum2, node2 = bfs([i for i in range(1, N + 1) if i not in combi])
        if node1 + node2 == N:
            res = min(res, abs(sum1 - sum2))

if res != float('inf'):
    print(res)
else:
    print(-1)