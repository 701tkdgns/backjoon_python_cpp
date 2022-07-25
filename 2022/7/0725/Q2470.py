N = int(input())
lst = list(map(int, input().split()))
lst.sort()
mn = 2e+9 + 1
l, r = 0, N - 1
res = []
while l < r:
    L, R = lst[l], lst[r]
    tot = L + R
    if abs(tot) < mn:
        mn = abs(tot)
        res = [L, R]
    if tot < 0:
        l += 1
    else:
        r -= 1
print(res[0], res[1])
