N = int(input())
lst = []
maxL, maxH, maxIdx = 0, 0, 0
res, L, R = 0, 0, 0
for _ in range(N):
    l, h = map(int, input().split())
    maxL = l if l > maxL else maxL
    maxH = h if h > maxH else maxH
    maxIdx = l if h == maxH else maxIdx
    lst.append([l, h])
stk = [0 for _ in range(maxL + 1)]
for ll, hh in lst:
    stk[ll] = hh
for i in range(maxIdx):
    L = stk[i] if L < stk[i] else L
    res += L
for i in range(maxL, maxIdx, - 1):
    R = stk[i] if R < stk[i] else R
    res += R
res += stk[maxIdx]
print(res)

# https://ssu-gongdoli.tistory.com/112