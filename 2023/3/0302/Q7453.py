def dfs(a, b, c, d):
    global res
    if a >= n or b >= n or c >= n or d >= n:
        return

    if A[a] + B[b] + C[c] + D[d] == 0:
        res += 1
        return

    for j in range(n):
        if not vA[a + j]:
            vA[a + j] = True
            dfs(a + j, b, c, d)
            vA[a + j] = False

        if not vB[b + j]:
            vB[b + j] = True
            dfs(a, b + j, c, d)
            vB[b + j] = False

        if not vC[c + j]:
            vC[c + j] = True
            dfs(a, b, c + j, d)
            vC[c + j] = False

        if not vD[d + j]:
            vD[d + j] = True
            dfs(a, b, c, d + j)
            vD[d + j] = False


n = int(input())
A, B, C, D = [], [], [], []
vA, vB, vC, vD = [False for _ in range(n)], [False for _ in range(n)], [False for _ in range(n)], [False for _ in
                                                                                                   range(n)]
res = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    A.append(tmp[0])
    B.append(tmp[1])
    C.append(tmp[2])
    D.append(tmp[3])

dfs(0, 0, 0, 0)
