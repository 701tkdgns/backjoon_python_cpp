N = int(input())
candy = list(map(int, input().split()))
res = sum(candy)
if res % 2 == 0:
    print(res)
else:
    candy.sort()
    for c in candy:
        if (res - c) % 2 == 0:
            res -= c
            break
    print(res)