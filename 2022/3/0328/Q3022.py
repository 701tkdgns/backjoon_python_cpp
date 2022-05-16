count = int(input())
childList = {}
warning = 0
total = 0
for i in range(count):
    name = input()
    if name not in childList:
        total += 1
        childList[name] = 1
    else:
        if childList[name] > total - childList[name]:
            warning += 1
        total += 1
        childList[name] += 1
    sortedList = sorted(childList.items(),
                        reverse=True,
                        key=lambda item: item[1])
print(warning)
