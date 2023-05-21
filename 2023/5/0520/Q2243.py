import sys, math

input = sys.stdin.readline


def get(s, e, idx, find_idx):
    if s == e:
        tree[idx] -= 1
        print(arr[idx])
        return tree[idx]

    l_idx = tree[idx * 2]
    m = (s + e) // 2
    if l_idx >= find_idx:
        get(s, m, idx * 2, find_idx)
    else:
        get(m + 1, e, idx * 2 + 1, find_idx - l_idx)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
    return tree[idx]


def update(s, e, idx, update_idx, update_data):
    if update_idx < s or e < update_idx:
        return tree[idx]
    if s == e == update_idx:
        tree[idx] += update_data
        arr[idx] = update_idx
        return tree[idx]
    m = (s + e) // 2
    left = update(s, m, idx * 2, update_idx, update_data)
    right = update(m + 1, e, idx * 2 + 1, update_idx, update_data)
    tree[idx] = left + right
    return tree[idx]


t = int(input())
h = 1000000 * 4
tree = [0] * h
arr = [0] * h
for _ in range(t):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        get(1, 1000000, 1, tmp[1])
    elif tmp[0] == 2:
        update(1, 1000000, 1, tmp[1], tmp[2])