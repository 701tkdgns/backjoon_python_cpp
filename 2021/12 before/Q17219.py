import sys
N, M = map(int, sys.stdin.readline().split())
idPW = {}
for _ in range(N):
    x, y = sys.stdin.readline().split()
    idPW[x] = y
for _ in range(M):
    print(idPW[sys.stdin.readline().rstrip()])
