test_stk = []


def push(data):
    test_stk.append(data)


def pop():
    data = test_stk[-1]
    del test_stk[-1]
    return data


for i in range(10):
    push(i)

print(pop())