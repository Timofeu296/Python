a = [3, 5, 6, 8, 10, 11, 35, 86, 95, 1826, 94648, 5, 3, 17]
count = 0
for i in range(len(a)):
    if a[i - 1] > a[i] > a[i + 1]:
        count = count + 1
        print(count,)
        print(a[i])
        