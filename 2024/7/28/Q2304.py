N = int(input())
lst = []
for _ in range(N):
    l, h = map(int, input().split())
    lst.append([l, h])
lst.sort()
stk = []
# print(lst)
res = 0
for i in range(N):
    tmp_l, tmp_h = 0, 0
    while stk and stk[0][1] < lst[i][1]:
        ll, hh = stk.pop()
        tmp_l = max(tmp_l, lst[i][0] - ll)
        tmp_h = stk[0][0] if (stk and tmp_h == 0) else tmp_h
    if tmp_l != 0 and tmp_h != 0:
        print(tmp_l, tmp_h)
        res += tmp_l * tmp_h
    stk.append(lst[i])
print(res, stk)
