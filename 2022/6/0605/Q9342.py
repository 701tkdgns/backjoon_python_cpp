import re
P = re.compile("^[A-F]?A+F+C+[A-F]?$")
for _ in range(int(input())):
    if P.match(input()) is not None:
        print("Infected!")
    else:
        print("Good")