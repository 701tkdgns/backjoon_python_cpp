cnt = 1
while True:
    T = int(input())
    if T == 0:
        break
    else:
        lst = []
        for _ in range(T):
            lst.append(input())
        lst.sort()
        print(cnt)
        for S in lst:
            print(S)
    cnt += 1