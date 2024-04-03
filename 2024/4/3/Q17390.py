import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
for i in range(1, N):
    A[i] = A[i] + A[i-1]
for _ in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        print(A[R-1])
    else:
        print(A[R-1] - A[L - 2])