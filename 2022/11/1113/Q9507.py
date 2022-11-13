lst = [0 for _ in range(68)]
lst[0], lst[1] = 1, 1
lst[2] = 2
lst[3] = 4
for i in range(4, 68):
    lst[i] = lst[i-1] + lst[i-2] + lst[i-3] + lst[i-4]
for _ in range(int(input())):
    n = int(input())
    print(lst[n])
