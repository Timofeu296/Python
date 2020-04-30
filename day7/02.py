def delenie(a, b):
    while a > 0:
        c = a % 10
        a = a // 10
        if c == b:
            return 1
    return 0


def proverka(d, e):
    for i in range (1, 1001):
        c = delenie(i, e)
        if i % d == 0 or c == 1:
            print(i)
num1 =int(input())
num2 = int(input())
proverka(num1, num2)