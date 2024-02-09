import sys
input = sys.stdin.readline
n = int(input())
stk = []
for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        stk.append(lst[1])
    elif lst[0] == 2:
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif lst[0] == 3:
        print(len(stk))
    elif lst[0] == 4:
        if stk:
            print(0)
        else:
            print(1)
    elif lst[0] == 5:
        if stk:
            print(stk[-1])
        else:
            print(-1)
