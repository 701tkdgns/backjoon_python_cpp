from collections import deque

def bfs(mid):
    dq = deque([start])
    visit = set()
    visit.add(start)
    res = []
    while dq:
        node = dq.popleft()
        for new_node, w in lst[node]:
            if new_node not in visit and w >= mid:
                visit.add(new_node)
                dq.append(new_node)
    return True if end in visit else False

n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
start, end = map(int, input().split())
_min, _max = 1, 10**9

res = _min
while _min <= _max:
    mid = (_min+_max) // 2
    if bfs(mid):
        res = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(res)