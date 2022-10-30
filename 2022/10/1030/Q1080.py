N, M = map(int, input().split())
init, target = [], []
for _ in range(N):
    init.append(list(map(int, input().rstrip())))

for _ in range(N):
    target.append(list(map(int, input().rstrip())))


init_0, init_1 = 0, 0
target_0, target_1 = 0, 0

for i in range(N):
    init_0 += init[i].count(0)
    init_1 += init[i].count(1)
    target_0 += target[i].count(0)
    target_1 += target[i].count(1)

print(init_0, init_1, target_0, target_1)