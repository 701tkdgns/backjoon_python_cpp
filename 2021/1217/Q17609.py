def secondCheck(S, L, R):
    while L < R:
        if S[L] != S[R]:
            return False
        L += 1
        R -= 1
    return True


def firstCheck(S, L, R):
    while L < R:
        if S[L] == S[R]:
            L += 1
            R -= 1
        else:
            chk1 = secondCheck(S, L+1, R)
            chk2 = secondCheck(S, L, R-1)
            if chk1 or chk2:
                return 1
            else:
                return 2
    return 0


for _ in range(int(input())):
    S = input()
    L, R = 0, len(S) - 1
    res = firstCheck(S, L, R)
    print(res)