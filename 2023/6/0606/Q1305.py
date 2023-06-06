def makePI(s):
    j, _s = 0, len(s)
    tmp = [0 for _ in range(_s)]
    for i in range(1, _s):
        while j > 0 and S[i] != S[j]:
            j = tmp[j - 1]
        if S[i] == S[j]:
            j += 1
            tmp[i] = j
    return tmp

L = int(input())
S = input()
s = len(S)
pi = makePI(S)
print(s - pi[s - 1])