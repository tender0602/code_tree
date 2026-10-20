arr1=[]
arr2=[]
for i in range(3) :
    a= list(map(int,input().split()))
    arr1.append(a)

blank=input()
for i in range(3) :
    b= list(map(int,input().split()))
    arr2.append(b)

result = [[arr1[i][j] * arr2[i][j] for j in range(3)] for i in range(3)]
for i in range(3):
    print(*result[i])