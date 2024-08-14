while True:
    try:
        A, B, C = map(int, input().split())
        res = max(abs(B - C) - 1, abs(A - B) - 1)
        print(res)
    except:
        break
