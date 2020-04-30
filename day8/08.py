def visocost(a):
    if a % 4 == 0 and a % 400 == 0 and a % 100 != 0:
        return "Yes"
    else:
        return "No"


num1 = int(input())
num2 = visocost(num1)
print(num2)
