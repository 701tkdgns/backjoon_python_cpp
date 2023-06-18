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

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in combination(arr[i + 1:], r - 1):
                yield [arr[i]] + nxt


for a in combination('ABCDE', 2):
    print(a)
