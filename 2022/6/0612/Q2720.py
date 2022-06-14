for _ in range(int(input())):
    penny = [25, 10, 5, 1]
    N = int(input())
    lst = [0, 0, 0, 0]
    for i in range(4):
        lst[i] = N // penny[i]
        N = N % penny[i]
    print(*lst)