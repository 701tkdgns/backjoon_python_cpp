for _ in range(int(input())):
    a, b = map(str, input().split())
    res = len(a)
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(0 if cnt == 0 else cnt - 1)