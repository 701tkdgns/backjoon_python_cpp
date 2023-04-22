if __name__ == "__main__":
    while True:
        tmp = list(map(int, input().split()))
        if len(tmp) == 1 and tmp[0] == 0:
            break
        lst = tmp[1:] + [0]
        stk = [[0, lst[0]]]
        res, left = 0, 0
        for i in range(tmp[0] + 1):
            left = i
            while stk and stk[-1][1] > lst[i]:
                left, h = stk.pop()
                res = max(res, (i - left) * h)
            stk.append([left, lst[i]])
        print(res)