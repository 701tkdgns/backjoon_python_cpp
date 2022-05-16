N = int(input())
A = list(map(int, input().split()))
B, P = sorted(A), [0 for _ in range(N)]
chk = [False for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if B[i] == A[j] and not chk[j]:
            P[j] = cnt
            cnt += 1
            chk[j] = True

for i in P:
    print(i, end=' ')