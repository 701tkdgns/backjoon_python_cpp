def gcd(b, s):
    while b % s != 0:
        tmp = b
        b = s
        s = tmp % b
    return s


for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst = sorted(lst[1:])
    if len(lst) == 1:
        print(lst[0])
    else:
        tmp_lst = []
        chk_lst = []
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i != j and sorted([i, j]) not in chk_lst:
                    tmp_lst.append(gcd(lst[j], lst[i]))
                    chk_lst.append(sorted([i, j]))
        print(sum(tmp_lst))