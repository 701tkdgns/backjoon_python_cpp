def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):

        if len(chosen) == r:
            yield [chosen]

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    return generate([], used)


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i + 1:], r - 1):
                yield [arr[i]] + next


for i in permutation('ABCD', 2):
    print(i)
