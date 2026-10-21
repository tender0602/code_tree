n,m = tuple(map(int,input().split()))

matrix =[ [ 0 for _ in range(n)] for _ in range(n)]

for i in range(m) :
    x,y = tuple(map(int,input().split()))
    matrix[x-1][y-1] = x*y



for dot in matrix : 
    print(*dot)