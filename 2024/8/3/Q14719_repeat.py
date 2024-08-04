def main():
    H, W = map(int, input().split())
    lst = list(map(int, input().split()))
    L, R, res = lst[0], lst[W - 1], 0
    maxH = max(lst)
    maxIdx = lst.index(maxH)
    for i in range(maxIdx + 1):
        res = res + L - lst[i] if L >= lst[i] else res
        L = lst[i] if L < lst[i] else L
    for i in range(W - 1, maxIdx, -1):
        res = res + R - lst[i] if R >= lst[i] else res
        R = lst[i] if R < lst[i] else R
    print(res)


if __name__ == "__main__":
    main()
