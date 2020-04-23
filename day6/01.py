def our_pow(a, b):
    c = 1
    while b > 0:
        b = b - 1
        c = c * a
    return c


num1 = int(input())
num2 = int(input())
num3 = our_pow(num1, num2)
print(num3)
        