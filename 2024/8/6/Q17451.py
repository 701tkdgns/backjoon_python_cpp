import sys
input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

N = int(input())
lst = list(map(int, input().split()))
gcd = GCD(max(lst[N - 1], lst[N - 2]), min(lst[N - 1], lst[N - 2]))
cnt = 1
while True:
    tst = gcd * cnt
    chk = True
    for v in lst:
        if tst >= v:
            if tst % v == 0:
                continue
            else:
                tst = tst - tst % v
        else:
            chk = False
    if chk:
        break
    cnt += 1
print(gcd * cnt)