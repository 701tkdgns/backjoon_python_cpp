
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    direction = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]
    lst = []
    for _ in range(L):
        tmp = []
        for _ in range(R):
            tmp.append(list(map(str, input().rstrip())))
        lst.append(tmp)
        input()
