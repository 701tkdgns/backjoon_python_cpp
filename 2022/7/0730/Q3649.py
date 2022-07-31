while True:
    try:
        x = int(input())
        nano_x = x * (10 ** 7)
        lst = []
        n = int(input())
        for _ in range(n):
            lst.append(int(input()))
        lst.sort()
        l, r = 0, n - 1
        res = []
        while l < r:
            if lst[l] + lst[r] == nano_x:
                if res:
                    if abs(res[0] - res[1]) < abs(lst[l] - lst[r]):
                        res = [lst[l], lst[r]]
                else:
                    res = [lst[l], lst[r]]
                r -= 1
                l += 1
            elif lst[l] + lst[r] > nano_x:
                r -= 1
            else:
                l += 1
        if res:
            print("yes {} {}".format(res[0], res[1]))
        else:
            print("danger")
    except:
        break
