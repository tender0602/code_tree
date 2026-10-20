matrix = []
answer=0
for i in range(4) : 
    matrix.append(list(map(int,input().split())))
    answer+=sum(matrix[i][0:i+1])
print(answer)