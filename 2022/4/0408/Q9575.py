N = int(input())
for _ in range(N):
    a = int(input())
    lst_a = set(list(map(int, input().split())))
    b = int(input())
    lst_b = set(list(map(int, input().split())))
    c = int(input())
    lst_c = set(list(map(int, input().split())))
    res = []
    for i in lst_a:
        for j in lst_b:
            for k in lst_c:
                chk = True
                tmp = str(i + j + k).rstrip()
                for char in tmp:
                    if char == '5' or char == '8':
                        pass
                    else:
                        chk = False
                        break
                if chk and int(tmp) not in res:
                    res.append(int(tmp))
    print(len(res))
