A = list(input())
B=[]
for i in range(1,len(A),2) : 
    B.append(A[i])

for i in range(len(B)-1,-1,-1) :
    print(B[i],end='')