cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    name = []
    for _ in range(n):
        name.append(input())
    lst = []
    for _ in range(2 * n - 1):
        tmp = list(map(str, input().split()))
        T = int(tmp[0])
        if T in lst:
            lst.remove(T)
        else:
            lst.append(T)
    print(cnt, name[lst[0]-1])
    cnt += 1