def step(a):
    while a > 1:
        a = a / 2
        if a == 2:
            return 1
    return 0
num1 = int(input('Введите число 1:' ))
num2 = step(num1)
if num2 == 1:
     print('Является')
else:
    print('Нет')
        