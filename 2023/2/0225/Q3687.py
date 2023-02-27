# http://blog.devjoshua.me/2019/11/30/boj-3687/

def big(n):
    tmp = ''
    if n % 2 == 0:
        while n != 0:
            tmp += '1'
            n -= 2
    else:
        tmp += '7'
        n -= 3
        while n != 0:
            tmp += '1'
            n -= 2
    return tmp


def small(n):
    dp = [0 for _ in range(101)]
    dp[2] = 1
    dp[3] = 7
    dp[4] = 4
    dp[5] = 2
    dp[6] = 6
    dp[7] = 8
    dp[8] = 10
    for i in range(9, 101):
        for j in range(3, 8):
            pass

    return dp[n]


T = int(input())
lst = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(T):
    N = int(input())
    b, s = '', ''
    b = big(N)
    s = small(N)
    print(s, b)
