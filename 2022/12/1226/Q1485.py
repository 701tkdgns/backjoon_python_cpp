for _ in range(int(input())):
    lst, x, y = [0 for _ in range(6)], [], []
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            lst[k] = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            k += 1
    lst.sort()
    print(lst)