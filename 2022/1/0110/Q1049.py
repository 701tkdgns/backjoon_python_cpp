N, M = map(int, input().split())  # N : 끊어진 기타줄 개수
lst = []
ans = 0
for _ in range(M):
    a, b = map(int, input().split())  # a : 패키지 가격(6개), b : 낱개 가격
    lst.append((a, b))
min_p, min_e = 1001, 1001
for pa, ea in lst:
    min_p, min_e = min(pa, min_p), min(ea, min_e)
if N <= 6:
    ans = min(min_p, min_e * N)
else:
    n = N // 6
    N %= 6
    ans = min(n * min_p, n * min_e * 6) + min(min_p, N*min_e)
print(ans)
