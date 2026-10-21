n,m = tuple(map(int,input().split()))

matrix =[ [ 0 for _ in range(n)] for _ in range(n)]
cnt=1
for i in range(m) :
    x,y = tuple(map(int,input().split()))
    matrix[x-1][y-1] = cnt
    cnt+=1


for dot in matrix : 
    print(*dot)