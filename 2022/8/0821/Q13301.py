N = int(input())
if N <= 1:
    print(N*4)
else:
    lst = [0 for _ in range(N + 1)]
    lst[0], lst[1] = 1, 1
    for i in range(2, N + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    print(lst[N-1]*2 + 2*(lst[N-1]+lst[N-2]))