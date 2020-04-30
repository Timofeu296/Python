def factorial(a):
    b = 1
    for i in range(a):
        b = b * a
        a = a - 1
    return b

n = int(input())
k = int(input())
c = factorial(n)/ (factorial(k) * factorial(n - k))
print(int(c))