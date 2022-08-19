import math

lst = []

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    diagonal = h ** 2 + w ** 2
    res_h, res_w = 0, 0
    for new_w in range(2, 151):
        for new_h in range(1, new_w):
            tmp = new_h ** 2 + new_w ** 2
            if tmp > diagonal:
                res_w = new_w
                res_h = new_h
                break
            elif tmp == diagonal and h < new_h:
                res_h = new_h
                res_w = new_w
                break
        if res_w * res_h != 0:
            break

    print(res_h, res_w)

