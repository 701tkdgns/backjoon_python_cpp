import math, sys
sys.setrecursionlimit(10**8 + 1)
input = sys.stdin.readline

def init_segment(s, e, idx):
    if s == e:
        seg[idx] = lst[s - 1]
        return seg[idx]
    mid = (s + e) // 2
    left = init_segment(s, mid, idx * 2)
    right = init_segment(mid + 1, e, idx * 2 + 1)
    seg[idx] = left + right
    return seg[idx]


def find(s, e, idx, l, r):
    if s > r or e < l:
        return 0

    if s >= l and r >= e:
        return seg[idx]

    mid = (s + e) // 2
    _res = find(s, mid, idx * 2, l, r) + find(mid + 1, e, idx * 2 + 1, l, r)
    return _res


def update(s, e, idx, update_idx, update_data):
    if s > update_idx or e < update_idx:
        return 0
    if s == e:
        seg[idx] = update_data
        return
    mid = (s + e) // 2
    update(s, mid, idx * 2, update_idx, update_data)
    update(mid + 1, e, idx * 2 + 1, update_idx, update_data)
    seg[idx] = seg[idx * 2] + seg[idx * 2 + 1]


N, Q = map(int, input().split())
lst = list(map(int, input().split()))
logNum = math.ceil(math.log2(N)) + 1
h = 1 << logNum
seg = [0 for _ in range(h)]
init_segment(1, N, 1)
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x <= y:
        print(find(1, N, 1, x, y))
    else:
        print(find(1, N, 1, y, x))
    update(1, N, 1, a, b)
