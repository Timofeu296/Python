def sravnim(a, b, c):
    if a == b == c:
        return 3
    elif a == c or a == b or b == c:
        return 2
    else:
        return 0


num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = sravnim(num1, num2, num3)
print(num4)
