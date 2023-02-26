a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
_A, _B = dict(), dict()
res = 0

for i in A:
    _A[i] = _A.get(i, 0)
for i in B:
    _B[i] = _B.get(i, 0)

for i in B:
    if _A.get(i) is not None:
        _A[i] = _A.get(i) - 1

for i in A:
    if _B.get(i) is not None:
        _B[i] = _B.get(i) - 1

_a, _b = a, b

for key in _A.keys():
    _a += _A.get(key)

for key in _B.keys():
    _b += _B.get(key)
res = _a + _b
print(res)