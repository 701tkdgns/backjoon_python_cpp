import random


def binary_search(data, search):
    print(data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium + 1:], search)
        else:
            return binary_search(data[:medium], search)


data_list = random.sample(range(100000), 10000)
print(data_list)
data_list.sort()
print(binary_search(data_list, 66))
