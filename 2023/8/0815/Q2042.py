import math, sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def init(idx, start, end):
    if start == end:
        seg[idx] = lst[start - 1]
        return seg[idx]
    mid = (start + end) // 2
    seg[idx] = init(idx * 2, start, mid) + init(idx * 2 + 1, mid + 1, end)
    return seg[idx]


def update(idx, start, end, update_idx, update_value):
    if start > update_idx or end < update_idx:
        return
    seg[idx] += update_value
    if start == end:
        return
    mid = (start + end) // 2
    update(idx * 2, start, mid, update_idx, update_value)
    update(idx * 2 + 1, mid + 1, end, update_idx, update_value)


def find(idx, start, end, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return seg[idx]
    mid = (start + end) // 2
    sub_sum = find(idx * 2, start, mid, left, right) + find(idx * 2 + 1, mid + 1, end, left, right)
    return sub_sum


n, m, k = map(int, input().split())  # num cnt, modi cnt, sum cnt
h = 1 << (math.ceil(math.log2(n)) + 1)
seg = [0 for _ in range(h)]
lst = []
# input num
for i in range(n):
    lst.append(int(input()))
init(1, 1, n)
# modi num & sum num
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = c - lst[b - 1]
        lst[b - 1] = c
        update(1, 1, n, b, tmp)
    else:
        res = find(1, 1, n, b, c)
        print(res)


##################################

def init(start, end, idx):
    if start == end:
        segment_tree[idx] = l[start - 1]
        return segment_tree[idx]
    mid = (start + end) // 2
    segment_tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return segment_tree[idx]


def update(start, end, idx, update_idx, update_data):
    if start > update_idx or end < update_idx:
        return
    segment_tree[idx] += update_data
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx * 2, update_idx, update_data)
    update(mid + 1, end, idx * 2 + 1, update_idx, update_data)


def find_sum(start, end, idx, left, right):
    if start > right or end < left:
        return 0

    if start >= left and end <= right:
        return segment_tree[idx]

    mid = (start + end) // 2
    sub_sum = find_sum(start, mid, idx * 2, left, right) + find_sum(mid + 1, end, idx * 2 + 1, left, right)
    return sub_sum


N, M, K = map(int, input().split())
l = [0 for _ in range(N)]
segment_tree = [0 for _ in range(N * 4)]
for i in range(N):
    l[i] = int(input())
init(1, N, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = c - l[b - 1]
        l[b - 1] = c
        update(1, N, 1, b, tmp)
    elif a == 2:
        print(find_sum(1, N, 1, b, c))
