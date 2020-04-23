def our_pow(a, b):
    c = 1
    for i in range(b):
        c = c * a
    return c


num1 = int(input())
num2 = int(input())
num3 = our_pow(num1, num2)
print(num3)