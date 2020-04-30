def chetnoe(a):
    if a % 2 == 0:
        return a + 2
    elif a % 2 != 0:
        a = a + 1
        return a


num1 = int(input())
num2 = chetnoe(num1)
print(num2)
