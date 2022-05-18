def GCD(b, s):
    while b % s:
        tmp = b
        b = s
        s = tmp % b
    return s


for _ in range(int(input())):
    lst = list(map(int, input().split()))
    res = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                res = max(res, GCD(lst[i], lst[j]))
    print(res)
