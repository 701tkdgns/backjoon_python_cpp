N = int(input())
lst = list(map(int, input().split()))
S = int(input())

for i in range(N):
    _max = max(lst[i: i + S + 1])
    _max_idx = lst.index(_max)
    for j in range(_max_idx, i, -1):
        lst[j], lst[j-1] = lst[j-1], lst[j]
    S -= (_max_idx - i)
    if S <= 0:
        break
print(*lst)
