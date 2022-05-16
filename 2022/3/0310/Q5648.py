lst = []
n, idx = 10**6, 0
while True:
    if len(lst) == n:
        break
    tmp_i = 0
    for i in list(map(int, input().split())):
        if idx == 0 and tmp_i == 0:
            n = i
            tmp_i += 1
            idx += 1
        else:
            tmp = int(''.join(reversed(str(i))))
            lst.append(tmp)
lst.sort()
for i in lst:
    print(i)