H, W = map(int, input().split())
weather = [] # . 구름x c 구름o
for i in range(H):
    weather.append(list(input()))

res = [[-1] * len(weather[0]) for _ in range(len(weather))]

for i in range(H):
    chk = False
    for j in range(W):
        if chk and j-1 >= 0:
            res[i][j] = res[i][j-1] + 1
        if weather[i][j] == 'c':
            res[i][j] = 0
            chk = True

for i in range(H):
    for j in range(W):
        print(res[i][j], end=' ')
    print()