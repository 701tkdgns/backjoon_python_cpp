import sys
from collections import deque
input = sys.stdin.readline
MAX = int(10e9)


def bfs(s, e):
    dq = deque([[s, ""]])
    check.add(s)
    if s == e:
        return 0
    else:
        res = -1
        while dq:
            s, t = dq.popleft()
            if s == e:
                res = t
                return res
            if s*s <= MAX and s*s not in check:
                dq.append([s*s, t+"*"])
                check.add(s*s)
            if s+s <= MAX and s+s not in check:
                dq.append([s+s, t+"+"])
                check.add(s+s)
            if 1 not in check:
                dq.append([1, t+"/"])
                check.add(1)
        return res


check = set()
S, E = map(int, input().split())
print(bfs(S, E))