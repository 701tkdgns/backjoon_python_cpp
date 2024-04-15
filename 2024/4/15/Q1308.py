def dayArr(year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days[1] = 29
    return days


def findingDays(year, month, day):
    days = 0
    for i in range(1, year):
        date = dayArr(i)
        for j in range(12):
            days += date[j]
    date = dayArr(year)
    for i in range(month - 1):
        days += date[i]
    days += day
    return days


today = list(map(int, input().split()))
d_day = list(map(int, input().split()))
if today[0] + 1000 < d_day[0] or (today[0] + 1000 == d_day[0] and (today[1], today[2]) <= (d_day[1], d_day[2])):
    print('gg')
else:
    _today = findingDays(today[0], today[1], today[2])
    _d_day = findingDays(d_day[0], d_day[1], d_day[2])
    print('D-{}'.format(_d_day - _today))