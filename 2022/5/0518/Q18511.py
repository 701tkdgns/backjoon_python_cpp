def backtracking(n):
    global tmp
    if len(n) >= len(str(N)):
        return
    for i in range(k):
        n += k_lst[i]
        if int(n) <= N and int(n) not in tmp:
            tmp.append(int(n))
        backtracking(n)
        n = n[:-1]


N, k = map(int, input().split())
k_lst = list(map(str, input().split()))
tmp = []
backtracking('')
print(max(tmp))
