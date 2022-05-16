n1, n2 = map(int, input().split())
N1, N2 = list(input()), list(input())
T = int(input())
N1 = N1[::-1]
ant = N1 + N2
while T > 0:
    tmp = []
    for i in range(1, len(ant)):
        if ant[i] in N2 and ant[i-1] in N1:
            tmp.append(i)
    for i in tmp:
        ant[i], ant[i-1] = ant[i-1], ant[i]
    T -= 1
print(''.join(ant))