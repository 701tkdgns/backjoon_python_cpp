T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    R, L = [], []
    for i in range(len(lst)):
        if i % 2 == 0:
            R.append(lst[i])
        else:
            L.append(lst[i])
    R.extend(reversed(L))
    res = -1
    for i in range(N):
        if i == N - 1:
            if res < abs(R[-1] - R[0]):
                res = abs(R[i] - R[0])

        elif res < abs(R[i+1] - R[i]):
            res = abs(R[i+1] - R[i])
    print(res)