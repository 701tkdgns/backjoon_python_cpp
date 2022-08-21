def GCD(s, b):
    while b % s != 0:
        tmp = b
        b = s
        s = tmp % b
    return s


A, B = map(int, input().split())
res = GCD(A, B)
print(A // res * B // res * res)
