import math
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
const = 1000000007


def makeTree(s, e, idx):
    if s == e:
        seg[idx] = lst[s - 1]
        return seg[idx]

    mid = (s + e) // 2
    left = makeTree(s, mid, idx * 2)
    right = makeTree(mid + 1, e, idx * 2 + 1)
    seg[idx] = (left * right) % const
    return seg[idx]


def find(s, e, idx, l, r):
    if r < s or e < l:
        return 1

    if s >= l and r >= e:
        return seg[idx]

    mid = (s + e) // 2
    return_val = find(s, mid, idx * 2, l, r) * find(mid + 1, e, idx * 2 + 1, l, r)
    return return_val % const


def update(s, e, idx, update_idx, update_data):
    if s > update_idx or e < update_idx:
        return
    if s == e:
        seg[idx] = update_data
        return
    mid = (s + e) // 2
    update(s, mid, idx * 2, update_idx, update_data)
    update(mid + 1, e, idx * 2 + 1, update_idx, update_data)
    seg[idx] = seg[idx * 2] * seg[idx * 2 + 1] % const


N, M, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
logNum = math.ceil(math.log2(N) + 1)
h = 1 << logNum
seg = [0 for _ in range(h)]
makeTree(1, N, 1)
# print(seg)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        lst[b-1] = c
        update(1, N, 1, b, c)
        # print(seg)
    elif a == 2:
        print(find(1, N, 1, b, c))
