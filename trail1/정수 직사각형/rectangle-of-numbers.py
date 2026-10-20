a,b = map(int,input().split())
arr = [[0 for _ in range(b)] for _ in range(a)]
num=1
for i in range(a):
    for j in range(b) :
        arr[i][j] = num
        num +=1

for row in arr :
    for x in row :
        print(x,end=' ')
    print()