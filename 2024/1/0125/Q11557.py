T = int(input())
for _ in range(T):
    N = int(input())
    _dict = {}
    res_key, res_value = '', 0
    for _ in range(N):
        a, b = input().split()
        _dict[a] = int(b)
    for key in _dict:
        if res_value < _dict[key]:
            res_key = key
            res_value = _dict[key]
    print(res_key)