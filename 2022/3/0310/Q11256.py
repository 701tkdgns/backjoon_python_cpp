t = int(input())
for _ in range(t):
    j, n = map(int, input().split())
    lst = []
    for _ in range(n):
        r, c = map(int, input().split())
        lst.append(r * c)
    lst.sort(reverse=True)
    res = 0
    for i in lst:
        if j > i:
            j -= i
            res += 1
        else:
            break
    if j > 0:
        res += 1
    print(res)
