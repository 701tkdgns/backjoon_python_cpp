N, K = map(int, input().split())
lst = [0 for _ in range(N)]
for i in range(N):
    lst[i] = float(input()) * 10
lst = sorted(lst)[K:N-K]
jp, bp = 0, 0
for i in lst:
    jp += i
jp = jp/(N-2*K)/10
for i in lst:
    bp += i
bp = bp + lst[0]*K + lst[-1]*K
bp = bp / N / 10
print("{:.2f}\n{:.2f}".format(jp + 0.00000001, bp + 0.00000001))