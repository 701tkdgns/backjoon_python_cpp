def sum_num(inputs):
    res = 0
    for i in inputs:
        if i.isdigit():
            res += int(i)
    return res


N = int(input())
lst = []
for i in range(N):
    lst.append(input())
lst.sort(key=lambda x: (len(x), sum_num(x), x))
for i in lst:
    print(i)
