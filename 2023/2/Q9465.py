T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    dp = [0 for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]
    for _ in range(2):
        lst.append(list(map(int, input().split())))
    for i in range(N):
