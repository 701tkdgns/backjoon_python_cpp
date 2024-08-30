import math


def check_erastwo(n: int):
    if n < 2: return False
    chk: bool = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            chk = False
            break
    return chk


def solution(n, k):
    answer = 0
    v = ""
    while (n > 0):
        v += str(n % k)
        n //= k
    v = ''.join(reversed(v))
    lst = v.split('0')
    for _num in lst:
        if _num != '' and check_erastwo(int(_num)):
            answer += 1

    return answer