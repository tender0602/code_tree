a,b=map(int,input().split())
matrix1=[]
matrix2=[]
for i in range(a):
    matrix1.append(list(map(int,input().split())))
for i in range(a):
    matrix2.append(list(map(int,input().split())))

answer = matrix1.copy()

for i in range(a) :
    for j in range(b) :
        if matrix1[i][j] == matrix2[i][j] :
            answer[i][j] = 0
        else :
            answer[i][j] = 1

for i in answer :
    print(*i)