a =  int(input("Укажите число от 1 до 8: "))
b =  int(input("Укажите число от 1 до 8: "))
c =  int(input("Укажите число от 1 до 8: "))
d =  int(input("Укажите число от 1 до 8: "))

if c == a + 1 and d == b + 1  or c == a - 1 and d == b - 1 or c == a - 1 and d == b or c == a and d == b - 1 or c == a + 1 and d == b or c == a and d == b + 1 or c == a + 1 and d == b - 1 or c == a - 1 and d == b + 1:
    print("Yes")
else:
    print("No")
