import math
import sys
input = sys.stdin.readline

def init_segmentTree(s, e, idx):
    if s == e:
        segmentTree[idx] = lst[s]
        return segmentTree[idx]
    mid = (s + e) // 2
    left = init_segmentTree(s, mid, idx * 2)
    right = init_segmentTree(mid + 1, e, idx * 2 + 1)
    segmentTree[idx] = min(left, right)
    return segmentTree[idx]


def find(s, e, idx, l, r):
    if r < s or e < l:
        return 10e10 + 1
    if l <= s and e <= r:
        return segmentTree[idx]
    mid = (s + e) // 2
    left = find(s, mid, idx * 2, l, r)
    right = find(mid + 1, e, idx * 2 + 1, l, r)
    return min(left, right)


N, M = map(int, input().split())
lst = []
logNum = math.ceil(math.log2(N)) + 1
h = 1 << logNum
segmentTree = [0 for _ in range(h)]
for _ in range(N):
    lst.append(int(input()))
init_segmentTree(0, N-1, 1)
# print(segmentTree)
for _ in range(M):
    a, b = map(int, input().split())
    res = find(0, N-1, 1, a - 1, b - 1)
    print(res)

