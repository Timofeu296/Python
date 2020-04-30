def isprime(a):
    de = 0
    b = 0
    while de <= a:
        de = de + 1
        if a % de == 0:
            b = b + 1
    if b == 2:
        print(a)

n = int(input())
for i in range(1,n + 1):
   isprime(i)

