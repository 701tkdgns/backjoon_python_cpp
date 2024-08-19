N = int(input())
S = list(map(str, input().split()))
cheeses = set()
for s in S:
    if s.endswith("Cheese"):
        cheeses.add(s)
if len(cheeses) >= 4:
    print("yummy")
else:
    print("sad")