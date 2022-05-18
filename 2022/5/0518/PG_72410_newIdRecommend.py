def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    tmp = ''
    for t in new_id:
        if 97 <= ord(t) <= 122:
            tmp += t
        elif 48 <= ord(t) <= 57:
            tmp += t
        elif t == '-':
            tmp += t
        elif t == '_':
            tmp += t
        elif t == '.':
            tmp += t
    new_id = tmp
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    answer = new_id
    return answer