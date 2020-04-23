def phactorial(b):
    c = 1
    for i in range (1, b + 1):
        c = c * i
    return c


num1 = int(input())
num2 = phactorial(num1)
print(num2)
