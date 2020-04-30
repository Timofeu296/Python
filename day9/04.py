a =  int(input("Укажите число от 1 до 8: "))
b =  int(input("Укажите число от 1 до 8: "))
c =  int(input("Укажите число от 1 до 8: "))
d =  int(input("Укажите число от 1 до 8: "))
if c == a or d == b or c - a == d - b or b - d == a - c or c - a == b - d or a - c == d - b :
    print("Yes")
else:
    print("No")
