n=int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i][0] =1

for i in range(1,n) :
    for j in range(1,n):
        matrix[i][j] = matrix[i-1][j-1]+matrix[i-1][j]

index = 0
for answer in matrix :
    print(*answer[0:index+1])
    index+=1

