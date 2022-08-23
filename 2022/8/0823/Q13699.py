N = int(input())
if N == 0:
    lst = [1]
else:
    lst = [0 for _ in range(N + 1)]
    lst[0] = 1
    lst[1] = 1
    for index in range(2, N + 1):
        for i in range(index):
            lst[index] += lst[i] * lst[index - i - 1]
print(lst[N])
