a = [3, 5, 6, 8, 10, 11, 45, 86, 95, 1826, 94648, 0, 3, 17]
count = 0
for i in a:
    if i % 7 == 0 or i % 10 == 5:
        count = count + 1
print(count)