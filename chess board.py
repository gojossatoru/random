lol = [int(i) for i in input().split()]
a, b = lol[0], lol[1]
matrix = []
for i in range(a):
    one=[]
    for j in range(b):
        one.append('.')
    matrix.append(one)

for i in range(1, a+1):
    for j in range(1, b+1):
        if (i%2 == 0 and j%2 != 0) or (i%2 != 0 and j%2 == 0):
            matrix[i-1][j-1] = "*"

for i in range(a):
    print(*matrix[i])
