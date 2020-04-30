def syma(a):
    b = 0
    while a > 0:
        b = b + a % 10
        a = a // 10
    return b

num1 = int(input())
num2 = syma(num1)
print(num2)