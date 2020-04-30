def treugolnic(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b:
        return"Yes"
    else:
        return"No"


num1 = int(input())
num2= int(input())
num3 = int(input())
num4= treugolnic(num1, num2, num3)
print(num4)