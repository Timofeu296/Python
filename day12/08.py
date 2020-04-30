a = [3, 5, 6, 8, 10, 11, 45, 86, 95, 1826, 94648, 0, 3, 17]
minimum = 5000000000
for i in a:
    if i < minimum and i % 10 == 5:
        minimum = i
print(minimum)
