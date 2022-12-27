# 각 4변의 길이가 모두 같고, 양 점에서 그은 두 대각선의 길이가 같다면 정사각형이다.

for _ in range(int(input())):
    lst, x, y = [0 for _ in range(6)], [], []
    for _ in range(4):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            lst[k] = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            k += 1
    lst.sort()
    if lst[0] == lst[1] == lst[2] == lst[3] and lst[4] == lst[5]:
        print(1)
    else:
        print(0)