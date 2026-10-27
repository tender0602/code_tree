n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt=0
a=1

for i in range(n) :
    for j in range(n-1) :
        if grid[i][j] == grid[i][j+1]:
            a+=1
        else :
            a=1
        if a==m :
            cnt+=1
            a=1
            break

a=1
for j in range(n) :
    for i in range(n-1) :
        if grid[i][j] == grid[i+1][j]:
            a+=1
        else :
            a=1
        if a==m :
            cnt+=1
            a=1
            break
if n==1 and m==1:
    print(2)
else :
    print(cnt)



