lst = []
for _ in range(int(input())):
    name, k, y, s = input().split()
    lst.append([name, int(k), int(y), int(s)])
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for tmp in lst:
    print(tmp[0])