N = int(input())
lst = list(map(int, input().split()))
l_stk, r_stk = [], []
while lst:
    n = lst[0]
    del lst[0]
    if l_stk:
        if l_stk[-1] > n:
            l_stk.append(n)
        else:
            while l_stk:
                if l_stk[-1] < n:
                    r_stk.append(l_stk.pop())
                else:
                    break
            l_stk.append(n)
    else:
        l_stk.append(n)

r_stk.extend(reversed(l_stk))
chk = True
for i in range(len(r_stk) - 1):
    if abs(r_stk[i + 1] - r_stk[i]) != 1:
        chk = False
        break
if chk:
    print('Nice')
else:
    print('Sad')
