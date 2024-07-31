N = int(input())
graph = []
maxL, maxH, maxIdx = 0, 0, 0
L, R, res = 0, 0, 0
for _ in range(N):
    a, b = map(int, input().split())
    graph.append([a, b])
    maxL = a if a > maxL else maxL
    maxH = b if b > maxH else maxH
    maxIdx = a if b == maxH else maxIdx
stk = [0 for _ in range(maxL + 1)]
for i, h in graph:
    stk[i] = h
for i in range(maxIdx + 1):
    L = stk[i] if stk[i] > L else L
    res += L
for i in range(maxL, maxIdx, -1):
    R = stk[i] if stk[i] > R else R
    res += R
print(res)