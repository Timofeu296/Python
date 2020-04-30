def rasryad(a):
    b = 0
    while a > 0:
        a = a // 10
        b = b + 1
    return b


num1 = int(input())
num2 = rasryad(num1)
print(num2)