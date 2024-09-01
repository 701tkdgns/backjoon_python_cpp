import re


def solution(files):
    def key_func(file):
        # 정규 표현식을 사용하여 HEAD, NUMBER, TAIL을 분리합니다.
        match = re.match(r"([a-zA-Z- .]+)(\d{1,5})", file)
        head = match.group(1).lower()
        number = int(match.group(2))
        return (head, number)

    # 정렬: HEAD 우선, 그 다음 NUMBER, 마지막으로 원래 순서 유지
    files.sort(key=key_func)
    return files