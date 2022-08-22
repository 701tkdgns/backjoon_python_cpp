import sys
std = sys.stdin.readline

t = int(std())
for _ in range(t):
    n = int(std())
    lst = [str(std().strip()) for _ in range(n)]
    lst.sort()
    chk = True
    for i in range(n - 1):
        if lst[i] == lst[i + 1][0:len(lst[i])]:
            chk = False
            break
    if not chk:
        print("NO")
    else:
        print("YES")