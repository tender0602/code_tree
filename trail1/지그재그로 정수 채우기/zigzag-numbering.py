n, m = map(int, input().split())

cnt = 0

matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m) :
    if i%2!=0 :
        for j in range(n-1,-1,-1) :
            matrix[j][i] = cnt
            cnt +=1

    else : 
        for j in range(n) :
            matrix[j][i] = cnt
            cnt +=1


for i in matrix :
    print(*i)