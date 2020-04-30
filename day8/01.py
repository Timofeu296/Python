a = int(input())
b = 0
c = 0
while a > 0:
    if a % 10 == 0:
        b =  b + 1
    if a % 10 == 9:
        c = c + 1
    a = a // 10
if c > b:
    print(9)
else:
    print(0)