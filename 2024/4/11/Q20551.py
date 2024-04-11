import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = []
B = dict()
for _ in range(N):
    A.append(int(input()))
A.sort()
for i in range(len(A) - 1, -1, -1):
    B[A[i]] = i
for _ in range(M):
    D = int(input())
    print(B[D] if D in B else -1)
