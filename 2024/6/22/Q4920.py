while True:
    N = int(input())
    if N == 0:
        break
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
