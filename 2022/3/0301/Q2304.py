N = int(input())
lst = []
maxH, maxL = 1, 0
maxIdx = 0
for i in range(N):
    l, h = map(int, input().split())
    lst.append([l, h])
    if maxL < l:
        maxL = l
    if maxH < h:
        maxH = h
        maxIdx = l
stk = [0] * (maxL + 1)
for l, h in lst:
    stk[l] = h
total, tmp = 0, 0
for i in range(maxIdx + 1):
    if stk[i] > tmp:
        tmp = stk[i]
    total += tmp
tmp = 0
for i in range(maxL, maxIdx, -1):
    if stk[i] > tmp:
        tmp = stk[i]
    total += tmp
print(total)