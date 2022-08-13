import sys
std = sys.stdin
keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"

while True:
    s = std.readline().rstrip()
    if s == '':
        break

    s_len = len(s)
    res = ''
    for index in range(s_len):
        if s[index] != ' ':
            keyboard_idx = keyboard.index(s[index])
            res += keyboard[keyboard_idx-1]
        else:
            res += ' '
    print(res)