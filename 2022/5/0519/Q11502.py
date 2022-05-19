eratosthenes = [2]
for i in range(3, 1000):
    chk = True
    for j in range(2, i):
        if i % j == 0:
            chk = False
            break
    if chk:
        eratosthenes.append(i)
T = int(input())
for _ in range(T):
    N = int(input())
    tmp = []
    chk = True
    for i in eratosthenes:
        for j in eratosthenes:
            for k in eratosthenes:
                if i + j + k == N:
                    tmp.append([i, j, k])
                elif i + j + k > N:
                    break
    tmp.sort()
    if len(tmp) == 0:
        print(0)
    else:
        print(tmp[0][0], tmp[0][1], tmp[0][2])
