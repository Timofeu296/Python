a = int(input())
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(b)
for i in range(3):
    for j in range(3):
        b[i][j] = b[i][j] * a
        #print(b[i][j])
print(b)