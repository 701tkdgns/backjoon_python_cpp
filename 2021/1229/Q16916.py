# import sys
# import re
# S = sys.stdin.readline().rstrip()
# P = sys.stdin.readline().rstrip()
# pattern = re.compile(P)
# if pattern.search(S):
#     print(1)
# else:
#     print(0)

def makeTable(s):
    pattern = [0] * len(s)

    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pattern[j - 1]
        if s[i] == s[j]:
            j += 1
            pattern[i] = j
    return pattern


def kmp(s, p):
    pattern = makeTable(s)

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pattern[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            else:
                j += 1
    else:
        return False


s = input().strip()
p = input().strip()

print(1 if kmp(s, p) else 0)