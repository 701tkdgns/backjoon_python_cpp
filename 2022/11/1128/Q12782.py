for _ in range(int(input())):
    a, b = map(str, input().split())
    res = len(a)
    cnt1, cnt0 = 0, 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] == '1':
                cnt1 += 1
            else:
                cnt0 += 1
    print(max(cnt1, cnt0))
