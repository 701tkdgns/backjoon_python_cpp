import sys
from collections import deque
input = sys.stdin.readline

def bfs(k):
    dq = deque([k])
    cnt = 1
    while dq:
        k = dq.popleft()
        if friends.get(k):
            for key in friends[k]:
                dq.append(key)
                cnt += 1
    return cnt


F = int(input())
for _ in range(F):
    friends = dict()
    N = int(input())
    for _ in range(N):
        a, b = input().split()
        if friends.get(a) is None:
            friends[a] = []
        friends[a].append(b)
        cnt = 0
        keys = friends.keys()
        for k in keys:
            cnt = max(cnt, bfs(k))
        print(cnt)