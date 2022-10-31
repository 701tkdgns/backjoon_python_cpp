def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            init[i][j] = 1 - init[i][j]


def check():
    for i in range(N):
        for j in range(M):
            if init[i][j] != target[i][j]:
                return False
    return True


N, M = map(int, input().split())
init, target = [], []
cnt = 0
for _ in range(N):
    init.append(list(map(int, input().rstrip())))

for _ in range(N):
    target.append(list(map(int, input().rstrip())))

for i in range(N - 2):
    for j in range(M - 2):
        if init[i][j] != target[i][j]:
            reverse(i, j)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)
