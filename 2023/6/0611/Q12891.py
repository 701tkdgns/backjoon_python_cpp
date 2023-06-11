s, p = map(int, input().split())
string = input()
a, c, g, t = map(int, input().split())
dna = {"A": 0, "C": 0, "G": 0, "T": 0}
res, cnt = 0, 0
start = string[:p]
for i in start:
    dna[i] += 1
if dna["A"] >= a and dna["C"] >= c and dna["G"] >= g and dna["T"] >= t:
    cnt += 1
start_idx, end_idx = 0, p
for i in range(len(string) - p):
    dna[string[start_idx + i]] -= 1
    dna[string[end_idx + i]] += 1
    if dna["A"] >= a and dna["C"] >= c and dna["G"] >= g and dna["T"] >= t:
        cnt += 1
print(cnt)