N = int(input())
fact = [1, 1]
chk = False
val = 0
for i in range(2, 21):
    fact.append(fact[i - 1] * i)
for i in range(20, -1, -1):
    if val + fact[i] < N:
        val += fact[i]
    elif val + fact[i] == N:
        chk = True
        break
print("YES" if chk else "NO")