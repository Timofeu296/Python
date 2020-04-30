a = [3, 5, 6, 8, 10, 11, 45, 86, 95, 1826, 94648, 0, 3, 17]
count = 0
for i in range(len(a)):
    if a[i] > a[i - 1]:
        count = count + 1
print(count)