def bolshee(a, b , c):
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    if c > b and c > a:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = bolshee(num1, num2, num3)
print(num4)
