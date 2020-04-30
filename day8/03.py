def chisla(a):
    b = 0
    while a > 0:
        a = a // 10
        b = b + 1
    if b == 3:
        return "трехзначное"
    if b == 2:
        return "двухзначное"
    else:
        return "я не знаю"


num1 = int(input())
num2 = chisla(num1)
print(num2)
