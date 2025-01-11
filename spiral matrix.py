def cycle(st, en1, en2):
    global count
    direction=['right', 'down', 'left', 'up']
    dir=direction[0]
    if dir == 'right':
        for j in range (en1):
            if matrix[st][j]=='.':
                matrix[st][j]=count
                count+=1
        dir=direction[1]
    if dir == 'down':
        for i in range(en2):
            if matrix[i][en1]=='.':
                matrix[i][en1]=count
                count+=1
        dir=direction[2]
    if dir == 'left':
        for j in range(en1, 0, -1):
            if matrix[en2][j]=='.':
                matrix[en2][j]=count
                count+=1
        dir=direction[3]
    if dir == 'up':
        for i in range(en2, 0, -1):
            if matrix[i][st]=='.':
                matrix[i][st]=count
                count+=1
        dir=direction[0]

a=[int(i) for i in input().split()]
n=a[0]
m=a[1]
matrix=[]

for i in range(n):
    one=[]
    for j in range(m):
        one.append('.')
    matrix.append(one)

st_=0
en1_=m-1
en2_=n-1

count=1
while count <= n*m:
    cycle(st_, en1_, en2_)
    st_+=1
    en1_-=1
    en2_-=1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

