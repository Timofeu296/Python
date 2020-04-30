def syma2(a):
    b = 0
    while a > 0:
        c = a % 10
        a = a // 10
        if c % 2 != 0:
            b = b + c
    return b


num1 = int(input())
num2 = syma2(num1)
print(num2)