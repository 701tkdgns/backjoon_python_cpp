def check():
    if dna["A"] >= a and dna["C"] >= c and dna["G"] >= g and dna["T"] >= t:
        return True
    else:
        return False


S, P = map(int, input().split())
string = input()
cnt = 0
dna = {"A": 0, "C": 0, "G": 0, "T": 0}
a, c, g, t = map(int, input().split())
s, e = 0, P
chk = string[:P]
for i in range(len(chk)):
    dna[chk[i]] += 1
if check():
    cnt += 1
for i in range(S - P):
    dna[string[s + i]] -= 1
    dna[string[e + i]] += 1
    if check():
        cnt += 1
print(cnt)
