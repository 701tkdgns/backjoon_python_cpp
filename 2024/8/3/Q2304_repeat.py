def main():
    N = int(input())
    graph = []
    maxL, maxH, maxIdx = 0, 0, 0
    for _ in range(N):
        l, h = map(int, input().split())
        graph.append([l, h])
        maxL = l if maxL < l else maxL
        maxH = h if maxH < h else maxH
        maxIdx = l if maxH == h else maxIdx
    stk = [0 for _ in range(maxL + 1)]
    for l, h in graph:
        stk[l] = h
    res, L, R = 0, 0, 0
    for i in range(maxIdx + 1):
        L = stk[i] if L < stk[i] else L
        res += L
    for i in range(maxL, maxIdx, -1):
        R = stk[i] if R < stk[i] else R
        res += R
    print(res)


if __name__ == "__main__":
    main()