S = input().split()
a, b, c = int(S[0]), int(S[2]), int(S[4])
tmp = 0
if S[1] == '+':
    tmp = a + b
elif S[1] == '-':
    tmp = a - b
elif S[1] == '*':
    tmp = a * b
elif S[1] == '/':
    tmp = a // b
if tmp == c:
    print("YES")
else:
    print("NO")