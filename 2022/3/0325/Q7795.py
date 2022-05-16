import sys
std = sys.stdin
T = int(std.readline())
for _ in range(T):
    a, b = map(int, std.readline().split())
    A = list(sorted(map(int, std.readline().split()), reverse=True))
    B = list(sorted(map(int, std.readline().split()), reverse=True))
    res = 0
    for i in range(a):
        for j in range(b):
            if B[j] < A[i]:
                res += b - j
                break
    print(res)