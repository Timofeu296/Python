a = [3, 5, 6, 8, 10, 11, 0, 86, 0, 1826, 94648, 0, 3, 17]
b = 0
for i in a:
    if i == 0:
        b = b + 1
if b >= 3:
    print("Yes")
