n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt_list=[]
cnt=0

for i in range(0,n-2) :
    for j in range(0,n-2) :
        for k in range(i,i+3):
            for l in range(j,j+3):
                if grid[k][l]==1 :
                    cnt +=1
    
        cnt_list.append(cnt)
        cnt=0

print(max(cnt_list))


