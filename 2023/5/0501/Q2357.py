# https://squareyun.tistory.com/103

import math
import sys
sys.setrecursionlimit(10**6)

def makeSegTree(idx, s, e):
    if s == e:
        seg[idx] = [lst[s], lst[s]]
        return seg[idx]
    m = (s + e) // 2
    left = makeSegTree(idx * 2, s, m)
    right = makeSegTree(idx * 2 + 1, m + 1, e)
    seg[idx] = (min(left[0], right[0]), max(left[1], right[1]))
    return seg[idx]


def find(idx, s, e, l, r):
    if r < s or l > e:
        return [10e10 + 1, -1]
    if l <= s and e <= r:
        return seg[idx]
    m = (s + e) // 2
    left = find(idx * 2, s, m, l, r)
    right = find(idx * 2 + 1, m + 1, e, l, r)
    return min(left[0], right[0]), max(left[1], right[1])


n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n)) + 1
nodeNum = 1 << h
seg = [0] * nodeNum
makeSegTree(1, 0, len(lst) - 1)
for _ in range(m):
    a, b = map(int, input().split())
    res = find(1, 0, len(lst) - 1, a - 1, b - 1)
    print(*res)
