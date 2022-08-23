N = int(input())
if N <= 3:
    print(1)
elif N >= 4:
    lst = [0 for _ in range(N + 1)]
    for i in range(1, 4):
        lst[i] = 1
    for i in range(4, N + 1):
        lst[i] = lst[i-1] + lst[i-3]
    print(lst[N])