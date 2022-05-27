N, K = map(int, input().split())
lst = [0 for _ in range(N)]
for i in range(N):
    lst[i] = float(input())
lst.sort()
print(lst[K:(N-K)])
sub_avg = sum(lst[K:(N-K)]) / (N-(K*2))
cor_avg = (lst[K]*K + sum(lst[K:-K]) + lst[-(K+1)]*K) / N
print('%.2f' % sub_avg)
print('%.2f' % cor_avg)
