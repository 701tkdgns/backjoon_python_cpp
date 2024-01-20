a, b = input().split()
min_a, min_b = int(a.replace("6", "5")), int(b.replace("6", "5"))
max_a, max_b = int(a.replace("5", "6")), int(b.replace("5", "6"))

print(min_a + min_b, max_a + max_b)
