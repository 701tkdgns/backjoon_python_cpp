N = int(input())
lst = [0 for _ in range(91)]
lst[1], lst[2] = 1, 1
if N >= 3:
    for i in range(3, N + 1):
        lst[i] = lst[i-1] + lst[i-2]
print(lst[N])