N1,N2 = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
answer = 'No'
for i in range(N1-N2+1) :
    if B[0] == A[i] :
        if B == A[i:i+N2] :
            answer = "Yes"
            break
print(answer)
