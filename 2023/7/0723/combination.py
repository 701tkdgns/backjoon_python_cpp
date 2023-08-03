# def combination(arr, r):
#     arr = sorted(arr)
#
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#
#     generate([])
# combination('ABCDE', 2)

# def combination(arr, r):
#     arr = sorted(arr)
#
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#     generate([])
#
# combination("ABCDE", 2)

# def combination(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for nxt in combination(arr[i + 1:], r - 1):
#                 yield [arr[i]] + nxt
#
#
# for a in combination('ABCDE', 2):
#     print(a)

def combination(arr, r):
    _arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        start = _arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(_arr)):
            chosen.append(_arr[i])
            generate(chosen)
            chosen.pop()

    generate([])


def permutation(arr, r):
    _arr = sorted(arr)
    visit = [0] * len(arr)

    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        for i in range(len(_arr)):
            if visit[i] == 0:
                visit[i] = 1
                chosen.append(_arr[i])
                generate(chosen)
                chosen.pop()
                visit[i] = 0

    generate([])


permutation("ABCD", 2)
# combination("ABCD", 2)
