N = int(input())
pharmacy = dict()
for _ in range(N):
    e, n = map(int, input().split())
    pharmacy[e] = n
R = int(input())
for _ in range(R):
    L = list(map(int, input().split()))
    l, L = L[0], L[1:]
    res = []
    for i in L:
        if i in pharmacy:
            res.append(pharmacy[i])
    if len(res) == l:
        print(*res)
    else:
        print("YOU DIED")
