N, M = map(int, input().split())
chk = True
for _ in range(M):
    n = int(input())
    lst = list(map(int, input().split()))
    if chk:
        while lst:
            tmp = lst.pop()
            if lst:
                if tmp > lst[-1]:
                    chk = False
                    break
    else:
        break
if chk:
    print('Yes')
else:
    print('No')