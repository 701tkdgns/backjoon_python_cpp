import bisect

T = int(input())
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
A, B = [], []
for i in range(N):
    s = a[i]
    A.append(s)
    for j in range(i + 1, N):
        s += a[j]
        A.append(s)
for i in range(M):
    s = b[i]
    B.append(s)
    for j in range(i + 1, M):
        s += b[j]
        B.append(s)
A.sort()
B.sort()
res = 0
for i in range(len(A)):
    l = bisect.bisect_left(B, T - A[i])
    r = bisect.bisect_right(B, T - A[i])
    res += r - l
print(res)
