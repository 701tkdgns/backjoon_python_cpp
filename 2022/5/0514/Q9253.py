A = input()
B = input()
S = input()

cnt = 0
if S in A:
    cnt += 1
if S in B:
    cnt += 1

if cnt == 2:
    print("YES")
else:
    print("NO")
