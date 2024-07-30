H, W = map(int, input().split())
lst = list(map(int, input().split()))
maxH, maxIdx, res = 0, 0, 0
stk = [0 for _ in range(W + 1)]
for i in range(W):
    maxH = lst[i] if maxH < lst[i] else maxH
    maxIdx = i if maxH == lst[i] else maxIdx
    stk[i] = lst[i]
L, R = 0, 0
l_h, r_h = 0, 0
for i in range(maxIdx):
    l_h = stk[i] if l_h < stk[i] else l_h
    L += l_h - stk[i]
for i in range(W, maxIdx, -1):
    r_h = stk[i] if r_h < stk[i] else r_h
    R += r_h - stk[i]
res = L + R
print(res)
