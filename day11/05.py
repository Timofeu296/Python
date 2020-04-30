def calculator(a, b, c):
    if c == '/' and b == 0:
       return 'Stop! Division by zero!'
    elif c == '/':
        return a / b
    elif c == '+':
        return a + b
    elif c == '*':
        return a * b
    elif c == '-':
        return a - b
    else:
        return 'Не понял тебя'

num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
num3 = input('Введите знак операции: ')
num4 = calculator(num1, num2, num3)
print(num4)